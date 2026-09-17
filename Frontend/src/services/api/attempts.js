import apiClient from './client';

export const buildPaperApi = async (examId, questionCount, title = null) => {
  const payload = {
    exam_id: examId,
    question_count: questionCount,
  };
  if (title) payload.title = title;
  const response = await apiClient.post('/api/papers/build', payload);
  return response.data;
};

export const startAttemptApi = async (paperId) => {
  const response = await apiClient.post('/api/attempts/', { paper_id: paperId });
  return response.data;
};

export const getAttemptApi = async (attemptId) => {
  const response = await apiClient.get(`/api/attempts/${attemptId}`);
  return response.data;
};

export const getAttemptAnswersApi = async (attemptId) => {
  const response = await apiClient.get(`/api/attempt-answers/${attemptId}`);
  return response.data;
};

export const saveAnswerApi = async (attemptId, questionId, selectedOption) => {
  const response = await apiClient.post('/api/attempt-answers/', {
    attempt_id: attemptId,
    question_id: questionId,
    selected_option: selectedOption,
  });
  return response.data;
};

export const submitAttemptApi = async (attemptId) => {
  const response = await apiClient.post(`/api/attempts/${attemptId}/submit`);
  return response.data;
};

export const getResultApi = async (attemptId) => {
  const response = await apiClient.get(`/api/results/${attemptId}`);
  return response.data;
};

