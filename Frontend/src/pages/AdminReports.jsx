import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { getExamsApi } from '../services/api/exams';
import { getAllQuestionsApi } from '../services/api/admin';
import { 
  BarChart3, 
  TrendingUp, 
  CheckCircle2, 
  Clock, 
  AlertTriangle, 
  PieChart, 
  ArrowLeft,
  FileSpreadsheet
} from 'lucide-react';

const AdminReports = () => {
  const [exams, setExams] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const examList = await getExamsApi();
        setExams(examList);
      } catch (err) {
        console.error('Failed to load reports data:', err);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, []);

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between mb-8 pb-6 border-b border-gray-200 gap-4">
        <div>
          <div className="flex items-center space-x-2">
            <span className="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-blue-100 text-blue-800">
              Exam Analytics & Reporting
            </span>
            <span className="text-xs text-gray-400 font-mono">Full-Stack Core</span>
          </div>
          <h1 className="text-2xl font-black text-gray-900 mt-1 tracking-tight">
            Assessment Reports & Logs
          </h1>
          <p className="text-sm text-gray-500 mt-0.5">
            Operational summaries of mock examinations, question distributions, and scoring status.
          </p>
        </div>

        <Link
          to="/admin"
          className="inline-flex items-center space-x-2 bg-gray-100 hover:bg-gray-200 text-gray-700 font-bold text-xs px-4 py-2.5 rounded-xl transition-colors self-start sm:self-auto"
        >
          <ArrowLeft className="w-4 h-4" />
          <span>Back to Control Center</span>
        </Link>
      </div>

      {/* High-level Status */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-6 mb-8">
        <div className="bg-white p-5 rounded-2xl border border-gray-200 shadow-sm">
          <div className="flex items-center justify-between">
            <span className="text-xs font-bold text-gray-500 uppercase">Scoring Engine</span>
            <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-100 text-emerald-800">
              Active
            </span>
          </div>
          <div className="text-xl font-bold text-gray-900 mt-2">Deterministic Scoring</div>
          <p className="text-xs text-gray-500 mt-1">
            Calculates correct (+mark), wrong (-penalty), and unanswered accurately on submission.
          </p>
        </div>

        <div className="bg-white p-5 rounded-2xl border border-gray-200 shadow-sm">
          <div className="flex items-center justify-between">
            <span className="text-xs font-bold text-gray-500 uppercase">Session Integrity</span>
            <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-100 text-emerald-800">
              Enforced
            </span>
          </div>
          <div className="text-xl font-bold text-gray-900 mt-2">UTC Server-Side Timer</div>
          <p className="text-xs text-gray-500 mt-1">
            Strict expiration enforcement protects against client clock manipulation and auto-submits on time.
          </p>
        </div>

        <div className="bg-white p-5 rounded-2xl border border-gray-200 shadow-sm">
          <div className="flex items-center justify-between">
            <span className="text-xs font-bold text-gray-500 uppercase">State Recovery</span>
            <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-100 text-emerald-800">
              Resilient
            </span>
          </div>
          <div className="text-xl font-bold text-gray-900 mt-2">Real-Time Sync</div>
          <p className="text-xs text-gray-500 mt-1">
            Student answers auto-save on select; re-hydrated from database on reconnect or page refresh.
          </p>
        </div>
      </div>

      {/* Exam Categories Summary Table */}
      <div className="bg-white rounded-2xl border border-gray-200 p-6 shadow-sm mb-8">
        <h3 className="text-base font-bold text-gray-900 mb-4 flex items-center space-x-2">
          <FileSpreadsheet className="w-4 h-4 text-indigo-600" />
          <span>Configured Exam Portals</span>
        </h3>

        {loading ? (
          <div className="p-8 text-center text-xs text-gray-500">Loading exam catalogue...</div>
        ) : exams.length === 0 ? (
          <div className="p-8 text-center text-xs text-gray-500">No exams configured yet.</div>
        ) : (
          <div className="overflow-x-auto">
            <table className="w-full text-left text-xs">
              <thead className="bg-gray-50 text-gray-600 font-bold border-b border-gray-200 uppercase tracking-wider">
                <tr>
                  <th className="py-3 px-4">Exam ID</th>
                  <th className="py-3 px-4">Exam Name</th>
                  <th className="py-3 px-4">Category</th>
                  <th className="py-3 px-4">Description</th>
                  <th className="py-3 px-4">Status</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-gray-100 font-medium">
                {exams.map((ex) => (
                  <tr key={ex.id} className="hover:bg-gray-50/75 transition-colors">
                    <td className="py-3 px-4 font-mono text-gray-400">#{ex.id}</td>
                    <td className="py-3 px-4 font-bold text-gray-900">{ex.name}</td>
                    <td className="py-3 px-4">
                      <span className="px-2 py-0.5 rounded text-[11px] font-semibold bg-gray-100 text-gray-700 uppercase">
                        {ex.category}
                      </span>
                    </td>
                    <td className="py-3 px-4 text-gray-500 max-w-xs truncate">
                      {ex.description || 'Standard competitive examination paper'}
                    </td>
                    <td className="py-3 px-4">
                      <span className="inline-flex items-center space-x-1 text-emerald-600 font-semibold">
                        <CheckCircle2 className="w-3.5 h-3.5" />
                        <span>Ready for Mock Tests</span>
                      </span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>

      {/* Pending Data Analyst Specialist Section */}
      <div className="bg-gray-50 rounded-2xl border border-dashed border-gray-300 p-8 text-center">
        <div className="w-12 h-12 rounded-2xl bg-white text-indigo-600 border border-gray-200 flex items-center justify-center mx-auto mb-3 shadow-sm">
          <PieChart className="w-6 h-6" />
        </div>
        <h3 className="text-base font-bold text-gray-900">Advanced Statistical & Cohort Analytics</h3>
        <p className="text-xs text-gray-500 max-w-xl mx-auto mt-1 mb-4">
          Detailed student percentile curves, item response theory (IRT), and question discrimination indexes are reserved for the dedicated Data Analyst role. Core exam results, marks, and answer reviews are fully functional.
        </p>
        <span className="inline-block px-3 py-1 rounded-full text-xs font-semibold bg-amber-100 text-amber-900 border border-amber-200">
          Module Status: Pending Specialist Engine Integration
        </span>
      </div>
    </div>
  );
};

export default AdminReports;

