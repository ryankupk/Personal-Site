<script setup>

import {ref, defineProps} from 'vue';

const props = defineProps({
  bannerText: {
    type: String,
    required: true
  },
  bgColor: {
    type: String,
    required: false 
  },
  borderColor: {
    type: String,
    required: false
  },
})

</script>

<template>
  <span class="banner" 
  :style="{
      backgroundColor: bgColor,
      borderColor: borderColor,
      borderStyle: borderColor ? 'solid' : '', // Apply border style only if borderColor is provided
    }"
  >
  {{bannerText}}
  </span>
</template>


<style scoped>
  .banner {

    width: 100%; /* Ensures the banner stretches across the viewport */
    /* max-width: 500px; */
    margin: 0 auto;
    text-align: center;
    position: sticky;
    top: 20;
    left: 0;
    z-index: 1000;
    color: black; /* Black text color */
    padding: 10px 20px; /* Adds padding for some spacing */
    box-sizing: border-box; /* Ensures padding does not affect the overall width */
    text-align: center; /* Centers the text */
    font-weight: bold; /* Make the text stand out */
  }
</style>
