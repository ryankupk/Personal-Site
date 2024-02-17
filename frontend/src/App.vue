<script setup>
import { RouterLink, RouterView } from 'vue-router'
import DevelopmentBanner from './components/DevelopmentBanner.vue'; // Adjust the path as necessary
</script>

<template>
  <DevelopmentBanner />
  <header>

    <div class="wrapper">
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
        <RouterLink to="/projects">Projects</RouterLink>
        <RouterLink to="/services">Services</RouterLink>
        <RouterLink to="/contact">Contact</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<!-- <script lang="js">
import DevelopmentBanner from '@/components/DevelopmentBanner.vue'; // Adjust the path as necessary

export default {
  name: 'App',
  components: {
    DevelopmentBanner
  }
}
</script> -->

<style scoped>
header {
  width: 100%; /* Ensure header spans the full width */
}

.wrapper {
  width: 100%; /* Ensure wrapper spans the full width */
  display: flex;
  justify-content: center; /* Horizontally center the content within the wrapper */
}

nav {
  display: flex;
  justify-content: center; /* Center items horizontally */
  flex-wrap: wrap; /* Allow items to wrap if needed */
  margin-top: 2rem; /* Adjust as needed to position at the top */
}

nav a {
  display: inline-block; /* Display links inline */
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
  text-decoration: none; /* Optional: Removes underline from links */
}

nav a:first-of-type {
  border-left: 0; /* Remove border for the first link */
}

@media (min-width: 1024px) {
  .wrapper {
    justify-content: center; /* Keep content centered */
  }

  nav {
    justify-content: center;
    font-size: 1rem; /* Adjust font size as necessary */
  }
}
</style>
