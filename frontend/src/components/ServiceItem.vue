<script setup>
defineProps({
    url: {
        type: String,
        required: true
    },
    name: {
        type: String, 
        required: true
    }
})
</script>

<template>
  <div class="item">
    <a href="{{ url }}">
        <h1 class="service-name">{{ name }}</h1>
        <img href="" class="service-icon"></img>
    </a>
  </div>
</template>