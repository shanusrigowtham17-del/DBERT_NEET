import React, { createContext, useState, useEffect, useContext } from 'react';
import { loginApi, registerApi, getMeApi } from '../services/api/auth';

const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
  const [token, setToken] = useState(() => localStorage.getItem('access_token') || null);
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  // Initialize and verify user from stored token on mount
  useEffect(() => {
    let isMounted = true;

    const loadUser = async () => {
      const storedToken = localStorage.getItem('access_token');
      if (!storedToken) {
        if (isMounted) {
          setUser(null);
          setLoading(false);
        }
        return;
      }

      try {
        const userData = await getMeApi();
        if (isMounted) {
          setUser(userData);
          setToken(storedToken);
        }
      } catch (err) {
        console.error('Failed to authenticate with stored token', err);
        localStorage.removeItem('access_token');
        if (isMounted) {
          setUser(null);
          setToken(null);
        }
      } finally {
        if (isMounted) {
          setLoading(false);
        }
      }
    };

    loadUser();

    return () => {
      isMounted = false;
    };
  }, []);

  const login = async (email, password) => {
    const data = await loginApi(email, password);
    const accessToken = data.access_token;
    localStorage.setItem('access_token', accessToken);
    setToken(accessToken);

    // Fetch user details immediately
    const userData = await getMeApi();
    setUser(userData);
    return userData;
  };

  const register = async (name, email, password, role = 'student') => {
    return await registerApi(name, email, password, role);
  };

  const logout = () => {
    localStorage.removeItem('access_token');
    setToken(null);
    setUser(null);
  };

  const value = {
    token,
    user,
    loading,
    isAuthenticated: !!token && !!user,
    login,
    register,
    logout,
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};

export default AuthContext;

