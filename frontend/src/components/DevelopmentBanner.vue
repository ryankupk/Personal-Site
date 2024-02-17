<template>
  <span class="development-banner">&#9888; Site is currently under active development, expect changes &#9888;</span>
</template>

<script lang="ts">
export default {
  name: 'DevelopmentBanner',
}
</script>

<style scoped>
.development-banner {
    background-color: #ffecb3; /* Mellow yellow background */
    color: black; /* Black text color */
    padding: 10px 20px; /* Adequate padding for spacing */
    text-align: center; /* Center the text and icon */
    font-weight: bold; /* Make the text stand out */
    border-bottom: 2px solid #ffd700; /* A subtle border to define the banner's bottom edge */
  }
</style>
