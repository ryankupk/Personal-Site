<script setup>
import { defineProps, defineEmits, ref } from 'vue';

const props = defineProps(['books']);
const emit = defineEmits(['selectBook', 'deleteBook', 'reorderBooks']);

const selectBook = (book) => {
  emit('selectBook', book);
};

const deleteBook = (bookId) => {
  emit('deleteBook', bookId);
};

const draggedItem = ref(null);

const dragStart = (event, index) => {
  draggedItem.value = index;
  event.dataTransfer.setData('text/plain', index);
  event.target.classList.add('dragging');
};

const dragEnd = (event) => {
  draggedItem.value = null;
  event.target.classList.remove('dragging');
};

const dragOver = (event) => {
  event.preventDefault();
};

const drop = (event, targetIndex) => {
  event.preventDefault();
  const sourceIndex = parseInt(event.dataTransfer.getData('text/plain'));
  if (sourceIndex !== targetIndex) {
    emit('reorderBooks', { sourceIndex, targetIndex });
  }
  event.target.classList.remove('drag-over');
};

const dragEnter = (event) => {
  if (event.target.classList.contains('book-item')) {
    event.target.classList.add('drag-over');
  }
};

const dragLeave = (event) => {
  if (event.target.classList.contains('book-item')) {
    event.target.classList.remove('drag-over');
  }
};
</script>

<template>
  <div class="book-list">
    <h2>Your Books</h2>
    <ul>
      <li
        v-for="(book, index) in books"
        :key="book.id"
        class="book-item"
        :class="{ 'dragging': draggedItem === index }"
        @click="selectBook(book)"
        draggable="true"
        @dragstart="dragStart($event, index)"
        @dragend="dragEnd"
        @dragover="dragOver"
        @dragenter="dragEnter"
        @dragleave="dragLeave"
        @drop="drop($event, index)"
      >
        <div class="drag-handle">☰</div>
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
  user-select: none; /* Prevent text selection during drag */
}

li:hover {
  background-color: #3a3a3a;
  opacity: 0.8; /* Indicate draggable items */
}

li:active {
  opacity: 0.6; /* Visual feedback when dragging */
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

.book-item {
  cursor: move;
  padding: 18px;
  font-size: 1.1rem;
  border: 1px solid #444;
  border-radius: 5px;
  margin-bottom: 12px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: all 0.3s ease;
  user-select: none;
  background-color: #2a2a2a;
}

.book-item:hover {
  background-color: #3a3a3a;
}

.book-item.dragging {
  opacity: 0.5;
  background-color: #4a4a4a;
}

.book-item.drag-over {
  border: 2px dashed #666;
  background-color: #3a3a3a;
}

.drag-handle {
  cursor: move;
  padding: 0 10px;
  color: #666;
  font-size: 1.2rem;
}

.book-info {
  flex-grow: 1;
  margin-left: 10px;
  margin-right: 20px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}
</style>