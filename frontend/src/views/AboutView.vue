<script setup>

// import RollingAnimation from '../components/animations/RollingAnimation.vue'

</script>
<template>
  <div class="about">
    <div class="header">
      <h2 class="about-header">Hi, I'm Ryan</h2>
      <img class="propic" src="/public/propic.jpg">
    </div>
    <p class="about-item">I'm a software engineer with a passion for solving complex problems and creating efficient, user-friendly applications. I earned my Bachelor's degree in Computer Science with a minor in Spanish and an honors distinction from Westminster University, as well as an Associate's degree with honors distinction from Utah Valley University. My technical skills include proficiency in Python, Java, JavaScript, Vue.js, and various AWS services. I'm also well-versed in both SQL and NoSQL data storage technologies, such as PostgreSQL, DynamoDB, and MongoDB.</p>
    <p class="about-item">Throughout my professional journey, I have had the privilege of working with industry leaders like Amazon, where I developed and maintained scripts, optimized database infrastructure, and collaborated with cross-functional teams to deliver high-quality software. I take pride in my ability to bridge the gap between technical and non-technical stakeholders, effectively communicating complex concepts and translating business requirements into efficient code.</p>
    <p class="about-item">As an avid learner, I constantly seek to expand my knowledge and stay up-to-date with the latest industry trends, particularly in the rapidly evolving field of artificial intelligence. I enjoy exploring and utilizing new AI technologies, such as OLLAMA and Stable Diffusion, to enhance my projects and push the boundaries of what's possible.</p>
    <a href="/projects" class="projects-link blue">Check out some projects here</a>
    <p class="about-item">When I'm not immersed in code, you can find me enjoying the great outdoors with my dog, going on hikes or camping trips with friends. I'm also an avid music listener (some might say borderline addict!) and enjoy the occasional game, whether it's video games, sports, or board games. I find that having a variety of interests and experiences outside of work helps me approach problems with fresh perspectives and creative solutions.</p>
    <p class="about-item">If you'd like to learn more about my work or discuss potential collaborations, feel free to reach out through the Contact&nbsp;section. I'm always excited to connect with fellow professionals and explore new opportunities!</p>
    <a href="/contact" class="contact-link blue">Contact me directly</a>

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

.projects-link, .contact-link {
  font-size: 1.1rem;
  background-color: #202020;
  border-radius: 8px;
  border: 2px solid #303030;
}
</style>
