<template>
  <!-- adapted from https://codepen.io/eight/pen/LrabbE -->
  <div class="triangle">
    <div class="square" v-for="i in 120" :key="i" :style="squareStyle(i)"></div>
  </div>
</template>

<script setup>

const squareStyle = (i) => {
  let left, top, right, animationDelay, filter;
  const baseDelay = -0.3;
  const animationDuration = '20s';
  const animationTimingFunction = 'linear';
  const rotateAnimationName = 'rotate';

  if (i <= 40) {
    left = `${(i * 6) - 142}px`;
    top = '100px';
  } else if (i <= 80) {
    left = `${(i * -3) + 220}px`;
    top = `${(i * -5) + 305}px`;
  } else {
    right = `${(i * 3) - 260}px`;
    top = `${(i * 5) - 500}px`;
  }

  animationDelay = `${baseDelay * i}s`;
  filter = `hue-rotate(${3 * i}deg)`;

  return {
    position: 'absolute',
    top,
    left,
    right,
    width: '38px',
    height: '38px',
    border: '1px solid #fa0',
    animation: `${rotateAnimationName} ${animationDuration} ${animationTimingFunction} infinite`,
    animationDelay,
    filter,
  };
};
</script>

<style scoped>
/* @keyframes rotate {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
} */

body {
  background: #2a2a2a;
}

.triangle {
  position: absolute;
  top: 50%;
  left: 50%;
  /* transform: translate(-20px, -20px); */
}
</style>
