<script setup>


</script>

<template>
  <div id="body">
    
    <div class="home">
      <header class="header">
        <h1 class="title">Greenhouse Farming System</h1>
        <p class="subtitle">Empowering sustainable agriculture with technology</p>
      </header>
    
      <section class="info-section">
        <p>Welcome to our Greenhouse Farming System, designed to help you monitor, control, and optimize your greenhouse environment for maximum yield and efficiency. Our system includes:</p>
        <ul class="features-list">
          <li>Real-time temperature and humidity monitoring</li>
          <li>Automated irrigation and lighting controls</li>
          <li>Data analytics for optimal crop growth</li>
        </ul>
      </section>
      
      <div class="buttons">
          <router-link to="/login" class="button login-button">Login</router-link>
          <router-link to="/login" class="button signup-button">Signup</router-link>
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
  background: #ffffff;
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
  font-size: 2.5rem;
  color: #2c3e50;
  margin-bottom: 10px;
}

.subtitle {
  font-size: 1rem;
  color: #7f8c8d;
}

.info-section {
  font-size: 0.95rem;
  color: #4d4d4d;
  line-height: 1.5;
  margin: 20px 0;
}

.features-list {
  list-style-type: none;
  padding: 0;
  margin: 15px 0;
}

.features-list li {
  background: #e0f7e0;
  padding: 8px;
  border-radius: 5px;
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
  border: none;
  cursor: pointer;
  border-radius: 8px;
  transition: all 0.3s ease;
}

.button:hover {
  transform: translateY(-2px);
  box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);
}

.login-button {
  background-color: #3498db;
  text-decoration: none;
}

.signup-button {
  background-color: #2ecc71;
  text-decoration: none;
}

.login-button:hover {
  background-color: #2980b9;
}

.signup-button:hover {
  background-color: #27ae60;
}

</style>
