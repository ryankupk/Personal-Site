<script setup>
import { computed } from 'vue';

const props = defineProps(['books']);

const totalBooks = computed(() => props.books.length);
const averageRating = computed(() => {
  const totalRating = props.books.reduce((sum, book) => sum + (book.rating || 0), 0);
  return totalRating / totalBooks.value || 0;
});
const mostReadGenre = computed(() => {
  const genreCounts = props.books.reduce((counts, book) => {
    counts[book.genre] = (counts[book.genre] || 0) + 1;
    return counts;
  }, {});
  const genres = Object.entries(genreCounts);
  return genres.length > 0
    ? genres.reduce((a, b) => a[1] > b[1] ? a : b)[0]
    : 'No genres';
});
</script>

<template>
  <div class="book-stats">
    <h2>Library Stats</h2>
    <p>Total Books: {{ totalBooks }}</p>
    <p>Average Rating: {{ averageRating.toFixed(1) }}</p>
    <p>Most Read Genre: {{ mostReadGenre }}</p>
  </div>
</template>

<style scoped>
.book-stats {
  flex: 1;
  background-color: #2a2a2a;
  padding: 30px;  /* Increased from 25px */
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

h2 {
  font-size: 1.8rem;  /* Increased from 1.5rem */
  margin-bottom: 25px;  /* Increased from 20px */
  padding-bottom: 15px;  /* Increased from 10px */
  border-bottom: 1px solid #444;
}

p {
  margin-bottom: 12px;  /* Increased from 10px */
  font-size: 1.1rem;  /* Increased from 16px */
}
</style>