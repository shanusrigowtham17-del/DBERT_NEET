import apiClient from './client';

export const loginApi = async (email, password) => {
  const response = await apiClient.post('/api/auth/login', { email, password });
  return response.data;
};

export const registerApi = async (name, email, password, role = 'student') => {
  const response = await apiClient.post('/api/auth/register', {
    name,
    email,
    password,
    role,
  });
  return response.data;
};

export const getMeApi = async () => {
  const response = await apiClient.get('/api/auth/me');
  return response.data;
};

