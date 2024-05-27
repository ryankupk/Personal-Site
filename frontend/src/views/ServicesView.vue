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
    <ServiceItem name="Immich" url="https://immich.ryankupka.dev/" extension="png"/>
    <ServiceItem name="dufs" url="https://dufs.ryankupka.dev/dufs" extension="png"/>
  </div>
</template>

<style scoped>
  .services {
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
  }
</style>
