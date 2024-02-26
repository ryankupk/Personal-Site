<script setup>

import { ref } from 'vue';
import axios from 'axios';
import { useToast } from 'vue-toastification';


const form = ref({
  message: '',
  sender: '',
  contact_info: '',
});

const toast = useToast();

const submitForm = async () => {
  try {
    await axios.post("/api/contact", form.value);
    toast.success('Message sent successfully!');

    form.value = { message: '', sender: '', contact_info: '' }; // Reset form
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
        <input type="text" v-model="form.sender" id="name" placeholder="">
        <label for="contact-information">Contact Information</label> 
        <input type="text" v-model="form.contact_info" id="contact-information" placeholder="">
        <label for="message">Message</label> 
        <textarea v-model="form.message" id="message" placeholder=""></textarea>
        <button class="button-4" @click="submitForm" role="button">Send</button>

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

/* button */
.button-4 {
  appearance: none;
  background-color: #292929;
  border: 1px solid rgba(27, 31, 35, 0.15);
  border-radius: 6px;
  box-shadow: rgba(27, 31, 35, 0.04) 0 1px 0, rgba(255, 255, 255, 0.25) 0 1px 0 inset;
  box-sizing: border-box;
  color: #CCCCCC;
  cursor: pointer;
  display: inline-block;
  font-family: -apple-system, system-ui, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
  font-size: 14px;
  font-weight: 500;
  line-height: 20px;
  list-style: none;
  padding: 6px 16px;
  position: relative;
  transition: background-color 0.2s cubic-bezier(0.3, 0, 0.5, 1);
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  vertical-align: middle;
  white-space: nowrap;
  word-wrap: break-word;
}

.button-4:hover {
  background-color: #202020;
  text-decoration: none;
  transition-duration: 0.1s;
}

.button-4:disabled {
  background-color: #FAFBFC;
  border-color: rgba(27, 31, 35, 0.15);
  color: #959DA5;
  cursor: default;
}

.button-4:active {
  background-color: #EDEFF2;
  box-shadow: rgba(225, 228, 232, 0.2) 0 1px 0 inset;
  transition: none 0s;
}

.button-4:focus {
  outline: 1px transparent;
}

.button-4:before {
  display: none;
}

.button-4:-webkit-details-marker {
  display: none;
}

</style>