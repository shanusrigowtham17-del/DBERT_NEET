import apiClient from './client';

export const getExamsApi = async () => {
  const response = await apiClient.get('/api/exams/');
  return response.data;
};

export const getTopicsApi = async (examId) => {
  const response = await apiClient.get(`/api/topics/${examId}`);
  return response.data;
};

export const getPapersByExamApi = async (examId) => {
  const response = await apiClient.get(`/api/papers/${examId}`);
  return response.data;
};

export const getQuestionsByExamApi = async (examId) => {
  const response = await apiClient.get(`/api/questions/${examId}`);
  return response.data;
};

export const getPaperQuestionsApi = async (paperId) => {
  const response = await apiClient.get(`/api/paper-questions/${paperId}`);
  return response.data;
};
