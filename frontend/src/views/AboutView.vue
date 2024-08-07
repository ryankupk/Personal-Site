<script setup>
import axios from 'axios';
import 'deep-chat';


// import RollingAnimation from '../components/animations/RollingAnimation.vue'

const history = [
  {role: 'user', text: 'Hey, how are you today?'},
  {role: 'ai', text: 'Good!'},

  {role: 'user', text: 'What\'s Ryan\'s LinkedIn URL?'},
  {role: 'ai', text: 'The URL for Ryan\'s LinkedIn profile is https://linkedin.com/in/ryan-kupka'},
]

const openChatModal = () => {
  const chatModal = document.getElementById('assistant-chat-modal');
  closeDisclaimerModal()
  chatModal.style.display = 'flex';
  chatModal.showModal();
};

const closeChatModal = () => {
  const chatModal = document.getElementById('assistant-chat-modal');
  chatModal.style.display = 'none';
  chatModal.close();
};

const openDisclaimerModal = () => {
  const chatModal = document.getElementById('disclaimer-modal');
  chatModal.style.display = 'flex';
  chatModal.showModal();
};

const closeDisclaimerModal = () => {
  const chatModal = document.getElementById('disclaimer-modal');
  chatModal.style.display = 'none';
  chatModal.close();
};

document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape') {
    closeChatModal();
  }
});

const sendMessage = async (message) => {
  console.log(message)
  const messageObject = {
    "message": message.text
  }
  const result = await axios.post("/api/chat", messageObject)
  console.log(result)
  return result;
}

</script>
<template>
  <div class="about">
    <div class="header">
      <h2 class="about-header">Hi, I'm Ryan</h2>
      <img class="propic" src="/propic.jpg">
    </div>
    <p class="about-item">I'm a software engineer with a passion for solving complex problems and creating efficient, user-friendly applications. I earned my Bachelor's degree in Computer Science with a minor in Spanish and an honors distinction from Westminster University, as well as an Associate's degree with honors distinction from Utah Valley University. My technical skills include proficiency in Python, Java, JavaScript, Vue.js, and various AWS services. I'm also well-versed in both SQL and NoSQL data storage technologies, such as PostgreSQL, DynamoDB, MongoDB, and S3.</p>
    <p class="about-item">Throughout my professional journey, I have had the privilege of working with industry leaders like Amazon, where I developed and maintained scripts, optimized database infrastructure, and collaborated with cross-functional teams to deliver high-quality software. I take pride in my ability to bridge the gap between technical and non-technical stakeholders, effectively communicating complex concepts and translating business requirements into efficient code.</p>
    <p class="about-item">As an avid learner, I love to expand my knowledge and stay up-to-date with the latest industry trends, particularly in the rapidly evolving field of artificial intelligence. I enjoy exploring and utilizing new AI technologies, such as local LLMs with Ollama and image generation with Stable Diffusion, to enhance my projects and push the boundaries of what's possible.</p>
    <a href="/projects" class="projects-link blue">Check out some projects here</a>
    <p class="about-item">When I'm not immersed in code, you can find me enjoying the outdoors with my dog, going on hikes or camping trips with friends. I'm also an avid music listener (some might say borderline addict!) and enjoy the occasional game, whether it's video games, sports, or board games. As a fan of mechanical and custom keyboards, I enjoy writing the C/QMK code for the firmware of my Sofle V2.1. I like having a variety of interests and experiences outside of work, which also helps me approach problems with fresh perspectives and creative solutions.</p>
    <p class="about-item">If you'd like to learn more about my work or discuss potential collaborations, feel free to reach out through the Contact&nbsp;section. I'm always excited to connect with others and explore new opportunities!</p>
    <div class="cta-wrapper">
      <a href="/contact" class="contact-link blue">Contact me directly</a>
      <div style="cursor:pointer;" class="chat-link blue" @click="openDisclaimerModal">Chat with my personal AI LLM assistant</div>
    </div>

    <dialog class="disclaimer-modal modal" id="disclaimer-modal" style="flex-direction: column;">
      <span class="disclaimer-text">
        This is an LLM based on a very small model. It will almost definitely make mistakes or say things which are outright wrong. It will likely answer questions that it's not supposed to. It usually does provide accurate information, but there's no reason to believe that what it says is exactly correct. This entire chat feature is for entertainment purposes. By agreeing to use it, the site owner will not be held responsible for anything that the LLM says.
      </span>

      <div class="disclaimer-buttons">
        <button class="disclaimer-accept-button" @click="openChatModal">Accept and continue to chat</button>
        <button class="disclaimer-decline-button" @click="closeDisclaimerModal">Decline</button>
      </div>
    </dialog>

    <dialog class="chat-modal modal" id="assistant-chat-modal">
      <button class="close-button" @click="closeChatModal">×</button>
      <deep-chat
        class="deep-chat"
        :textInput="{ placeholder: { text: 'Message AI assistant' } }"
        :history="history"
        :connect="{
          url: 'http://192.168.1.114:3001/api/chat/',
          method: 'POST',
        }"
        :chatStyle="{
          backgroundColor: '#f7f7f7',
          borderRadius: '8px',
          width: '90%',
          height: '90%',
        }"
      />
    </dialog>
    <!-- <RollingAnimation :attributes="[1, 2, 3]"/> -->
    
  </div>
</template>

<style>
@media (min-width: 1024px) {
}
.about {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.header {
  display: flex;
  align-items: center;
  margin-top: 40px;
}
.about-header {
  margin-right: 45px;
}
.propic {
  border-radius: 25px;
  width: 140px;
}

.about-item {
  font-family: 'Abril Fatface', 'Playfair Display', 'Raleway', 'Lobster', 'Cardo', 'Josefin Sans';
  text-align: justify;
  font-size: 1.3rem;
  margin-top: 25px;
  margin-bottom: 25px;
}

.projects-link, .contact-link, .chat-link {
  font-size: 1.1rem;
  background-color: #202020;
  border-radius: 8px;
  border: 2px solid #303030;
  margin-top: 15px; /* Adjust as needed for spacing */
}

.cta-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 15px;
}

.modal {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 80%;
  max-width: 800px;
  height: 80%;
  max-height: 600px;
  padding: 20px;
  border: none;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  background-color: var(--color-background);
  color: white;
}
.chat-modal {
  display: none;
  flex-direction: column;
}
dialog::backdrop {
  background-color: rgba(0, 0, 0, 0.5);
}
.close-button {
  position: absolute;
  top: 10px;
  right: 10px;
  font-size: 24px;
  background: none;
  border: none;
  cursor: pointer;
  color: #333;
  z-index: 1001;
}
.disclaimer-buttons {
  display: flex;
  justify-content: center;
  margin-top: auto;
}
.disclaimer-accept-button, .disclaimer-decline-button {
  width: 20%;
  margin: 10px;
  color: black;
  /* background-color: var(--vt-c-black); */
}
.disclaimer-accept-button:hover, .disclaimer-decline-button:hover {
  cursor: pointer;
}

</style>
