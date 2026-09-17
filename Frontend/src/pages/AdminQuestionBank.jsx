import React, { useState, useEffect } from 'react';
import { getExamsApi, getTopicsApi } from '../services/api/exams';
import { getAllQuestionsApi, createQuestionApi } from '../services/api/admin';
import { 
  HelpCircle, 
  Plus, 
  Search, 
  Filter, 
  CheckCircle2, 
  AlertCircle, 
  X, 
  ChevronRight,
  Sparkles,
  BookOpen
} from 'lucide-react';

const AdminQuestionBank = () => {
  const [exams, setExams] = useState([]);
  const [selectedExamId, setSelectedExamId] = useState('');
  const [questions, setQuestions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [successMsg, setSuccessMsg] = useState('');

  // Modal State
  const [showAddModal, setShowAddModal] = useState(false);
  const [examTopics, setExamTopics] = useState([]);
  const [submittingQuestion, setSubmittingQuestion] = useState(false);
  const [formData, setFormData] = useState({
    exam_id: '',
    topic_id: '',
    text: '',
    option_a: '',
    option_b: '',
    option_c: '',
    option_d: '',
    correct_option: 'A',
    difficulty: 'medium',
    source: 'Curated Assessment Bank',
    explanation: '',
  });

  // Load exams on mount
  useEffect(() => {
    const fetchExams = async () => {
      try {
        const examList = await getExamsApi();
        setExams(examList);
        if (examList.length > 0) {
          // Default to first exam or all
          setSelectedExamId('');
        }
      } catch (err) {
        console.error('Failed to load exams', err);
        setError('Failed to load exam categories.');
      }
    };
    fetchExams();
  }, []);

  // Load questions whenever filter changes
  useEffect(() => {
    const fetchQuestions = async () => {
      setLoading(true);
      setError('');
      try {
        const examIdNum = selectedExamId ? Number(selectedExamId) : null;
        const list = await getAllQuestionsApi(examIdNum);
        setQuestions(list);
      } catch (err) {
        console.error('Failed to load questions:', err);
        setError('Unable to load question bank.');
      } finally {
        setLoading(false);
      }
    };
    fetchQuestions();
  }, [selectedExamId]);

  // Load topics when exam changes in modal form
  const handleExamChangeInForm = async (e) => {
    const examId = e.target.value;
    setFormData((prev) => ({ ...prev, exam_id: examId, topic_id: '' }));
    if (!examId) {
      setExamTopics([]);
      return;
    }
    try {
      const topics = await getTopicsApi(Number(examId));
      setExamTopics(topics);
      if (topics.length > 0) {
        setFormData((prev) => ({ ...prev, topic_id: topics[0].id }));
      }
    } catch (err) {
      console.error('Failed to load topics for exam', err);
    }
  };

  const handleOpenAddModal = async () => {
    setShowAddModal(true);
    setSuccessMsg('');
    const initialExamId = selectedExamId || (exams.length > 0 ? exams[0].id : '');
    setFormData((prev) => ({
      ...prev,
      exam_id: initialExamId,
      text: '',
      option_a: '',
      option_b: '',
      option_c: '',
      option_d: '',
      correct_option: 'A',
      difficulty: 'medium',
      source: 'Curated Assessment Bank',
      explanation: '',
    }));
    if (initialExamId) {
      try {
        const topics = await getTopicsApi(Number(initialExamId));
        setExamTopics(topics);
        if (topics.length > 0) {
          setFormData((prev) => ({ ...prev, topic_id: topics[0].id }));
        }
      } catch (err) {
        console.error('Failed to load topics', err);
      }
    }
  };

  const handleCreateQuestion = async (e) => {
    e.preventDefault();
    if (!formData.exam_id || !formData.topic_id || !formData.text.trim()) {
      alert('Please fill out all required fields.');
      return;
    }

    setSubmittingQuestion(true);
    try {
      const payload = {
        exam_id: Number(formData.exam_id),
        topic_id: Number(formData.topic_id),
        text: formData.text.trim(),
        option_a: formData.option_a.trim(),
        option_b: formData.option_b.trim(),
        option_c: formData.option_c.trim(),
        option_d: formData.option_d.trim(),
        correct_option: formData.correct_option.trim().toUpperCase(),
        difficulty: formData.difficulty,
        source: formData.source.trim(),
        explanation: formData.explanation ? formData.explanation.trim() : null,
      };

      const newQ = await createQuestionApi(payload);
      setQuestions((prev) => [newQ, ...prev]);
      setShowAddModal(false);
      setSuccessMsg(`Question #${newQ.id} created successfully!`);
    } catch (err) {
      console.error('Failed to create question:', err);
      alert(err.response?.data?.detail || 'Failed to create question.');
    } finally {
      setSubmittingQuestion(false);
    }
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between mb-8 pb-6 border-b border-gray-200 gap-4">
        <div>
          <div className="flex items-center space-x-2">
            <span className="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-emerald-100 text-emerald-800">
              Question Management
            </span>
            <span className="text-xs text-gray-400 font-mono">SQLite Repository</span>
          </div>
          <h1 className="text-2xl font-black text-gray-900 mt-1 tracking-tight">
            Curated Question Bank
          </h1>
          <p className="text-sm text-gray-500 mt-0.5">
            Inspect, filter, and author questions stored in the real examination database.
          </p>
        </div>

        <button
          onClick={handleOpenAddModal}
          className="flex items-center space-x-2 bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-xs px-4 py-2.5 rounded-xl shadow-sm transition-colors self-start sm:self-auto"
        >
          <Plus className="w-4 h-4" />
          <span>Add New Question</span>
        </button>
      </div>

      {successMsg && (
        <div className="mb-6 p-4 rounded-xl bg-emerald-50 border border-emerald-200 text-emerald-900 text-xs flex items-center justify-between">
          <div className="flex items-center space-x-2">
            <CheckCircle2 className="w-4 h-4 text-emerald-600" />
            <span>{successMsg}</span>
          </div>
          <button onClick={() => setSuccessMsg('')} className="font-bold underline ml-2">
            Dismiss
          </button>
        </div>
      )}

      {/* Filter Bar */}
      <div className="bg-white rounded-2xl border border-gray-200 p-4 mb-6 flex flex-wrap items-center justify-between gap-4 shadow-sm">
        <div className="flex items-center space-x-3">
          <Filter className="w-4 h-4 text-gray-400" />
          <span className="text-xs font-bold text-gray-700 uppercase tracking-wider">Filter by Exam:</span>
          <select
            value={selectedExamId}
            onChange={(e) => setSelectedExamId(e.target.value)}
            className="text-xs font-semibold bg-gray-50 border border-gray-300 rounded-lg px-3 py-1.5 focus:outline-none focus:ring-2 focus:ring-indigo-500"
          >
            <option value="">All Exams ({questions.length} Questions)</option>
            {exams.map((ex) => (
              <option key={ex.id} value={ex.id}>
                {ex.name} ({ex.category})
              </option>
            ))}
          </select>
        </div>

        <div className="text-xs text-gray-500 font-medium">
          Showing <span className="font-bold text-gray-900">{questions.length}</span> verified questions
        </div>
      </div>

      {/* Question List */}
      {loading ? (
        <div className="bg-white rounded-2xl border border-gray-200 p-12 text-center shadow-sm">
          <div className="w-8 h-8 border-4 border-indigo-600 border-t-transparent rounded-full animate-spin mx-auto mb-3"></div>
          <p className="text-xs text-gray-500">Loading questions from database...</p>
        </div>
      ) : questions.length === 0 ? (
        <div className="bg-white rounded-2xl border border-gray-200 p-12 text-center shadow-sm">
          <HelpCircle className="w-12 h-12 text-gray-300 mx-auto mb-3" />
          <h3 className="text-base font-bold text-gray-800">No questions found</h3>
          <p className="text-xs text-gray-500 mt-1 mb-4">
            No questions match your filter. You can add one using the button above.
          </p>
        </div>
      ) : (
        <div className="space-y-4">
          {questions.map((q, idx) => (
            <div
              key={q.id}
              className="bg-white rounded-2xl border border-gray-200 p-6 shadow-sm hover:border-gray-300 transition-colors"
            >
              <div className="flex flex-wrap items-center justify-between gap-2 mb-3">
                <div className="flex items-center space-x-2">
                  <span className="w-6 h-6 rounded-full bg-indigo-50 text-indigo-700 text-xs font-bold flex items-center justify-center">
                    {idx + 1}
                  </span>
                  <span className="text-xs font-mono text-gray-400">ID #{q.id}</span>
                  <span className="px-2 py-0.5 rounded text-[11px] font-semibold bg-gray-100 text-gray-700 capitalize">
                    {q.difficulty}
                  </span>
                  <span className="px-2 py-0.5 rounded text-[11px] font-medium bg-blue-50 text-blue-700">
                    {q.source}
                  </span>
                </div>

                <div className="flex items-center space-x-2">
                  <span className="text-xs font-semibold text-gray-500">Answer Key:</span>
                  <span className="px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-100 text-emerald-800">
                    Option {q.correct_option || 'N/A'}
                  </span>
                </div>
              </div>

              {/* Question Body */}
              <p className="text-sm font-semibold text-gray-900 mb-4 leading-relaxed">
                {q.text}
              </p>

              {/* Options Grid */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 mb-4">
                <div
                  className={`p-3 rounded-xl border text-xs flex items-start space-x-2 ${
                    q.correct_option === 'A'
                      ? 'border-emerald-300 bg-emerald-50/50 font-bold text-emerald-900'
                      : 'border-gray-200 bg-gray-50 text-gray-700'
                  }`}
                >
                  <span className="font-bold text-gray-500">A.</span>
                  <span>{q.option_a}</span>
                </div>
                <div
                  className={`p-3 rounded-xl border text-xs flex items-start space-x-2 ${
                    q.correct_option === 'B'
                      ? 'border-emerald-300 bg-emerald-50/50 font-bold text-emerald-900'
                      : 'border-gray-200 bg-gray-50 text-gray-700'
                  }`}
                >
                  <span className="font-bold text-gray-500">B.</span>
                  <span>{q.option_b}</span>
                </div>
                <div
                  className={`p-3 rounded-xl border text-xs flex items-start space-x-2 ${
                    q.correct_option === 'C'
                      ? 'border-emerald-300 bg-emerald-50/50 font-bold text-emerald-900'
                      : 'border-gray-200 bg-gray-50 text-gray-700'
                  }`}
                >
                  <span className="font-bold text-gray-500">C.</span>
                  <span>{q.option_c}</span>
                </div>
                <div
                  className={`p-3 rounded-xl border text-xs flex items-start space-x-2 ${
                    q.correct_option === 'D'
                      ? 'border-emerald-300 bg-emerald-50/50 font-bold text-emerald-900'
                      : 'border-gray-200 bg-gray-50 text-gray-700'
                  }`}
                >
                  <span className="font-bold text-gray-500">D.</span>
                  <span>{q.option_d}</span>
                </div>
              </div>

              {/* Explanation if present */}
              {q.explanation && (
                <div className="text-xs bg-indigo-50/50 border border-indigo-100 rounded-xl p-3 text-indigo-900">
                  <span className="font-bold">Explanation: </span>
                  <span>{q.explanation}</span>
                </div>
              )}
            </div>
          ))}
        </div>
      )}

      {/* Add Question Modal */}
      {showAddModal && (
        <div className="fixed inset-0 z-50 bg-black/40 backdrop-blur-sm flex items-center justify-center p-4 overflow-y-auto">
          <div className="bg-white rounded-2xl max-w-2xl w-full p-6 shadow-2xl border border-gray-100 max-h-[90vh] overflow-y-auto">
            <div className="flex items-center justify-between pb-4 border-b border-gray-100 mb-4">
              <h2 className="text-base font-bold text-gray-900 flex items-center space-x-2">
                <Plus className="w-4 h-4 text-indigo-600" />
                <span>Add Question to Database</span>
              </h2>
              <button
                onClick={() => setShowAddModal(false)}
                className="text-gray-400 hover:text-gray-600 p-1 rounded-lg"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            <form onSubmit={handleCreateQuestion} className="space-y-4 text-xs">
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                  <label className="block font-bold text-gray-700 mb-1">Target Exam *</label>
                  <select
                    value={formData.exam_id}
                    onChange={handleExamChangeInForm}
                    required
                    className="w-full bg-gray-50 border border-gray-300 rounded-xl px-3 py-2 font-medium"
                  >
                    <option value="">Select Exam</option>
                    {exams.map((ex) => (
                      <option key={ex.id} value={ex.id}>
                        {ex.name}
                      </option>
                    ))}
                  </select>
                </div>

                <div>
                  <label className="block font-bold text-gray-700 mb-1">Topic *</label>
                  <select
                    value={formData.topic_id}
                    onChange={(e) => setFormData({ ...formData, topic_id: e.target.value })}
                    required
                    className="w-full bg-gray-50 border border-gray-300 rounded-xl px-3 py-2 font-medium"
                  >
                    <option value="">Select Topic</option>
                    {examTopics.map((top) => (
                      <option key={top.id} value={top.id}>
                        {top.name}
                      </option>
                    ))}
                  </select>
                </div>
              </div>

              <div>
                <label className="block font-bold text-gray-700 mb-1">Question Text *</label>
                <textarea
                  rows={3}
                  value={formData.text}
                  onChange={(e) => setFormData({ ...formData, text: e.target.value })}
                  placeholder="Enter the full question stem..."
                  required
                  className="w-full bg-gray-50 border border-gray-300 rounded-xl p-3 font-medium focus:ring-2 focus:ring-indigo-500"
                />
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                <div>
                  <label className="block font-bold text-gray-700 mb-1">Option A *</label>
                  <input
                    type="text"
                    value={formData.option_a}
                    onChange={(e) => setFormData({ ...formData, option_a: e.target.value })}
                    required
                    className="w-full bg-gray-50 border border-gray-300 rounded-xl px-3 py-2 font-medium"
                  />
                </div>
                <div>
                  <label className="block font-bold text-gray-700 mb-1">Option B *</label>
                  <input
                    type="text"
                    value={formData.option_b}
                    onChange={(e) => setFormData({ ...formData, option_b: e.target.value })}
                    required
                    className="w-full bg-gray-50 border border-gray-300 rounded-xl px-3 py-2 font-medium"
                  />
                </div>
                <div>
                  <label className="block font-bold text-gray-700 mb-1">Option C *</label>
                  <input
                    type="text"
                    value={formData.option_c}
                    onChange={(e) => setFormData({ ...formData, option_c: e.target.value })}
                    required
                    className="w-full bg-gray-50 border border-gray-300 rounded-xl px-3 py-2 font-medium"
                  />
                </div>
                <div>
                  <label className="block font-bold text-gray-700 mb-1">Option D *</label>
                  <input
                    type="text"
                    value={formData.option_d}
                    onChange={(e) => setFormData({ ...formData, option_d: e.target.value })}
                    required
                    className="w-full bg-gray-50 border border-gray-300 rounded-xl px-3 py-2 font-medium"
                  />
                </div>
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
                <div>
                  <label className="block font-bold text-gray-700 mb-1">Correct Answer *</label>
                  <select
                    value={formData.correct_option}
                    onChange={(e) => setFormData({ ...formData, correct_option: e.target.value })}
                    required
                    className="w-full bg-emerald-50 border border-emerald-300 text-emerald-900 font-bold rounded-xl px-3 py-2"
                  >
                    <option value="A">Option A</option>
                    <option value="B">Option B</option>
                    <option value="C">Option C</option>
                    <option value="D">Option D</option>
                  </select>
                </div>

                <div>
                  <label className="block font-bold text-gray-700 mb-1">Difficulty</label>
                  <select
                    value={formData.difficulty}
                    onChange={(e) => setFormData({ ...formData, difficulty: e.target.value })}
                    className="w-full bg-gray-50 border border-gray-300 rounded-xl px-3 py-2 font-medium"
                  >
                    <option value="easy">Easy</option>
                    <option value="medium">Medium</option>
                    <option value="hard">Hard</option>
                  </select>
                </div>

                <div>
                  <label className="block font-bold text-gray-700 mb-1">Source Tag</label>
                  <input
                    type="text"
                    value={formData.source}
                    onChange={(e) => setFormData({ ...formData, source: e.target.value })}
                    className="w-full bg-gray-50 border border-gray-300 rounded-xl px-3 py-2 font-medium"
                  />
                </div>
              </div>

              <div>
                <label className="block font-bold text-gray-700 mb-1">Explanation (Optional)</label>
                <textarea
                  rows={2}
                  value={formData.explanation}
                  onChange={(e) => setFormData({ ...formData, explanation: e.target.value })}
                  placeholder="Provide rational or solution steps..."
                  className="w-full bg-gray-50 border border-gray-300 rounded-xl p-3 font-medium"
                />
              </div>

              <div className="flex space-x-3 pt-4 border-t border-gray-100">
                <button
                  type="button"
                  onClick={() => setShowAddModal(false)}
                  disabled={submittingQuestion}
                  className="flex-1 py-2.5 rounded-xl border border-gray-300 text-gray-700 font-semibold hover:bg-gray-50"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  disabled={submittingQuestion}
                  className="flex-1 py-2.5 rounded-xl bg-indigo-600 text-white font-bold hover:bg-indigo-700 shadow-md shadow-indigo-100 flex items-center justify-center space-x-1"
                >
                  {submittingQuestion ? 'Saving to DB...' : 'Save Question'}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};

export default AdminQuestionBank;

