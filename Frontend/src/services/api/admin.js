import apiClient from './client';

export const getAllQuestionsApi = async (examId = null, topicId = null) => {
  const params = {};
  if (examId) params.exam_id = examId;
  if (topicId) params.topic_id = topicId;
  const response = await apiClient.get('/api/questions/', { params });
  return response.data;
};

export const createQuestionApi = async (questionData) => {
  const response = await apiClient.post('/api/questions/', questionData);
  return response.data;
};

export const createExamApi = async (examData) => {
  const response = await apiClient.post('/api/exams/', examData);
  return response.data;
};

export const getExamBlueprintsApi = async () => {
  const response = await apiClient.get('/api/exam-blueprints/');
  return response.data;
};

export const createBlueprintApi = async (blueprintData) => {
  const response = await apiClient.post('/api/exam-blueprints/', blueprintData);
  return response.data;
};

