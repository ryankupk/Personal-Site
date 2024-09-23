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
  externalLink: {
    type: String,
    required: false
  },
})

</script>


<template>

  <div class="container">
    <q-expansion-item :label="title" style="max-width: 100%;">
      <div class="inner-items">
        <a v-if="externalLink" :href="externalLink" class="cta-button" rel="noopener noreferrer">View {{ title }}</a>
        <router-link v-if="routerTo" :to="{ name: `${routerTo}`}" class="cta-button">View {{ routerTo }}</router-link>
        <br/>
        {{ description }} <br/>
        <div class="source-wrapper">
          <img src="@/assets/github-mark-white.svg" class="gh-logo">
          <a :href="sourceURL" class="blue project-link">View Source</a> <br/>
        </div>
      </div>
    </q-expansion-item>
  </div>
</template>


<style scoped>
.container{
  width: 100%;
  margin: 15px 5px 15px 5px;
  min-width: 420px;
  max-width: 420px;
  border: 1px solid #DDDDDD;
}

.inner-items {
  padding-left: 30px;
  padding-right: 30px;
  padding-top: 8px;
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

.cta-button {
  display: inline-block;
  padding: 10px 20px;
  background-color: #3498db;
  color: white;
  text-decoration: none;
  border-radius: 5px;
  font-weight: bold;
  margin-bottom: 15px;
  transition: background-color 0.3s ease;
}

.cta-button:hover {
  background-color: #2980b9;
}

/* .arrow {
  padding: 3px 5px 3px 5px;
  border: 1px solid black;
  float: right;
} */
</style>
