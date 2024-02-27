<script>
</script>

<template>
  <!-- adapted from codepen: https://codepen.io/kryo2k/pen/xbxjGP -->
  <div class="container">
    <div v-for="n in 29" :key="n" :class="['ring', 'el-' + n]"></div>
  </div>
</template>

<style lang="scss" scoped>
@import "bourbon";

$box-size: 480px * 4;
$rings: 30;
$duration: 2.5s;
$lagdelay: 1.25;

.container {
  position: fixed; // Use fixed positioning
  width: 100vw; // Viewport width
  height: 100vh; // Viewport height
  display: flex;
  justify-content: center;
  align-items: center;
  top: 50%;
  left: 50%;
  margin-top: calc($box-size / 2 * -1);
  margin-left: calc($box-size / 2 * -1);
  z-index: -1;
  .ring {
    position: absolute;
  }
}

@for $i from 1 through $rings {
  $perc: calc(($rings - $i) / $rings);

  @keyframes el-animate-#{$i} {
    0% {
      border-color: rgb(255 * $perc, 255 * $perc, 255 * $perc);
      transform: rotate(0deg);
    }
    25% {
      border-color: rgb(255 * (1 - $perc), 125 * $perc, 255 * (1 - $perc));
      transform: rotate(45deg);
    }
    75% {
      border-color: rgb(125 * $perc, 255 * (1 - $perc), 255 * $perc);
      transform: rotate(135deg);
    }
    100%{
      border-color: rgb(255 * $perc, 255 * $perc, 255 * $perc);
      transform: rotate(180deg);
    }
  }

  .ring.el-#{$i} {
    $size: $box-size * $perc;

    border: 3px solid black;
    border-color: rgb(255 * $perc, 255 * $perc, 255 * $perc);
    left: calc($box-size / 2) - calc($size / 2);
    top: calc($box-size / 2) - calc($size / 2);
    width: $size;
    height: $size;
    border-radius: ($size * 0.35);

    animation: el-animate-#{$i} $duration linear;
    animation-delay: $lagdelay * ($duration * $perc);
    animation-iteration-count: infinite;
  }
}
</style>
