<script setup>
import { ref } from 'vue';
defineProps({
    url: {
        type: String,
        required: true
    },
    name: {
        type: String, 
        required: true
    },
    extension: {
        type: String,
        required: true
    }
});
const dimensions = ref('150px');
</script>

<template>
  <div class="item">
    <a :href="url">
        <h1 class="service-name">{{ name }}</h1>
        <img class="service-icon" :src="`${name.toLowerCase()}.${extension}`" :alt="name" :width="dimensions" :height="dimensions">
        <!-- <picture> <source :type="image/`${extension}`" :srcset="`${name.toLowerCase()}.${extension}`"> </picture> -->
    </a>
  </div>
</template>

<style scoped>
a, a:visited {
  text-decoration: none;
  color: inherit;
}

h1 {
    display: flex;
    justify-content: center;
}

.item {
    margin: 18px;
}

</style>