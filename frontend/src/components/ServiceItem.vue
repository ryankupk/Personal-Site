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
const dimensions = ref('120rem');
</script>

<template>
  <div class="item">
    <a :href="url" target="_blank">
        <h4 class="service-name">{{ name }}</h4>
        <div class="service-icon-container">
            <img class="service-icon" 
            :src="`${name.toLowerCase()}.${extension}`" 
            :alt="name" 
            :width="dimensions" 
            :height="dimensions">
        </div>
    </a>
  </div>
</template>

<style scoped>
.item {
    display: flex;
    margin: 18px;
    flex-direction: column;
    align-items: center;
    min-width: 167px;
}

a, a:visited {
  text-decoration: none;
  color: inherit;
}

h4 {
    display: flex;
    justify-content: center;
}
.service-icon {
    width: 100%;
    object-fit: contain;
}
.service-icon-container {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
}

</style>