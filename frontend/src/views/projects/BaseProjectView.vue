<template>

 <div class="backButtonContainer">
   <div class="backButton">
      <router-link to="/projects" class="button-4 routerLink">Back to projects</router-link>
   </div>
   <slot class="project"></slot> <!-- slot for project view -->
 </div>

</template>


<style scoped>
.backButtonContainer {
   margin-top: 30px;
}
.backButton {
   display: flex;
   align-items: center;
   flex-direction: column;

   margin-bottom: 30px;
}
.routerLink {
   text-decoration: none;
   color: inherit;
   display: inline-block;
   padding: 10px 20px;
}
</style>