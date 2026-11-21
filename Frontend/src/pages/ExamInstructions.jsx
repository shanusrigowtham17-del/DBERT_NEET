import React, { useState, useEffect } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';
import { getExamsApi, getQuestionsByExamApi } from '../services/api/exams';
import { buildPaperApi, startAttemptApi } from '../services/api/attempts';
import { BookOpen, Clock, AlertTriangle, CheckCircle, ArrowLeft, Play, AlertCircle } from 'lucide-react';

const ExamInstructions = () => {
  const { examId } = useParams();
  const navigate = useNavigate();

  const [exam, setExam] = useState(null);
  const [availableQuestions, setAvailableQuestions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [starting, setStarting] = useState(false);
  const [error, setError] = useState('');
  const [agreed, setAgreed] = useState(false);

  useEffect(() => {
    const loadExamData = async () => {
      setLoading(true);
      setError('');
      try {
        const [exams, questions] = await Promise.all([
          getExamsApi(),
          getQuestionsByExamApi(examId).catch(() => []),
        ]);

        const selectedExam = exams.find((e) => String(e.id) === String(examId));
        if (!selectedExam) {
          setError('Exam not found.');
        } else {
          setExam(selectedExam);
          setAvailableQuestions(questions || []);
        }
      } catch (err) {
        console.error('Failed to load exam instructions:', err);
        setError('Failed to load exam details. Please try again.');
      } finally {
        setLoading(false);
      }
    };

    loadExamData();
  }, [examId]);

  const handleStartExam = async () => {
    if (!agreed) {
      setError('Please acknowledge that you have read and understood the instructions.');
      return;
    }

    if (availableQuestions.length === 0) {
      setError('This exam does not have any questions available in the database yet.');
      return;
    }

    setStarting(true);
    setError('');

    try {
      // 1. Build or fetch paper using available question count
      const questionCount = Math.min(25, availableQuestions.length);
      const paper = await buildPaperApi(Number(examId), questionCount);

      // 2. Start attempt
      const attempt = await startAttemptApi(paper.id);

      // Store attempt info in sessionStorage for smooth reload/recovery
      sessionStorage.setItem(
        `attempt_${attempt.id}`,
        JSON.stringify({
          ...attempt,
          examId: Number(examId),
          examName: exam?.name,
        })
      );

      // 3. Navigate to exam taking page
      navigate(`/exam/${attempt.id}`, {
        state: {
          attempt,
          exam,
          paper,
        },
      });
    } catch (err) {
      console.error('Failed to start exam:', err);
      const detail = err.response?.data?.detail;
      setError(typeof detail === 'string' ? detail : 'Failed to start the exam. Please try again.');
      setStarting(false);
    }
  };

  if (loading) {
    return (
      <div className="max-w-4xl mx-auto px-4 py-16 text-center">
        <div className="w-10 h-10 border-4 border-indigo-600 border-t-transparent rounded-full animate-spin mx-auto mb-4"></div>
        <p className="text-gray-600 font-medium text-sm">Loading exam instructions...</p>
      </div>
    );
  }

  if (!exam) {
    return (
      <div className="max-w-md mx-auto px-4 py-16 text-center">
        <AlertCircle className="w-12 h-12 text-red-500 mx-auto mb-3" />
        <h2 className="text-lg font-bold text-gray-900">Exam Not Found</h2>
        <p className="text-sm text-gray-500 mt-1 mb-6">The exam you requested could not be located.</p>
        <Link
          to="/dashboard"
          className="inline-flex items-center space-x-2 text-sm font-semibold text-indigo-600 hover:text-indigo-800"
        >
          <ArrowLeft className="w-4 h-4" />
          <span>Return to Dashboard</span>
        </Link>
      </div>
    );
  }

  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 py-10">
      <Link
        to="/dashboard"
        className="inline-flex items-center space-x-1.5 text-xs font-semibold text-gray-500 hover:text-gray-800 mb-6 transition-colors"
      >
        <ArrowLeft className="w-4 h-4" />
        <span>Back to Dashboard</span>
      </Link>

      <div className="bg-white rounded-3xl shadow-xl border border-gray-100 overflow-hidden">
        {/* Header */}
        <div className="bg-gradient-to-r from-indigo-700 to-indigo-600 px-8 py-8 text-white">
          <span className="text-xs font-semibold uppercase tracking-widest text-indigo-200 bg-white/10 px-3 py-1 rounded-full inline-block mb-3">
            Exam Instructions
          </span>
          <h1 className="text-2xl sm:text-3xl font-bold tracking-tight">{exam.name}</h1>
          <p className="text-indigo-100 text-xs sm:text-sm mt-2 max-w-2xl leading-relaxed">
            {exam.description || 'Standard competitive assessment paper.'}
          </p>

          <div className="mt-6 flex flex-wrap gap-4 text-xs font-medium text-indigo-100">
            <div className="flex items-center space-x-1.5 bg-white/10 px-3 py-1.5 rounded-lg">
              <Clock className="w-4 h-4 text-indigo-200" />
              <span>Timed Session</span>
            </div>
            <div className="flex items-center space-x-1.5 bg-white/10 px-3 py-1.5 rounded-lg">
              <BookOpen className="w-4 h-4 text-indigo-200" />
              <span>Questions Available: {availableQuestions.length}</span>
            </div>
          </div>
        </div>

        {/* Content Body */}
        <div className="p-8 space-y-6">
          {error && (
            <div className="p-4 rounded-xl bg-red-50 border border-red-200 flex items-start space-x-3 text-red-700 text-sm">
              <AlertCircle className="w-5 h-5 flex-shrink-0 text-red-500 mt-0.5" />
              <span>{error}</span>
            </div>
          )}

          <div>
            <h2 className="text-base font-bold text-gray-900 uppercase tracking-wider mb-3">
              General Instructions
            </h2>
            <ul className="space-y-3 text-sm text-gray-600">
              <li className="flex items-start space-x-2.5">
                <CheckCircle className="w-4 h-4 text-emerald-600 flex-shrink-0 mt-0.5" />
                <span>
                  The clock will be set at the server. The countdown timer at the top displays the remaining time to complete the test.
                </span>
              </li>
              <li className="flex items-start space-x-2.5">
                <CheckCircle className="w-4 h-4 text-emerald-600 flex-shrink-0 mt-0.5" />
                <span>
                  When the timer reaches zero, the exam will submit automatically. Any unsubmitted responses will be evaluated.
                </span>
              </li>
              <li className="flex items-start space-x-2.5">
                <CheckCircle className="w-4 h-4 text-emerald-600 flex-shrink-0 mt-0.5" />
                <span>
                  You can navigate between questions freely using the Question Palette on the right or the Next/Previous buttons.
                </span>
              </li>
              <li className="flex items-start space-x-2.5">
                <CheckCircle className="w-4 h-4 text-emerald-600 flex-shrink-0 mt-0.5" />
                <span>
                  Selecting an option automatically saves your answer to the server. You can change your choice anytime before final submission.
                </span>
              </li>
            </ul>
          </div>

          <div className="p-4 rounded-xl bg-amber-50 border border-amber-200 flex items-start space-x-3 text-amber-800 text-xs leading-relaxed">
            <AlertTriangle className="w-5 h-5 flex-shrink-0 text-amber-600 mt-0.5" />
            <div>
              <span className="font-bold block mb-0.5">Important Security Notice</span>
              Server-side timer verification is authoritative. Closing or refreshing your browser window does not pause the exam clock.
            </div>
          </div>

          {/* Declaration Checkbox */}
          <div className="pt-4 border-t border-gray-100">
            <label className="flex items-start space-x-3 cursor-pointer select-none">
              <input
                type="checkbox"
                checked={agreed}
                onChange={(e) => setAgreed(e.target.checked)}
                className="w-4 h-4 text-indigo-600 border-gray-300 rounded focus:ring-indigo-500 mt-0.5"
              />
              <span className="text-xs text-gray-700 leading-relaxed font-medium">
                I have read, understood and agree to abide by the exam instructions. I understand that any attempt after timer expiry will be rejected.
              </span>
            </label>
          </div>

          {/* Action Button */}
          <div className="pt-4 flex justify-end">
            <button
              type="button"
              onClick={handleStartExam}
              disabled={starting || !agreed}
              className={`px-8 py-3.5 rounded-xl font-bold text-sm flex items-center space-x-2 transition-all shadow-lg ${
                starting || !agreed
                  ? 'bg-gray-200 text-gray-400 cursor-not-allowed shadow-none'
                  : 'bg-indigo-600 hover:bg-indigo-700 text-white shadow-indigo-200 active:scale-[0.99]'
              }`}
            >
              <Play className="w-4 h-4 fill-current" />
              <span>{starting ? 'Building Paper & Starting...' : 'I Am Ready — Start Exam'}</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ExamInstructions;

