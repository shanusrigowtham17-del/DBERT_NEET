import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './context/AuthContext';
import Navbar from './components/Navbar';
import ProtectedRoute from './components/ProtectedRoute';

import Login from './pages/Login';
import Register from './pages/Register';
import StudentDashboard from './pages/StudentDashboard';
import ExamInstructions from './pages/ExamInstructions';
import ExamTaking from './pages/ExamTaking';
import ExamResult from './pages/ExamResult';
import AdminDashboard from './pages/AdminDashboard';
import AdminQuestionBank from './pages/AdminQuestionBank';
import AdminReports from './pages/AdminReports';

const AppRoutes = () => {
  const { isAuthenticated, loading, user } = useAuth();

  return (
    <div className="min-h-screen flex flex-col bg-gray-50 text-gray-900">
      <Navbar />
      <main className="flex-1">
        <Routes>
          {/* Public Routes */}
          <Route
            path="/login"
            element={!loading && isAuthenticated ? (
              <Navigate to={user?.role === 'admin' ? "/admin" : "/dashboard"} replace />
            ) : <Login />}
          />
          <Route
            path="/register"
            element={!loading && isAuthenticated ? (
              <Navigate to={user?.role === 'admin' ? "/admin" : "/dashboard"} replace />
            ) : <Register />}
          />

          {/* Student Protected Routes */}
          <Route
            path="/dashboard"
            element={
              <ProtectedRoute>
                <StudentDashboard />
              </ProtectedRoute>
            }
          />
          <Route
            path="/exam/:examId/instructions"
            element={
              <ProtectedRoute>
                <ExamInstructions />
              </ProtectedRoute>
            }
          />
          <Route
            path="/exam/:attemptId"
            element={
              <ProtectedRoute>
                <ExamTaking />
              </ProtectedRoute>
            }
          />
          <Route
            path="/result/:attemptId"
            element={
              <ProtectedRoute>
                <ExamResult />
              </ProtectedRoute>
            }
          />

          {/* Admin Protected Routes */}
          <Route
            path="/admin"
            element={
              <ProtectedRoute requiredRole="admin">
                <AdminDashboard />
              </ProtectedRoute>
            }
          />
          <Route
            path="/admin/questions"
            element={
              <ProtectedRoute requiredRole="admin">
                <AdminQuestionBank />
              </ProtectedRoute>
            }
          />
          <Route
            path="/admin/reports"
            element={
              <ProtectedRoute requiredRole="admin">
                <AdminReports />
              </ProtectedRoute>
            }
          />

          {/* Root Redirect */}
          <Route
            path="/"
            element={
              <Navigate to={isAuthenticated && user?.role === 'admin' ? "/admin" : "/dashboard"} replace />
            }
          />

          {/* 404 Fallback */}
          <Route
            path="*"
            element={
              <Navigate to={isAuthenticated && user?.role === 'admin' ? "/admin" : "/dashboard"} replace />
            }
          />
        </Routes>
      </main>
    </div>
  );
};

function App() {
  return (
    <BrowserRouter>
      <AuthProvider>
        <AppRoutes />
      </AuthProvider>
    </BrowserRouter>
  );
}

export default App;
