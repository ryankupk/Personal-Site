<script setup>
import { ref } from 'vue';

const emit = defineEmits(['login', 'register']);

const username = ref('');
const password = ref('');
const isRegistering = ref(false);

const submitForm = () => {
  const credentials = { username: username.value, password: password.value };
  if (isRegistering.value) {
    emit('register', credentials);
  } else {
    emit('login', credentials);
  }
};

const toggleMode = () => {
  isRegistering.value = !isRegistering.value;
};
</script>

<template>
  <div class="login-form">
    <h2>{{ isRegistering ? 'Register' : 'Login' }}</h2>
    <form @submit.prevent="submitForm">
      <input v-model="username" type="text" placeholder="Username" required>
      <input v-model="password" type="password" placeholder="Password" required>
      <button type="submit">{{ isRegistering ? 'Register' : 'Login' }}</button>
    </form>
    <p>
      {{ isRegistering ? 'Already have an account?' : 'Don\'t have an account?' }}
      <a href="#" @click.prevent="toggleMode">{{ isRegistering ? 'Login' : 'Register' }}</a>
    </p>
  </div>
</template>

<style scoped>
.login-form {
  max-width: 300px;
  margin: 0 auto;
  padding: 20px;
  background-color: #2a2a2a;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

h2 {
  text-align: center;
  margin-bottom: 20px;
}

form {
  display: flex;
  flex-direction: column;
}

input {
  margin-bottom: 10px;
  padding: 10px;
  border: 1px solid #444;
  background-color: #333;
  color: #f0f0f0;
  border-radius: 4px;
}

button {
  background-color: #4CAF50;
  color: white;
  border: none;
  padding: 12px;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #45a049;
}

p {
  text-align: center;
  margin-top: 10px;
}

a {
  color: #4CAF50;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}
</style>