<script setup>
  import ProjectItem from '../components/ProjectItem.vue'
</script>

<template>
  <div class="projects">
    <ProjectItem />
  </div>
</template>

<style>
@media (min-width: 1024px) {
  .projects {
    display: flex;
    align-items: center;
  }
}
</style>
