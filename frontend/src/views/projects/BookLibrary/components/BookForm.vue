<script setup>
import { ref, watch } from 'vue';

const props = defineProps(['book']);
const emit = defineEmits(['addBook', 'updateBook']);

const form = ref({
  title: '',
  author: '',
  genre: '',
  pages: null,
  rating: null
});

const resetForm = () => {
  form.value = {
    title: '',
    author: '',
    genre: '',
    pages: null,
    rating: null
  };
};

watch(() => props.book, (newBook) => {
  if (newBook) {
    form.value = { ...newBook };
  } else {
    resetForm();
  }
}, { immediate: true });

const submitForm = () => {
  const bookData = {
    ...form.value,
    pages: form.value.pages ? parseInt(form.value.pages) : null,
    rating: form.value.rating ? parseFloat(form.value.rating) : null
  };
  
  if (props.book) {
    emit('updateBook', bookData);
  } else {
    emit('addBook', bookData);
  }
  resetForm();
};
</script>

<template>
  <div class="book-form">
    <h2>{{ book ? 'Edit Book' : 'Add New Book' }}</h2>
    <form @submit.prevent="submitForm">
      <input v-model="form.title" placeholder="Title" required>
      <input v-model="form.author" placeholder="Author" required>
      <input v-model="form.genre" placeholder="Genre">
      <input v-model="form.pages" type="number" placeholder="Number of pages">
      <input v-model="form.rating" type="number" step="0.1" min="0" max="5" placeholder="Rating (0-5)">
      <button type="submit">{{ book ? 'Update' : 'Add' }} Book</button>
    </form>
  </div>
</template>

<style scoped>
.book-form {
  flex: 1;
  background-color: #2a2a2a;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

h2 {
  font-size: 1.5rem;
  margin-bottom: 20px;
  padding-bottom: 10px;
  border-bottom: 1px solid #444;
}

form {
  display: flex;
  flex-direction: column;
}

input {
  margin-bottom: 15px;
  padding: 10px;
  border: 1px solid #444;
  background-color: #333;
  color: #f0f0f0;
  border-radius: 4px;
}

input::placeholder {
  color: #888;
}

button {
  background-color: #4CAF50;
  color: white;
  border: none;
  padding: 12px;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #45a049;
}
</style>