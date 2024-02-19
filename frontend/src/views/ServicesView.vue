<script setup>
import ServiceItem from '../components/ServiceItem.vue'
</script>

<template>
  <div class="services">
    <!-- <h2>Public</h2> -->
    <ServiceItem name="Ollama" url="https://ollama.ryankupka.dev/" extension="png"/>
    <ServiceItem name="Jellyfin" url="https://jelly.ryankupka.dev/" extension="png"/>
    <ServiceItem name="Navidrome" url="https://navi.ryankupka.dev/" extension="png"/>
    <ServiceItem name="Jellyseerr" url="https://reqs.ryankupka.dev/" extension="webp"/>
  </div>
</template>

<style scoped>
@media (min-width: 1024px) {
  .services {
    display: flex;
    flex-wrap: wrap;
    /* align-items: center; */
    justify-content: center;
  }
}
</style>
