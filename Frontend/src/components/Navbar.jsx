import React from 'react';
import { Link, useNavigate, useLocation } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { LogOut, BookOpen, User, ShieldCheck, HelpCircle, BarChart3, LayoutDashboard } from 'lucide-react';

const Navbar = () => {
  const { user, isAuthenticated, logout } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  const isAdmin = user?.role === 'admin';

  return (
    <header className="bg-white border-b border-gray-200 sticky top-0 z-30 shadow-sm">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
        <div className="flex items-center space-x-6">
          <Link to={isAdmin ? '/admin' : '/dashboard'} className="flex items-center space-x-2">
            <div className="bg-indigo-600 text-white p-2 rounded-lg">
              <BookOpen className="w-5 h-5" />
            </div>
            <div>
              <span className="font-bold text-lg text-gray-900 tracking-tight">Gyatri AI</span>
              <span className="text-xs text-indigo-600 block -mt-1 font-semibold uppercase">Exam Portal</span>
            </div>
          </Link>

          {/* Admin Navigation Tabs */}
          {isAuthenticated && isAdmin && (
            <nav className="hidden md:flex items-center space-x-1 pl-4 border-l border-gray-200 text-xs font-bold">
              <Link
                to="/admin"
                className={`flex items-center space-x-1.5 px-3 py-1.5 rounded-lg transition-colors ${
                  location.pathname === '/admin'
                    ? 'bg-indigo-50 text-indigo-700'
                    : 'text-gray-600 hover:text-gray-900 hover:bg-gray-50'
                }`}
              >
                <LayoutDashboard className="w-3.5 h-3.5" />
                <span>Console</span>
              </Link>
              <Link
                to="/admin/questions"
                className={`flex items-center space-x-1.5 px-3 py-1.5 rounded-lg transition-colors ${
                  location.pathname === '/admin/questions'
                    ? 'bg-indigo-50 text-indigo-700'
                    : 'text-gray-600 hover:text-gray-900 hover:bg-gray-50'
                }`}
              >
                <HelpCircle className="w-3.5 h-3.5" />
                <span>Questions</span>
              </Link>
              <Link
                to="/admin/reports"
                className={`flex items-center space-x-1.5 px-3 py-1.5 rounded-lg transition-colors ${
                  location.pathname === '/admin/reports'
                    ? 'bg-indigo-50 text-indigo-700'
                    : 'text-gray-600 hover:text-gray-900 hover:bg-gray-50'
                }`}
              >
                <BarChart3 className="w-3.5 h-3.5" />
                <span>Reports</span>
              </Link>
              <Link
                to="/dashboard"
                className={`flex items-center space-x-1.5 px-3 py-1.5 rounded-lg transition-colors ${
                  location.pathname === '/dashboard'
                    ? 'bg-indigo-50 text-indigo-700'
                    : 'text-gray-500 hover:text-gray-800 hover:bg-gray-50'
                }`}
              >
                <span>Student View</span>
              </Link>
            </nav>
          )}
        </div>

        <div className="flex items-center space-x-4">
          {isAuthenticated && user ? (
            <>
              <div className="hidden sm:flex items-center space-x-2 text-sm text-gray-700 bg-gray-50 px-3 py-1.5 rounded-full border border-gray-200">
                {isAdmin ? (
                  <ShieldCheck className="w-4 h-4 text-purple-600" />
                ) : (
                  <User className="w-4 h-4 text-indigo-600" />
                )}
                <span className="font-medium text-xs">{user.name}</span>
                <span
                  className={`text-[10px] uppercase font-bold px-2 py-0.5 rounded-full ${
                    isAdmin
                      ? 'bg-purple-100 text-purple-800 border border-purple-200'
                      : 'bg-indigo-100 text-indigo-800'
                  }`}
                >
                  {user.role}
                </span>
              </div>
              <button
                onClick={handleLogout}
                className="flex items-center space-x-1.5 text-xs font-medium text-gray-600 hover:text-red-600 hover:bg-red-50 px-3 py-1.5 rounded-lg transition-colors duration-150 border border-transparent hover:border-red-200"
                title="Log out"
              >
                <LogOut className="w-3.5 h-3.5" />
                <span>Logout</span>
              </button>
            </>
          ) : (
            <div className="flex items-center space-x-3 text-xs font-semibold">
              <Link
                to="/login"
                className="text-gray-600 hover:text-indigo-600 px-3 py-1.5 rounded-lg transition-colors"
              >
                Sign In
              </Link>
              <Link
                to="/register"
                className="bg-indigo-600 hover:bg-indigo-700 text-white px-4 py-1.5 rounded-lg transition-colors shadow-sm"
              >
                Register
              </Link>
            </div>
          )}
        </div>
      </div>
    </header>
  );
};

export default Navbar;
