<script setup>

import { ref } from 'vue';
import axios from 'axios';

const form = ref({
  message: '',
  sender: '',
  contact_info: '',
});

const submitForm = async () => {
  try {
    await axios.post('http://localhost:3001/api/contact/', form.value);
    alert('Message sent successfully!');
    form.value = { message: '', sender: '', contact_info: '' }; // Reset form
  } catch (error) {
    console.error('Failed to send message:', error);
    alert('Failed to send message.');
  }
};

</script>

<template>
    <div class="contact-form">
        <input type="text" v-model="form.sender" placeholder="Your Name">
        <input type="email" v-model="form.contact_info" placeholder="Your Email">
        <textarea v-model="form.message" placeholder="Your Message"></textarea>
        <button @click="submitForm">Send</button>

    </div>

</template>

<style scoped>

</style>