<script setup>
import { defineProps, defineEmits } from 'vue';

const props = defineProps(['books']);
const emit = defineEmits(['selectBook', 'deleteBook']);

const selectBook = (book) => {
  emit('selectBook', book);
};

const deleteBook = (bookId) => {
  emit('deleteBook', bookId);
};
</script>

<template>
  <div class="book-list">
    <h2>Your Books</h2>
    <ul>
      <li v-for="book in books" :key="book.id" @click="selectBook(book)">
        <div class="book-info">
          <span class="book-title">{{ book.title }}</span>
          <span class="book-author">by {{ book.author }}</span>
        </div>
        <button @click.stop="deleteBook(book.id)">Delete</button>
      </li>
    </ul>
  </div>
</template>

<style scoped>
.book-list {
  flex: 1;
  background-color: #2a2a2a;
  padding: 30px;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  width: 100%; /* Ensure full width */
}

h2 {
  font-size: 1.8rem;
  margin-bottom: 25px;
  padding-bottom: 15px;
  border-bottom: 1px solid #444;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  cursor: pointer;
  padding: 18px;
  font-size: 1.1rem;
  border: 1px solid #444;
  border-radius: 5px;
  margin-bottom: 12px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: background-color 0.3s ease;
}

li:hover {
  background-color: #3a3a3a;
}

.book-info {
  flex-grow: 1;
  margin-right: 20px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.book-title {
  font-weight: bold;
  margin-bottom: 5px;
  word-wrap: break-word;
  overflow-wrap: break-word;
}

.book-author {
  font-size: 0.9em;
  color: #aaa;
}

button {
  background-color: #c53030;
  color: white;
  border: none;
  padding: 10px 14px;
  font-size: 1rem;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  flex-shrink: 0;
}

button:hover {
  background-color: #9b2c2c;
}
</style>