<script setup>
// import Banner from '@/components/Banner.vue';
import ProjectItem from '@/components/ProjectItem.vue'
</script>

<template>
  <div class="projects">
    <ProjectItem 
      title="This Site!"
      description="This site is hand-written by myself. It's a Vue SPA frontend served by nginx and a Python FastAPI backend."
      sourceURL="https://github.com/ryankupk/Personal-Site"
      routerTo="home"
    />
    <ProjectItem 
      title="Wordle Helper"
      description="Utility to help solve Wordle. Enter guesses and select whether the letter is not in the word at all (gray), in the word in the wrong place (yellow), or in the word and in the correct place (green). The list of possible words will be displayed as a suggestion for what the word may be."
      sourceURL="https://github.com/ryankupk/wordle-hacks"
      routerTo="wordle"
    />
    <ProjectItem 
      title="Personal Book Library"
      description="A full CRUD application to manage your personal book collection. Add, edit, delete books, and view interesting statistics about your reading habits."
      sourceURL="https://github.com/ryankupk/Personal-Site/tree/main/frontend/src/views/projects/BookLibrary"
      routerTo="bookLibrary"
    />
    <ProjectItem 
      title="Knight's Tour"
      description="A knight's tour is a sequence of moves of a knight on a chessboard such that the knight visits every square exactly once"
      sourceURL="https://github.com/ryankupk/ai-knights-tour"
      externalLink="/projects/KnightsTour"
    />
    <ProjectItem 
      title="Ray Tracing"
      description="Visualization of light ray tracing for light sources simulated with various lenses and mirrors"
      sourceURL="https://github.com/ryankupk/Ray-Tracing"
      externalLink="/projects/RayTracing"
    />
  </div>
</template>

<style>
@media (min-width: 1024px) {
}
.projects {
  display: flex;
  flex-direction: column;
  flex-wrap: nowrap;
  align-items: center;
  margin-top: 30px;
}
</style>
