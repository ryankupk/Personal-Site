import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import Toast, { POSITION } from 'vue-toastification';
import 'vue-toastification/dist/index.css';

import VueTippy from 'vue-tippy';

import { Quasar } from 'quasar';
import 'quasar/src/css/index.sass';

const app = createApp(App);

app.use(router);

app.use(Toast, {
  position: POSITION.BOTTOM_CENTER,
  timeout: 3000,
  closeOnClick: true,
  pauseOnFocusLoss: true,
  pauseOnHover: true,
  draggable: true,
  draggablePercent: 0.6,
});

app.use(VueTippy, {
    component: 'tippy',
    followCursor: true
});

app.use(Quasar, {
  plugins: {}
});

app.mount('#app');
