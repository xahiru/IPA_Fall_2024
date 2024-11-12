<script setup>
import router from '../router';



</script>

<template>
  <div id="body">
    
    <div class="home">
      <header class="header">
        <h1 class="title">Greenhouse Farming System</h1>
        <p class="subtitle">Empowering sustainable agriculture with technology</p>
      </header>
    
      <section class="info-section">
        <ul class="features-list">
          <li>Real-time temperature and humidity monitoring</li>
          <li>Automated irrigation and lighting controls</li>
          <li>Data analytics for optimal crop growth</li>
        </ul>
      </section>
      
      <div class="buttons">
        <router-link to="/login">
          <button class="button login-button">Login</button>
        </router-link>
        <router-link to="/Signup">
          <button class="button signup-button">Signup</button>
        </router-link>
      </div>
    </div>
    
    
    
  </div>
</template>

<style scoped>
#body{
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center;
}

body {
  font-family: 'Roboto', sans-serif;
  background: linear-gradient(135deg, #88d8b0, #56ab2f);
  color: #333;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  margin: 0;
}

.home {
  text-align: center;
  background: #ffffff26;
  padding: 40px;
  border-radius: 15px;
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.2);
  max-width: 500px;
  width: 100%;
}

.header {
  margin-bottom: 30px;
}

.title {
  font-size: 2rem;
  color: #ffffff;
  margin-bottom: 10px;
}

.subtitle {
  font-size: 1rem;
  color: #c9c9c9;
}

.info-section {
  font-size: 0.95rem;
  color: #232323;
  line-height: 1.5;
  margin: 20px 0;
}

.features-list {
  list-style-type: none;
  padding: 0;
  margin: 15px 0;
}

.features-list li {
  background: #ffffff78;
  padding: 8px;
  margin-bottom: 8px;
}

.buttons {
  display: flex;
  gap: 20px;
  justify-content: center;
  margin-top: 25px;
}

.button {
  padding: 12px 28px;
  font-size: 1rem;
  font-weight: 600;
  color: white;
  border: whitesmoke;
  cursor: pointer;
  border-radius: 8px;
  transition: all 0.5s ease;
}

.button:hover {
  transform: translateY(-2px);
  box-shadow: 0px 8px 15px rgba(171, 171, 171, 0.293);
}

.login-button {
  background-color: #ffffff29;
}

.signup-button {
  background-color: #0846c1dc;
}

.login-button:hover {
  background-color: #ffffffa2;
}

.signup-button:hover {
  background-color: #031987;
}

</style>