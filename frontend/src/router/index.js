import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('@/views/AboutView.vue')
    },
    {
      path: '/projects',
      name: 'projects',
      component: () => import('@/views/ProjectView.vue')
    },
      {
        path: '/projects/wordle',
        name: 'wordle',
        component: () => import('@/views/projects/wordle/WordleView.vue')
      },
      // { // not used since this is served by nginx directly
      //   path: '/projects/RayTracing',
      //   name: 'RayTracing',
      // },
      // { // not used since this is served by nginx directly
      //   path: '/projects/KnightsTour',
      //   name: 'KnightsTour',
      // },
    {
      path: '/services',
      name: 'services',
      component: () => import('@/views/ServicesView.vue')
    },
    {
      path: '/contact',
      name: 'contact',
      component: () => import('@/views/ContactView.vue')
    },
    {
      path: '/projects/book-library',
      name: 'bookLibrary',
      component: () => import('@/views/projects/BookLibrary/BookLibraryView.vue')
    },
  ]
})

export default router
