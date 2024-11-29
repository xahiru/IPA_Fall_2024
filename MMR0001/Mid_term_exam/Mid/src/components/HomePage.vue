<script setup>
import { useRouter } from 'vue-router';
const router = useRouter();


const afterLogin = () => {
  const user = localStorage.getItem("user");
  if (user) {
    router.push({ name: 'Dashboard' });
  }
};

</script>

<template>
  <div id="body">
    
    <div class="home">
      <header class="header">
        <h1 class="title">Greenhouse Farming System</h1>
        <p class="subtitle">Agriculture with technology</p>
      </header>
    
      <section class="info-section">
        <p>Welcome to our Greenhouse Farming System, designed to help you monitor, control, and optimize your greenhouse environment</p>
      </section>
      
      <div class="buttons">
          <router-link to="/login" @click="afterLogin" class="button login-button">Login</router-link>
          <router-link to="/signup" @click="afterLogin" class="button signup-button">Signup</router-link>
      </div>
    </div>
    
    
    
  </div>
</template>

<style scoped>
#body {
  font-family: 'Arial', sans-serif;
  background-color: #21153a; 
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0;
}


.home {
  text-align: center;
  background: rgba(255, 255, 255, 0.1);
  padding: 20px;
  border-radius: 15px;
  box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
  width: 80%;
  max-width: 500px;
}

.header .title {
  font-size: 2.5rem;
  margin-bottom: 10px;
  text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
}

.header .subtitle {
  font-size: 1.2rem;
  margin-bottom: 20px;
  color: #f0f0f0;
}

.info-section p {
  font-size: 1rem;
  margin-bottom: 20px;
  line-height: 1.5;
  color: #e0e0e0;
}

.buttons {
  display: flex;
  justify-content: space-evenly;
  gap: 10px;
}

.button {
  display: inline-block;
  padding: 10px 20px;
  border: none;
  border-radius: 25px;
  font-size: 1rem;
  font-weight: bold;
  text-decoration: none;
  cursor: pointer;
  transition: background 0.3s, transform 0.2s;
}

.login-button {
  background-color: #2b580c;
  color: white;
}

.signup-button {
  background-color: #88cc88;
  color: white;
}

.button:hover {
  transform: scale(1.05);
}

.button:active {
  transform: scale(0.98);
}

.login-button:hover {
  background-color: #102edb;
}

.signup-button:hover {
  background-color: #1a2996;
}

@media (max-width: 600px) {
  .header .title {
    font-size: 2rem;
  }

  .header .subtitle {
    font-size: 1rem;
  }

  .button {
    font-size: 0.9rem;
    padding: 8px 15px;
  }
}
</style>
