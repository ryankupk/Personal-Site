<script setup>
import { QExpansionItem } from 'quasar';

defineProps({
  title: {
    type: String,
    required: true
  },
  description: {
    type: String,
    required: true
  },
  sourceURL: {
    type: String,
    required: true
  },
  routerTo: {
    type: String,
    required: false
  },
})

</script>


<template>

  <div class="container">
    <q-expansion-item :label="title" style="max-width: 100%;">
      <div class="inner-items">
        <div class="source-wrapper">
          <img src="@/assets/github-mark-white.svg" class="gh-logo">
          <a :href="sourceURL" class="blue project-link">View Source</a> <br/>
        </div>
        {{ description }}
        <router-link :to="{ name: `${routerTo}`}" class="blue project-link">view {{ routerTo }}</router-link>
      </div>
    </q-expansion-item>
  </div>
</template>


<style scoped>
.container{
  width: 100%;
  padding: 15px 5px 15px 5px;
  min-width: 420px;
  max-width: 420px;
  /* border-radius: 5%; */
  /* border: 2px solid black; */
}

.inner-items {
  padding-left: 30px;
  padding-right: 30px;
  background-color: #101010;
  max-width: inherit;
}

.source-wrapper {
  display: flex;
  align-items: center;
}
.gh-logo {
  width: 1.4rem;
  margin: 10px
}

.project-link {
  border-radius: 6px;
}

/* .arrow {
  padding: 3px 5px 3px 5px;
  border: 1px solid black;
  float: right;
} */
</style>
