import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { getExamsApi } from '../services/api/exams';
import { BookOpen, ArrowRight, Award, AlertCircle, RefreshCw } from 'lucide-react';
import { useAuth } from '../context/AuthContext';

const StudentDashboard = () => {
  const [exams, setExams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const { user } = useAuth();
  const navigate = useNavigate();

  const fetchExams = async () => {
    setLoading(true);
    setError('');
    try {
      const data = await getExamsApi();
      setExams(data || []);
    } catch (err) {
      console.error('Failed to load exams:', err);
      setError('Could not load exams. Please check your network or try again.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchExams();
  }, []);

  const handleSelectExam = (examId) => {
    navigate(`/exam/${examId}/instructions`);
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
      {/* Welcome banner */}
      <div className="bg-gradient-to-r from-indigo-700 via-indigo-600 to-purple-600 rounded-3xl p-8 text-white shadow-xl shadow-indigo-100 mb-10 flex flex-col md:flex-row md:items-center justify-between gap-6">
        <div>
          <span className="text-xs font-semibold uppercase tracking-widest text-indigo-200 bg-white/10 px-3 py-1 rounded-full inline-block mb-3">
            Candidate Portal
          </span>
          <h1 className="text-3xl font-extrabold tracking-tight">
            Welcome back, {user?.name || 'Student'}!
          </h1>
          <p className="text-indigo-100 text-sm mt-2 max-w-xl">
            Select an exam below to begin a timed practice session with instant AI grading and analytics.
          </p>
        </div>
        <div className="bg-white/10 backdrop-blur-md p-4 rounded-2xl flex items-center space-x-3 border border-white/20 self-start md:self-auto">
          <Award className="w-8 h-8 text-yellow-300 flex-shrink-0" />
          <div>
            <div className="text-xs text-indigo-100 uppercase tracking-wider font-semibold">Ready for Test</div>
            <div className="text-sm font-bold">{exams.length} Exams Available</div>
          </div>
        </div>
      </div>

      {/* Header and Refresh */}
      <div className="flex items-center justify-between mb-6">
        <div>
          <h2 className="text-xl font-bold text-gray-900 tracking-tight">Available Mock Exams</h2>
          <p className="text-xs text-gray-500 mt-0.5">Select an examination to view blueprint and instructions</p>
        </div>
        <button
          onClick={fetchExams}
          disabled={loading}
          className="flex items-center space-x-1.5 text-xs font-semibold text-indigo-600 hover:text-indigo-800 bg-indigo-50 hover:bg-indigo-100 px-3 py-1.5 rounded-lg transition-colors"
        >
          <RefreshCw className={`w-3.5 h-3.5 ${loading ? 'animate-spin' : ''}`} />
          <span>Refresh</span>
        </button>
      </div>

      {/* Error State */}
      {error && (
        <div className="mb-8 p-4 rounded-2xl bg-red-50 border border-red-200 flex items-start space-x-3 text-red-700 text-sm">
          <AlertCircle className="w-5 h-5 flex-shrink-0 text-red-500 mt-0.5" />
          <div className="flex-1">
            <p className="font-semibold">{error}</p>
            <button
              onClick={fetchExams}
              className="mt-2 text-xs font-bold text-red-700 underline hover:text-red-800"
            >
              Try Again
            </button>
          </div>
        </div>
      )}

      {/* Loading State */}
      {loading ? (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {[1, 2, 3].map((n) => (
            <div
              key={n}
              className="bg-white rounded-2xl border border-gray-200 p-6 animate-pulse space-y-4 shadow-sm"
            >
              <div className="w-10 h-10 bg-gray-200 rounded-xl"></div>
              <div className="h-5 bg-gray-200 rounded w-3/4"></div>
              <div className="h-4 bg-gray-100 rounded w-1/2"></div>
              <div className="h-10 bg-gray-200 rounded-xl mt-4"></div>
            </div>
          ))}
        </div>
      ) : exams.length === 0 ? (
        <div className="bg-white rounded-2xl border border-gray-200 p-12 text-center shadow-sm">
          <BookOpen className="w-12 h-12 text-gray-400 mx-auto mb-3" />
          <h3 className="text-base font-bold text-gray-800">No Exams Available</h3>
          <p className="text-xs text-gray-500 mt-1 max-w-sm mx-auto">
            There are currently no active exams configured in the portal. Please contact your administrator.
          </p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {exams.map((exam) => (
            <div
              key={exam.id}
              className="bg-white rounded-2xl border border-gray-200 hover:border-indigo-300 hover:shadow-lg transition-all duration-200 p-6 flex flex-col justify-between group"
            >
              <div>
                <div className="flex items-center justify-between mb-4">
                  <div className="w-10 h-10 rounded-xl bg-indigo-50 text-indigo-600 flex items-center justify-center font-bold text-sm">
                    {exam.name.charAt(0)}
                  </div>
                  <span className="text-xs font-semibold text-indigo-700 bg-indigo-50 px-2.5 py-1 rounded-full uppercase tracking-wider">
                    {exam.category || 'General'}
                  </span>
                </div>

                <h3 className="text-lg font-bold text-gray-900 group-hover:text-indigo-600 transition-colors">
                  {exam.name}
                </h3>
                <p className="text-xs text-gray-500 mt-2 line-clamp-3 leading-relaxed">
                  {exam.description || 'Full-length standard mock test paper based on the latest competitive blueprint.'}
                </p>
              </div>

              <div className="mt-6 pt-4 border-t border-gray-100 flex items-center justify-between">
                <span className="text-xs font-medium text-gray-400">Exam ID #{exam.id}</span>
                <button
                  onClick={() => handleSelectExam(exam.id)}
                  className="flex items-center space-x-1.5 text-xs font-bold text-white bg-indigo-600 hover:bg-indigo-700 px-4 py-2 rounded-xl transition-all shadow-md shadow-indigo-100 group-hover:translate-x-0.5"
                >
                  <span>Select Exam</span>
                  <ArrowRight className="w-3.5 h-3.5" />
                </button>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default StudentDashboard;

