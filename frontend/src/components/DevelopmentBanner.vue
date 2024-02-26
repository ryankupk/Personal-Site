<script setup>

</script>


<template>
  <span class="development-banner">&#9888; Site is currently under active development, expect changes &#9888;</span>
</template>


<style scoped>
  .development-banner {

    width: 100%; /* Ensures the banner stretches across the viewport */
    /* max-width: 500px; */
    margin: 0 auto;
    text-align: center;
    position: sticky;
    top: 20;
    left: 0;
    z-index: 1000;
    background-color: #ffecb3; /* Mellow yellow background */
    color: black; /* Black text color */
    padding: 10px 20px; /* Adds padding for some spacing */
    box-sizing: border-box; /* Ensures padding does not affect the overall width */
    text-align: center; /* Centers the text */
    font-weight: bold; /* Make the text stand out */
    border-bottom: 4px solid #ffd700; /* A subtle border to define the banner's bottom edge */
  }
</style>
