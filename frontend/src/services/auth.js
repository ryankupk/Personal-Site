import axios from 'axios';

const API_URL = '/api';

export const login = async (credentials) => {
  try {
    const response = await axios.post(`${API_URL}/login`, credentials);
    const token = response.data.access_token;
    localStorage.setItem('bookLibraryToken', token);
    return token;
  } catch (error) {
    throw error.response?.data?.detail || 'Login failed. Please try again.';
  }
};

export const register = async (credentials) => {
  try {
    await axios.post(`${API_URL}/register`, credentials);
    return await login(credentials);
  } catch (error) {
    throw error.response?.data?.detail || 'Registration failed. Please try again.';
  }
};

export const logout = () => {
  localStorage.removeItem('bookLibraryToken');
};

export const getToken = () => {
  return localStorage.getItem('bookLibraryToken');
};

export const isAuthenticated = () => {
  return !!getToken();
};