import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { getResultApi } from '../services/api/attempts';
import { Award, CheckCircle2, XCircle, HelpCircle, ArrowRight, AlertCircle, RefreshCw } from 'lucide-react';

const ExamResult = () => {
  const { attemptId } = useParams();
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  const fetchResult = async () => {
    setLoading(true);
    setError('');
    try {
      const data = await getResultApi(Number(attemptId));
      setResult(data);
    } catch (err) {
      console.error('Failed to load result:', err);
      const detail = err.response?.data?.detail;
      setError(typeof detail === 'string' ? detail : 'Result not found or could not be loaded.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchResult();
  }, [attemptId]);

  if (loading) {
    return (
      <div className="max-w-2xl mx-auto px-4 py-20 text-center">
        <div className="w-12 h-12 border-4 border-indigo-600 border-t-transparent rounded-full animate-spin mx-auto mb-4"></div>
        <h2 className="text-base font-bold text-gray-800">Calculating Exam Performance...</h2>
        <p className="text-xs text-gray-500 mt-1">Retrieving official evaluated score and analytics from the server.</p>
      </div>
    );
  }

  if (error || !result) {
    return (
      <div className="max-w-md mx-auto px-4 py-16 text-center">
        <AlertCircle className="w-12 h-12 text-red-500 mx-auto mb-3" />
        <h2 className="text-lg font-bold text-gray-900">Result Unavailable</h2>
        <p className="text-xs text-gray-500 mt-1 mb-6">{error || 'Unable to display result for this attempt.'}</p>
        <div className="flex justify-center space-x-3">
          <button
            onClick={fetchResult}
            className="px-4 py-2 bg-gray-100 hover:bg-gray-200 text-gray-800 rounded-xl text-xs font-semibold"
          >
            Try Again
          </button>
          <Link
            to="/dashboard"
            className="px-4 py-2 bg-indigo-600 hover:bg-indigo-700 text-white rounded-xl text-xs font-semibold"
          >
            Go to Dashboard
          </Link>
        </div>
      </div>
    );
  }

  const accuracy =
    result.attempted_questions > 0
      ? Math.round((result.correct_answers / result.attempted_questions) * 100)
      : 0;

  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
      {/* Result Hero Card */}
      <div className="bg-white rounded-3xl shadow-xl border border-gray-100 overflow-hidden mb-8">
        <div className="bg-gradient-to-r from-indigo-700 via-indigo-600 to-purple-600 p-8 text-white text-center">
          <div className="w-16 h-16 bg-white/10 rounded-2xl flex items-center justify-center mx-auto mb-4 backdrop-blur-sm border border-white/20">
            <Award className="w-8 h-8 text-yellow-300" />
          </div>
          <span className="text-xs font-semibold uppercase tracking-widest text-indigo-200 bg-white/10 px-3 py-1 rounded-full inline-block mb-2">
            Assessment Completed
          </span>
          <h1 className="text-3xl font-extrabold tracking-tight">Official Exam Result</h1>
          <p className="text-xs text-indigo-100 mt-1">Attempt ID #{result.attempt_id}</p>

          <div className="mt-6 inline-block bg-white/15 backdrop-blur-md rounded-2xl px-8 py-4 border border-white/20">
            <div className="text-xs uppercase tracking-wider text-indigo-100 font-semibold">Total Score</div>
            <div className="text-4xl font-black text-white mt-0.5">{result.score}</div>
          </div>
        </div>

        {/* Breakdown Metric Cards */}
        <div className="p-8">
          <h2 className="text-sm font-bold uppercase tracking-wider text-gray-400 mb-4">
            Performance Breakdown
          </h2>

          <div className="grid grid-cols-2 sm:grid-cols-3 gap-4 mb-8">
            <div className="bg-gray-50 rounded-2xl p-4 border border-gray-100">
              <div className="text-xs font-medium text-gray-500 mb-1">Total Questions</div>
              <div className="text-2xl font-bold text-gray-900">{result.total_questions}</div>
            </div>

            <div className="bg-gray-50 rounded-2xl p-4 border border-gray-100">
              <div className="text-xs font-medium text-gray-500 mb-1">Attempted</div>
              <div className="text-2xl font-bold text-indigo-600">{result.attempted_questions}</div>
            </div>

            <div className="bg-emerald-50/50 rounded-2xl p-4 border border-emerald-100">
              <div className="text-xs font-medium text-emerald-700 mb-1 flex items-center space-x-1">
                <CheckCircle2 className="w-3.5 h-3.5" />
                <span>Correct</span>
              </div>
              <div className="text-2xl font-bold text-emerald-600">{result.correct_answers}</div>
            </div>

            <div className="bg-red-50/50 rounded-2xl p-4 border border-red-100">
              <div className="text-xs font-medium text-red-700 mb-1 flex items-center space-x-1">
                <XCircle className="w-3.5 h-3.5" />
                <span>Wrong</span>
              </div>
              <div className="text-2xl font-bold text-red-600">{result.wrong_answers}</div>
            </div>

            <div className="bg-gray-50 rounded-2xl p-4 border border-gray-100">
              <div className="text-xs font-medium text-gray-500 mb-1 flex items-center space-x-1">
                <HelpCircle className="w-3.5 h-3.5" />
                <span>Unanswered</span>
              </div>
              <div className="text-2xl font-bold text-gray-600">{result.unanswered_questions}</div>
            </div>

            <div className="bg-indigo-50/50 rounded-2xl p-4 border border-indigo-100">
              <div className="text-xs font-medium text-indigo-700 mb-1">Accuracy</div>
              <div className="text-2xl font-bold text-indigo-700">{accuracy}%</div>
            </div>
          </div>

          <div className="flex flex-col sm:flex-row items-center justify-between gap-4 pt-6 border-t border-gray-100">
            <span className="text-xs text-gray-400">
              Scores computed according to exam blueprint negative marking scheme.
            </span>
            <Link
              to="/dashboard"
              className="w-full sm:w-auto inline-flex items-center justify-center space-x-2 bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-xs px-6 py-3 rounded-xl transition-all shadow-md shadow-indigo-100"
            >
              <span>Back to Dashboard</span>
              <ArrowRight className="w-3.5 h-3.5" />
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ExamResult;

