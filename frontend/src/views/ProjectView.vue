<script setup>
// import Banner from '@/components/Banner.vue';
import ProjectItem from '@/components/ProjectItem.vue'
import BaseProjectView from '@/views/projects/BaseProjectView.vue';
</script>

<template>
  <div class="projects">
    <ProjectItem 
      title="This Site!"
      description="This site is hand-written by myself. For the moment it's closed source, but will be opened up soon."
      sourceURL="https://github.com/ryankupk/Personal-Site"
      routerTo="home"
    />
    <ProjectItem 
      title="Wordle Helper"
      description="Wordle Helper"
      sourceURL="https://github.com/ryankupk/wordle-hacks"
      routerTo="wordle"
    />
    <!-- <ProjectItem 
      title="Knight's Tour"
      description="Knight's Tour"
      sourceURL="https://github.com/ryankupk/ai-knights-tour"
      routerTo="knightsTour"
    /> -->
  </div>
</template>

<style>
@media (min-width: 1024px) {
  .projects {
    display: flex;
    flex-direction: column;
    flex-wrap: nowrap;
    align-items: center;
    margin-top: 30px;
  }
}
</style>
