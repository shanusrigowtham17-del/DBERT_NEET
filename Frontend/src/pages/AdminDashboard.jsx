import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { getExamsApi } from '../services/api/exams';
import { getAllQuestionsApi, getExamBlueprintsApi } from '../services/api/admin';
import { 
  ShieldCheck, 
  BookOpen, 
  HelpCircle, 
  Layers, 
  BarChart3, 
  PlusCircle, 
  ExternalLink,
  Cpu,
  Bot,
  PieChart
} from 'lucide-react';

const AdminDashboard = () => {
  const [stats, setStats] = useState({
    examsCount: 0,
    questionsCount: 0,
    blueprintsCount: 0,
    loading: true,
    error: '',
  });

  useEffect(() => {
    const fetchAdminStats = async () => {
      try {
        const [exams, questions, blueprints] = await Promise.all([
          getExamsApi().catch(() => []),
          getAllQuestionsApi().catch(() => []),
          getExamBlueprintsApi().catch(() => []),
        ]);

        setStats({
          examsCount: exams.length,
          questionsCount: questions.length,
          blueprintsCount: blueprints.length,
          loading: false,
          error: '',
        });
      } catch (err) {
        console.error('Failed to load admin stats:', err);
        setStats((prev) => ({
          ...prev,
          loading: false,
          error: 'Failed to load system metrics.',
        }));
      }
    };

    fetchAdminStats();
  }, []);

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      {/* Header */}
      <div className="flex flex-col md:flex-row md:items-center md:justify-between mb-8 pb-6 border-b border-gray-200">
        <div>
          <div className="flex items-center space-x-2">
            <span className="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-purple-100 text-purple-800">
              Administrative Control Center
            </span>
            <span className="text-xs text-gray-400 font-mono">v1.0.0</span>
          </div>
          <h1 className="text-2xl font-black text-gray-900 mt-1 tracking-tight">
            Portal Administration & Configuration
          </h1>
          <p className="text-sm text-gray-500 mt-0.5">
            Manage exam categories, question banks, test blueprints, and review system status.
          </p>
        </div>

        <div className="mt-4 md:mt-0 flex items-center space-x-3">
          <Link
            to="/admin/questions"
            className="flex items-center space-x-2 bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-xs px-4 py-2.5 rounded-xl shadow-sm transition-colors"
          >
            <PlusCircle className="w-4 h-4" />
            <span>Manage Question Bank</span>
          </Link>
          <Link
            to="/dashboard"
            className="flex items-center space-x-1.5 bg-gray-100 hover:bg-gray-200 text-gray-700 font-medium text-xs px-3.5 py-2.5 rounded-xl transition-colors"
          >
            <span>Student Portal View</span>
            <ExternalLink className="w-3.5 h-3.5" />
          </Link>
        </div>
      </div>

      {/* Metrics Row */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-6 mb-10">
        <div className="bg-white p-6 rounded-2xl border border-gray-200 shadow-sm flex items-center space-x-4">
          <div className="w-12 h-12 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center">
            <BookOpen className="w-6 h-6" />
          </div>
          <div>
            <div className="text-xs font-semibold uppercase text-gray-400">Total Exams</div>
            <div className="text-2xl font-black text-gray-900 mt-0.5">
              {stats.loading ? '...' : stats.examsCount}
            </div>
            <div className="text-xs text-blue-600 font-medium mt-0.5">Configured Exam Types</div>
          </div>
        </div>

        <div className="bg-white p-6 rounded-2xl border border-gray-200 shadow-sm flex items-center space-x-4">
          <div className="w-12 h-12 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center">
            <HelpCircle className="w-6 h-6" />
          </div>
          <div>
            <div className="text-xs font-semibold uppercase text-gray-400">Question Bank</div>
            <div className="text-2xl font-black text-gray-900 mt-0.5">
              {stats.loading ? '...' : stats.questionsCount}
            </div>
            <div className="text-xs text-emerald-600 font-medium mt-0.5">Verified Questions in DB</div>
          </div>
        </div>

        <div className="bg-white p-6 rounded-2xl border border-gray-200 shadow-sm flex items-center space-x-4">
          <div className="w-12 h-12 rounded-xl bg-purple-50 text-purple-600 flex items-center justify-center">
            <Layers className="w-6 h-6" />
          </div>
          <div>
            <div className="text-xs font-semibold uppercase text-gray-400">Blueprints</div>
            <div className="text-2xl font-black text-gray-900 mt-0.5">
              {stats.loading ? '...' : stats.blueprintsCount}
            </div>
            <div className="text-xs text-purple-600 font-medium mt-0.5">Paper Generation Rules</div>
          </div>
        </div>
      </div>

      {/* Quick Action Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-10">
        <div className="bg-gradient-to-br from-indigo-900 to-indigo-950 text-white rounded-2xl p-6 shadow-md">
          <div className="flex items-center justify-between mb-4">
            <span className="text-xs font-bold uppercase tracking-wider text-indigo-300">Question Management</span>
            <HelpCircle className="w-5 h-5 text-indigo-400" />
          </div>
          <h2 className="text-lg font-bold">Curated Question Repository</h2>
          <p className="text-xs text-indigo-200 mt-1 mb-6 leading-relaxed">
            Create, verify, and inspect multiple-choice questions across UPSC, SSC, and Banking exams. All questions are linked to exam topics and verified answer keys.
          </p>
          <Link
            to="/admin/questions"
            className="inline-flex items-center space-x-2 bg-white text-indigo-900 font-bold text-xs px-4 py-2 rounded-xl hover:bg-indigo-50 transition-colors shadow-sm"
          >
            <span>Open Question Bank</span>
            <ExternalLink className="w-3.5 h-3.5" />
          </Link>
        </div>

        <div className="bg-gradient-to-br from-slate-900 to-slate-950 text-white rounded-2xl p-6 shadow-md">
          <div className="flex items-center justify-between mb-4">
            <span className="text-xs font-bold uppercase tracking-wider text-slate-300">Assessment Analytics</span>
            <BarChart3 className="w-5 h-5 text-slate-400" />
          </div>
          <h2 className="text-lg font-bold">Performance Logs & Reports</h2>
          <p className="text-xs text-slate-300 mt-1 mb-6 leading-relaxed">
            View student examination records, submission times, negative marking penalties, and overall score distributions.
          </p>
          <Link
            to="/admin/reports"
            className="inline-flex items-center space-x-2 bg-white text-slate-900 font-bold text-xs px-4 py-2 rounded-xl hover:bg-slate-50 transition-colors shadow-sm"
          >
            <span>Open Reports</span>
            <ExternalLink className="w-3.5 h-3.5" />
          </Link>
        </div>
      </div>

      {/* Specialist Modules & Architectural Boundary Status */}
      <div className="bg-white rounded-2xl border border-gray-200 p-6 shadow-sm">
        <div className="flex items-center space-x-3 mb-4">
          <div className="p-2 bg-amber-50 text-amber-700 rounded-lg">
            <ShieldCheck className="w-5 h-5" />
          </div>
          <div>
            <h3 className="text-sm font-bold text-gray-900">Specialist Subsystem Integration Status</h3>
            <p className="text-xs text-gray-500">
              Role boundaries strictly maintained. Pending external specialized modules are displayed with clean unconfigured states.
            </p>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 pt-2">
          {/* AI/ML Module */}
          <div className="border border-gray-200 rounded-xl p-4 bg-gray-50/50">
            <div className="flex items-center justify-between mb-2">
              <div className="flex items-center space-x-2">
                <Bot className="w-4 h-4 text-purple-600" />
                <span className="text-xs font-bold text-gray-800">AI / LLM Question Generator</span>
              </div>
              <span className="px-2 py-0.5 rounded text-[10px] font-semibold bg-amber-100 text-amber-800">
                Pending Module
              </span>
            </div>
            <p className="text-[11px] text-gray-500">
              Reserved for AI/ML Specialist. Current papers utilize human-curated and seeded SQLite question pools.
            </p>
          </div>

          {/* RPA Module */}
          <div className="border border-gray-200 rounded-xl p-4 bg-gray-50/50">
            <div className="flex items-center justify-between mb-2">
              <div className="flex items-center space-x-2">
                <Cpu className="w-4 h-4 text-blue-600" />
                <span className="text-xs font-bold text-gray-800">RPA Scraping Pipeline</span>
              </div>
              <span className="px-2 py-0.5 rounded text-[10px] font-semibold bg-gray-200 text-gray-700">
                Unconfigured
              </span>
            </div>
            <p className="text-[11px] text-gray-500">
              Reserved for RPA/Python Specialist. Live syllabus and PYQ web scrapers will integrate directly into the database.
            </p>
          </div>

          {/* Data Analyst Module */}
          <div className="border border-gray-200 rounded-xl p-4 bg-gray-50/50">
            <div className="flex items-center justify-between mb-2">
              <div className="flex items-center space-x-2">
                <PieChart className="w-4 h-4 text-emerald-600" />
                <span className="text-xs font-bold text-gray-800">Advanced Statistical Engine</span>
              </div>
              <span className="px-2 py-0.5 rounded text-[10px] font-semibold bg-blue-100 text-blue-800">
                Awaiting Engine
              </span>
            </div>
            <p className="text-[11px] text-gray-500">
              Reserved for Data Analyst Specialist. Standard score calculation and attempt metrics are fully operational in core backend.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AdminDashboard;

