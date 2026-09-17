import React, { useState, useEffect, useCallback } from 'react';
import { useParams, useNavigate, useLocation } from 'react-router-dom';
import { getPaperQuestionsApi, getQuestionsByExamApi, getExamsApi } from '../services/api/exams';
import { getAttemptApi, getAttemptAnswersApi, saveAnswerApi, submitAttemptApi } from '../services/api/attempts';
import QuestionCard from '../components/QuestionCard';
import QuestionPalette from '../components/QuestionPalette';
import Timer from '../components/Timer';
import { Send, AlertCircle, CheckCircle2, HelpCircle } from 'lucide-react';

const ExamTaking = () => {
  const { attemptId } = useParams();
  const navigate = useNavigate();
  const location = useLocation();

  const [attempt, setAttempt] = useState(() => {
    if (location.state?.attempt) return location.state.attempt;
    const stored = sessionStorage.getItem(`attempt_${attemptId}`);
    return stored ? JSON.parse(stored) : null;
  });

  const [questions, setQuestions] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [answers, setAnswers] = useState({});
  const [loading, setLoading] = useState(true);
  const [savingAnswer, setSavingAnswer] = useState(false);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState('');
  const [showSubmitModal, setShowSubmitModal] = useState(false);

  // Load attempt, previously saved answers, and questions
  useEffect(() => {
    let isMounted = true;

    const loadExamSession = async () => {
      setLoading(true);
      setError('');

      try {
        let currentAttempt = attempt;

        // If attempt not in local state, fetch directly from backend API
        if (!currentAttempt?.paper_id || !currentAttempt?.started_at) {
          try {
            currentAttempt = await getAttemptApi(Number(attemptId));
            if (isMounted) {
              setAttempt(currentAttempt);
              sessionStorage.setItem(`attempt_${attemptId}`, JSON.stringify(currentAttempt));
            }
          } catch (err) {
            throw new Error('Unable to retrieve examination attempt from server.');
          }
        }

        // If attempt is already marked submitted, redirect to result screen
        if (currentAttempt?.status === 'submitted') {
          navigate(`/result/${attemptId}`, { replace: true });
          return;
        }

        if (!currentAttempt?.paper_id) {
          throw new Error('Attempt details not found. Please start the exam again.');
        }

        // 1. Fetch paper questions
        const paperQuestions = await getPaperQuestionsApi(currentAttempt.paper_id);
        if (!paperQuestions || paperQuestions.length === 0) {
          throw new Error('No questions found for this exam paper.');
        }

        // 2. Fetch question details
        let examId = currentAttempt.examId;
        let examQuestions = [];

        if (examId) {
          examQuestions = await getQuestionsByExamApi(examId);
        } else {
          // Fallback: search across exams
          const allExams = await getExamsApi();
          for (const ex of allExams) {
            const qList = await getQuestionsByExamApi(ex.id).catch(() => []);
            if (qList.some((q) => q.id === paperQuestions[0]?.question_id)) {
              examQuestions = qList;
              break;
            }
          }
        }

        // Map paper questions to full question objects
        const questionMap = new Map(examQuestions.map((q) => [q.id, q]));
        const ordered = paperQuestions
          .map((pq) => {
            const detail = questionMap.get(pq.question_id);
            return {
              ...detail,
              id: pq.question_id,
              questionNumber: pq.question_number,
            };
          })
          .sort((a, b) => a.questionNumber - b.questionNumber);

        // 3. Fetch any existing saved answers from backend to restore state after refresh
        try {
          const savedAnswersList = await getAttemptAnswersApi(Number(attemptId));
          const answersMap = {};
          if (Array.isArray(savedAnswersList)) {
            savedAnswersList.forEach((ans) => {
              if (ans.selected_option) {
                answersMap[ans.question_id] = ans.selected_option;
              }
            });
          }
          if (isMounted) {
            setAnswers(answersMap);
          }
        } catch (ansErr) {
          console.warn('Could not restore prior answers from server:', ansErr);
        }

        if (isMounted) {
          setQuestions(ordered);
        }
      } catch (err) {
        console.error('Failed to load exam questions:', err);
        if (isMounted) {
          setError(err.message || 'Failed to load exam questions. Please try again.');
        }
      } finally {
        if (isMounted) {
          setLoading(false);
        }
      }
    };

    loadExamSession();

    return () => {
      isMounted = false;
    };
  }, [attemptId, navigate]);

  // Handle student selecting an answer
  const handleSelectOption = async (option) => {
    if (!questions[currentIndex]) return;
    const currentQ = questions[currentIndex];

    // Optimistically update local answer state
    setAnswers((prev) => ({
      ...prev,
      [currentQ.id]: option,
    }));

    setSavingAnswer(true);
    try {
      await saveAnswerApi(Number(attemptId), currentQ.id, option);
    } catch (err) {
      console.error('Failed to save answer:', err);
      const detail = err.response?.data?.detail;
      if (err.response?.status === 400 && detail === 'Attempt time has expired') {
        setError('Time has expired! Submitting your exam now...');
        handleSubmitExam(true);
      } else {
        setError('Failed to sync answer with server. Please check your connection.');
      }
    } finally {
      setSavingAnswer(false);
    }
  };

  // Handle final submission
  const handleSubmitExam = useCallback(
    async (isAutoSubmit = false) => {
      if (submitting) return;
      setSubmitting(true);
      setError('');

      try {
        await submitAttemptApi(Number(attemptId));
        // Clear stored attempt
        sessionStorage.removeItem(`attempt_${attemptId}`);
        navigate(`/result/${attemptId}`, { replace: true });
      } catch (err) {
        console.error('Submit error:', err);
        const detail = err.response?.data?.detail;
        // If already submitted or expired, navigate to result directly
        if (
          err.response?.status === 400 &&
          (detail === 'Attempt is not active' || detail === 'Attempt time has expired')
        ) {
          sessionStorage.removeItem(`attempt_${attemptId}`);
          navigate(`/result/${attemptId}`, { replace: true });
        } else {
          setError(typeof detail === 'string' ? detail : 'Failed to submit exam. Please try again.');
          setSubmitting(false);
        }
      }
    },
    [attemptId, submitting, navigate]
  );

  const handleTimerExpire = useCallback(() => {
    handleSubmitExam(true);
  }, [handleSubmitExam]);

  if (loading) {
    return (
      <div className="max-w-6xl mx-auto px-4 py-20 text-center">
        <div className="w-12 h-12 border-4 border-indigo-600 border-t-transparent rounded-full animate-spin mx-auto mb-4"></div>
        <h2 className="text-base font-bold text-gray-800">Loading Exam Session...</h2>
        <p className="text-xs text-gray-500 mt-1">Please wait while the test paper and saved answers initialize.</p>
      </div>
    );
  }

  if (error && questions.length === 0) {
    return (
      <div className="max-w-md mx-auto px-4 py-16 text-center">
        <AlertCircle className="w-12 h-12 text-red-500 mx-auto mb-3" />
        <h2 className="text-lg font-bold text-gray-900">Exam Loading Error</h2>
        <p className="text-xs text-gray-500 mt-1 mb-6">{error}</p>
        <button
          onClick={() => navigate('/dashboard')}
          className="px-4 py-2 bg-indigo-600 text-white rounded-xl text-xs font-semibold hover:bg-indigo-700"
        >
          Return to Dashboard
        </button>
      </div>
    );
  }

  const currentQuestion = questions[currentIndex];
  const answeredCount = Object.values(answers).filter(Boolean).length;
  const unansweredCount = questions.length - answeredCount;

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
      {/* Top Bar with Timer and Submit Button */}
      <div className="bg-white rounded-2xl shadow-sm border border-gray-200 px-6 py-4 mb-6 flex flex-wrap items-center justify-between gap-4">
        <div>
          <span className="text-xs font-semibold uppercase tracking-wider text-gray-400">Mock Examination</span>
          <h1 className="text-lg font-bold text-gray-900">
            {attempt?.examName || 'Assessment Paper'}
          </h1>
        </div>

        <div className="flex items-center space-x-4">
          {attempt && attempt.started_at && attempt.duration_seconds && (
            <Timer
              startedAt={attempt.started_at}
              durationSeconds={attempt.duration_seconds}
              onExpire={handleTimerExpire}
            />
          )}

          <button
            type="button"
            onClick={() => setShowSubmitModal(true)}
            disabled={submitting}
            className="flex items-center space-x-2 bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs px-5 py-2.5 rounded-xl transition-all shadow-md shadow-emerald-100 active:scale-[0.99]"
          >
            <Send className="w-3.5 h-3.5" />
            <span>Submit Exam</span>
          </button>
        </div>
      </div>

      {error && (
        <div className="mb-6 p-4 rounded-xl bg-amber-50 border border-amber-200 text-amber-900 text-xs flex items-center justify-between">
          <span>{error}</span>
          <button onClick={() => setError('')} className="font-bold underline ml-2">
            Dismiss
          </button>
        </div>
      )}

      {/* Main Examination Layout: Question Card (left) & Palette (right) */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2">
          <QuestionCard
            question={currentQuestion}
            questionNumber={currentIndex + 1}
            totalQuestions={questions.length}
            selectedOption={answers[currentQuestion?.id] || null}
            onSelectOption={handleSelectOption}
            onPrev={() => setCurrentIndex((prev) => Math.max(0, prev - 1))}
            onNext={() => setCurrentIndex((prev) => Math.min(questions.length - 1, prev + 1))}
            hasPrev={currentIndex > 0}
            hasNext={currentIndex < questions.length - 1}
            isSaving={savingAnswer}
          />
        </div>

        <div className="lg:col-span-1">
          <QuestionPalette
            totalQuestions={questions.length}
            currentIndex={currentIndex}
            answers={answers}
            questions={questions}
            onSelectQuestion={(idx) => setCurrentIndex(idx)}
          />
        </div>
      </div>

      {/* Confirmation Modal */}
      {showSubmitModal && (
        <div className="fixed inset-0 z-50 bg-black/40 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="bg-white rounded-2xl max-w-md w-full p-6 shadow-2xl border border-gray-100">
            <div className="w-12 h-12 rounded-2xl bg-indigo-50 text-indigo-600 flex items-center justify-center mx-auto mb-4">
              <HelpCircle className="w-6 h-6" />
            </div>

            <h3 className="text-lg font-bold text-gray-900 text-center">Confirm Exam Submission</h3>
            <p className="text-xs text-gray-500 text-center mt-1 mb-6">
              Are you sure you want to finish and submit your exam? You cannot modify answers after submission.
            </p>

            <div className="bg-gray-50 rounded-xl p-4 mb-6 grid grid-cols-2 gap-4 text-center">
              <div className="bg-white p-3 rounded-lg border border-gray-100 shadow-sm">
                <div className="text-xs text-gray-500 font-medium">Answered</div>
                <div className="text-lg font-bold text-emerald-600">{answeredCount}</div>
              </div>
              <div className="bg-white p-3 rounded-lg border border-gray-100 shadow-sm">
                <div className="text-xs text-gray-500 font-medium">Unanswered</div>
                <div className="text-lg font-bold text-gray-500">{unansweredCount}</div>
              </div>
            </div>

            <div className="flex space-x-3">
              <button
                type="button"
                onClick={() => setShowSubmitModal(false)}
                disabled={submitting}
                className="flex-1 py-2.5 rounded-xl border border-gray-300 text-gray-700 font-semibold text-xs hover:bg-gray-50"
              >
                Continue Exam
              </button>
              <button
                type="button"
                onClick={() => {
                  setShowSubmitModal(false);
                  handleSubmitExam(false);
                }}
                disabled={submitting}
                className="flex-1 py-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs hover:bg-emerald-700 shadow-md shadow-emerald-100 flex items-center justify-center space-x-1"
              >
                {submitting ? 'Submitting...' : 'Yes, Submit'}
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default ExamTaking;
