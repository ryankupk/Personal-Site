<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import BaseProjectView from '@/views/projects/BaseProjectView.vue';
import BookList from './components/BookList.vue';
import BookForm from './components/BookForm.vue';
import BookStats from './components/BookStats.vue';
import LoginForm from './components/LoginForm.vue';

const books = ref([]);
const selectedBook = ref(null);
const isAuthenticated = ref(false);
const token = ref('');
const loginError = ref('');

const login = async (credentials) => {
  try {
    const response = await axios.post('/api/login', credentials);
    token.value = response.data.access_token;
    localStorage.setItem('bookLibraryToken', token.value);
    isAuthenticated.value = true;
    loginError.value = '';
    await fetchBooks();
  } catch (error) {
    console.error('Login failed:', error);
    loginError.value = error.response?.data?.detail || 'Login failed. Please try again.';
  }
};

const register = async (credentials) => {
  try {
    await axios.post('/api/register', credentials);
    await login(credentials);
  } catch (error) {
    console.error('Registration failed:', error);
    loginError.value = error.response?.data?.detail || 'Registration failed. Please try again.';
  }
};

const logout = () => {
  token.value = '';
  localStorage.removeItem('bookLibraryToken');
  isAuthenticated.value = false;
  books.value = [];
  selectedBook.value = null;
};

const fetchBooks = async () => {
  try {
    const response = await axios.get('/api/books', {
      headers: { 'Authorization': `Bearer ${token.value}` }
    });
    books.value = response.data;
  } catch (error) {
    console.error('Error fetching books:', error);
  }
};

const addBook = async (book) => {
  try {
    const response = await axios.post('/api/books', book, {
      headers: { 'Authorization': `Bearer ${token.value}` }
    });
    books.value.push(response.data);
  } catch (error) {
    console.error('Error adding book:', error);
    if (error.response) {
      console.error('Response data:', error.response.data);
    }
  }
};

const updateBook = async (book) => {
  try {
    const response = await axios.put(`/api/books/${book.id}`, book, {
      headers: { 'Authorization': `Bearer ${token.value}` }
    });
    const index = books.value.findIndex(b => b.id === book.id);
    if (index !== -1) {
      books.value[index] = response.data;
    }
    selectedBook.value = null;
  } catch (error) {
    console.error('Error updating book:', error);
    if (error.response) {
      console.error('Response data:', error.response.data);
    }
  }
};

const deleteBook = async (bookId) => {
  try {
    await axios.delete(`/api/books/${bookId}`, {
      headers: { 'Authorization': `Bearer ${token.value}` }
    });
    books.value = books.value.filter(b => b.id !== bookId);
    selectedBook.value = null;
  } catch (error) {
    console.error('Error deleting book:', error);
  }
};

onMounted(() => {
  const savedToken = localStorage.getItem('bookLibraryToken');
  if (savedToken) {
    token.value = savedToken;
    isAuthenticated.value = true;
    fetchBooks();
  }
});
</script>

<template>
  <BaseProjectView>
    <div class="book-library">
      <h1>Personal Book Library</h1>
      <div v-if="!isAuthenticated">
        <LoginForm @login="login" @register="register" />
        <p v-if="loginError" class="error-message">{{ loginError }}</p>
      </div>
      <div v-else>
        <div class="library-header">
          <h2>Welcome to your library</h2>
          <button @click="logout" class="logout-button">Logout</button>
        </div>
        <div class="library-content">
          <BookList 
            :books="books" 
            @select-book="selectedBook = $event"
            @delete-book="deleteBook"
          />
          <BookForm 
            :book="selectedBook" 
            @add-book="addBook" 
            @update-book="updateBook"
          />
          <BookStats :books="books" />
        </div>
      </div>
    </div>
  </BaseProjectView>
</template>

<style scoped>
.book-library {
  max-width: 1400px;
  margin: 0 auto;
  padding: 20px;
  color: #f0f0f0;
}

h1 {
  text-align: center;
  margin-bottom: 40px;
  font-size: 3rem;
}

.library-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
  padding: 0 20px;
}

.library-content {
  display: flex;
  justify-content: space-between;
  gap: 30px;
}

.logout-button {
  background-color: #c53030;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.logout-button:hover {
  background-color: #9b2c2c;
}

.error-message {
  color: #c53030;
  text-align: center;
  margin-top: 10px;
}

@media (max-width: 1200px) {
  .library-content {
    flex-wrap: wrap;
  }

  .library-content > * {
    flex-basis: calc(50% - 15px);
  }
}

@media (max-width: 768px) {
  .library-content {
    flex-direction: column;
  }
  
  .library-content > * {
    flex-basis: 100%;
  }
}
</style>