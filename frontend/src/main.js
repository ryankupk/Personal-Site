import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import Toast, { POSITION } from 'vue-toastification';
import 'vue-toastification/dist/index.css';

const app = createApp(App)

app.use(Toast, {
  // You can set global options here
  position: POSITION.BOTTOM_CENTER,
  timeout: 3000,
  closeOnClick: true,
  pauseOnFocusLoss: true,
  pauseOnHover: true,
  draggable: true,
  draggablePercent: 0.6,
});

app.use(router)

app.mount('#app')
