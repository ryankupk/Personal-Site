<script setup>

import { ref, onMounted, onUnmounted } from 'vue';

defineProps({
    attributes: {
        type: Array,
        required: true
    }
})

const directions = ['rotate-face-up', 'rotate-face-down', /* other directions */];
const currentAnimation = ref('rotate-face-up');

function changeAnimation() {
  const randomIndex = Math.floor(Math.random() * directions.length);
  currentAnimation.value = directions[randomIndex];
  console.log(currentAnimation.value)
}

onMounted(() => {
  const intervalId = setInterval(() => {
    changeAnimation();
  }, 2000);

  // Cleanup on unmount to avoid memory leaks
  onUnmounted(() => {
    clearInterval(intervalId);
  });
});




// import { ref, onMounted, onUnmounted } from 'vue';

// defineProps({
//     attributes: {
//         type: Array,
//         required: true
//     }
// })

// const isAnimating = ref(false);

// const generateRandomValue = () => {
//     return Math.random() < 0.5 ? -1 : 1;
// };

// const rotateCube = () => {
//     isAnimating.value = true;

//     setTimeout(() => {
//         isAnimating.value = false;
//     }, 1999);

//     const direction = generateRandomValue();

// };

// onMounted(() => {

//     const intervalId = setInterval(rotateCube, 2000);

//     onUnmounted(() => {
//         clearInterval(intervalId);
//     });

// });

</script>

<template>
  <div class="container">
    <div :class="['cube', currentAnimation]" @animationend="changeAnimation">
        <div class="side  front">1</div>
        <div class="side   back">6</div>
        <div class="side  right">4</div>
        <div class="side   left">3</div>
        <div class="side    top">5</div>
        <div class="side bottom">2</div>
    </div>
  </div>
</template>


<style lang='scss' scoped>
$width: 320px;
$height: 160px;
$depth: 160px;

.animate {
    animation: rotate-face infinite 2s;
}

.cube {
    font-size: 80px;
    width: $width; 
    height: $height;
    margin: 80px auto;

    transform-style: preserve-3d;
}

.side {
    position: absolute;

    width: $width; 
    height: $height;

    background: rgba(cyan, .6);
    border: 1px solid rgba(0,0,0,0.5);

    color: white;
    text-align: center;
    line-height: $height;
}

.front {
transform: rotateX(0deg) translateZ(calc($depth / 2));
}
.top   {
transform: rotateX(90deg) translateZ(calc($depth / 2));
}
.right {
transform: rotateY(90deg) translateZ(calc($depth / 2));
}
.left  {
transform: rotateY(-90deg) translateZ(calc($depth / 2));
}
.bottom{
transform: rotateX(-90deg) translateZ(calc($depth / 2));
}
.back  {
transform: rotateY(-180deg) translateZ(calc($depth / 2));
}

@keyframes rotate-face-up {
    0% {
        transform: rotateX( 90deg);
        // transform: rotateX(calc(spin-count * 90) deg);
    }
    100% {
        // transform: rotate();
    }
}
@keyframes rotate-face-down {
    0% {
        transform: rotateX(-90deg);
        // transform: rotateX(calc(spin-count * 90) deg);
    }
    100% {
        // transform: rotate();
    }
}
@keyframes spin {
    0% {
        transform: rotateX(360deg);
        // transform: rotateX(calc(spin-count * 90) deg);
    }
    100% {
        transform: rotate();
    }
}

@keyframes el-animate {
    0% {
        transform: rotateX(0deg);
    }
    25% {
        transform: rotateX(90deg);
    }
    50% {
        transform: rotateX(180deg);
    }
    75% {
        transform: rotateX(270deg);
    }
    100% {
        transform: rotateX(360deg);
    }
}

</style>
