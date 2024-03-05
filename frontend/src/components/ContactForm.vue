<script setup>

import { ref, computed } from 'vue';

import axios from 'axios';

import { useToast } from 'vue-toastification';

import { Tippy } from 'vue-tippy';
import 'tippy.js/dist/tippy.css'

const form = ref({
  message: '',
  sender_name: '',
  contact_info: '',
});

const isFormEmpty = computed(() => {
  return (form.value.message === '' ||
          form.value.sender_name === '' || 
          form.value.contact_info === '');
});

const toast = useToast();

const submitForm = async () => {
  if (isFormEmpty.value) return; 

  try {
    await axios.post("/api/contact", form.value);
    toast.success('Message sent successfully!');

    form.value = { message: '', sender_name: '', contact_info: '' }; // Reset form
  } catch (error) {
    toast.error('Failed to send message.');

    console.error('Failed to send message:', error);
  }
};
</script>

<template>
    <div class="contact-form">
        <div class="spacer"></div>
        <label for="name">Your Name</label> 
        <input type="text" v-model="form.sender_name" id="name" placeholder="">
        <label for="contact-information">Contact Information</label> 
        <input type="text" v-model="form.contact_info" id="contact-information" placeholder="">
        <label for="message">Message</label> 
        <textarea v-model="form.message" id="message" placeholder=""></textarea>
        <tippy content="All fields are required for sending a message" placement="bottom">
          <button class="button-4" @click="submitForm" :disabled="isFormEmpty" role="button">
            Send
          </button>
        </tippy>
    </div>

</template>

<style scoped>
/* I don't think I like this but I'm undecided */
/* .contact-form {
  display: flex;
  flex-wrap: nowrap;
  flex-direction: column;
  align-items: center;
} */
.spacer {
  padding-top: 40px;
}
label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

input {
  max-width: 120px;
}
textarea {
  min-height: 100px;
}
input,
textarea {
  font-family: -apple-system, system-ui, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
  border: none;
  background-color: #292929;
  color: #CCCCCC;
  font-size: 16px;
  width: 100%;
  padding: 8px;
  margin-bottom: 20px; /* Adds space below each input/textarea */
  box-sizing: border-box; /* Ensures padding does not add to the total width */
  resize: none;
  min-width: 320px;
}

</style>