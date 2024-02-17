<template>
  <div class="gradient-edge" :class="{ 'left': isLeft, right: !isLeft}"></div>
</template>

<script>
export default {
  name: 'GradientEdge',
  props: {
    position: {
      type: String,
      required: true,
      validator: value => ['left', 'right'].includes(value)
    }
  },
  computed: {
    isLeft() {
      return this.position === 'left';
    } 
  }
};
</script>

<style scoped lang="scss">
@keyframes colorCycle {

  0%, 100% {
    background: linear-gradient(to left, rgba(255, 255, 255, 0), rgba(255, 200, 200, 0.8));
  }
  25% {
    background: linear-gradient(to left, rgba(255, 255, 255, 0), rgba(200, 255, 200, 0.8));
  }
  50% {
    background: linear-gradient(to left, rgba(255, 255, 255, 0), rgba(200, 200, 255, 0.8));
  }
  75% {
    background: linear-gradient(to left, rgba(255, 255, 255, 0), rgba(255, 255, 200, 0.8));
  }

  // Keyframes for color cycling
  // Add your color animation steps here
}

.gradient-edge {
  position: fixed;
  top: 0;
  width: 100px; // Adjust as needed
  height: 100vh;
  animation: colorCycle 10s infinite linear;
}

.left {
  left: 0;
  background: linear-gradient(to right, rgba(255, 255, 255, 0) 0%, rgba(255, 255, 255, 0.8) 100%);
//   transform: rotate(180deg);
}
.right {
  right: 0;
  background: linear-gradient(to left, rgba(255, 255, 255, 0) 0%, rgba(255, 255, 255, 0.8) 100%);
  transform: rotate(180deg);
}

</style>
