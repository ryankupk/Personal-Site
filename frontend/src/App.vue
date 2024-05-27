<script setup>
import { RouterLink, RouterView } from 'vue-router' 
import Banner from './components/Banner.vue'; 


import { onMounted, ref } from 'vue';

const bannerHeight = ref(0);

onMounted(() => {
  const bannerElement = document.querySelector('.banner');
  if (bannerElement) {
    bannerHeight.value = bannerElement.offsetHeight + 'px';
  }
});

</script>

<template>
  <!-- <Banner 
  class="banner" 
  banner-text="&#9888; Site is currently under active development, expect improvements &#9888;"
  bg-color="#ffecb3"
  border-color="#ffd700"
  /> -->
  <header>

    <div class="router-wrapper">
      <nav>
        <RouterLink class="blue" to="/">Home</RouterLink>
        <RouterLink class="blue" to="/about">About</RouterLink>
        <RouterLink class="blue" to="/projects">Projects</RouterLink>
        <RouterLink class="blue" to="/services">Services</RouterLink>
        <RouterLink class="blue" to="/contact">Contact</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>


<style scoped>
.banner {
  position: fixed; 
  left: 50%;
  transform: translateX(-50%);
  width: auto;
}

header {
  width: 100%; /* Ensure header spans the full width */
}

.router-wrapper {
  width: 100%; 
  display: flex;
  justify-content: center; /* Horizontally center the content within the router-wrapper */
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
  .router-wrapper {
    justify-content: center; /* Keep content centered */
  }

  nav {
    justify-content: center;
    font-size: 1rem; /* Adjust font size as necessary */
  }
}
@media (max-width: 500px) {
  nav a {
    padding: 0 0.53rem;
    font-size: 0.87rem;
  }
}
</style>
