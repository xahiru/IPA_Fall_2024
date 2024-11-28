<script setup>
import { useRouter } from 'vue-router';
import Navbar from './Navbar.vue';

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
    <Navbar />
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
        <router-link to="/login" @click="afterLogin" class="button login-button">Login</router-link>
        <router-link to="/signup" @click="afterLogin" class="button signup-button">Signup</router-link>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Global Reset */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Roboto', sans-serif;
  background: linear-gradient(135deg, #88d8b0, #56ab2f);
  color: #333;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

#body {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  padding: 20px;
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
  font-size: 1.1rem;
  color: #7f8c8d;
}

.info-section {
  font-size: 1rem;
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

/* Responsive Styles */

/* Large screens */
@media (max-width: 1200px) {
  .home {
    padding: 30px;
    margin-top: 200px;
  }

  .title {
    font-size: 2rem;
  }

  .subtitle {
    font-size: 1rem;
  }

  .buttons {
    gap: 15px;
  }

  .button {
    font-size: 0.95rem;
  }
}

/* Medium Screens (Tablets) */
@media (max-width: 768px) {
  .home {
    max-width: 90%; /* Makes the home section occupy 90% width on tablets */
    padding: 30px;
    margin-top: 200px;
  }

  .title {
    font-size: 1.8rem;
  }

  .subtitle {
    font-size: 1rem;
  }

  .buttons {
    flex-direction: column;
    gap: 15px; /* Stack buttons vertically */
  }

  .button {
    font-size: 1.1rem; /* Slightly increase button font size for better visibility */
  }
}

/* Small Screens (Phones) */
@media (max-width: 480px) {
  .home {
    padding: 20px;
    max-width: 95%; /* Slightly larger home width */
    margin-top: 200px;
  }

  .title {
    font-size: 1.5rem;
  }

  .subtitle {
    font-size: 0.9rem;
  }

  .info-section {
    font-size: 0.95rem; /* Slightly smaller text for better readability */
  }

  .buttons {
    gap: 10px;
  }

  .button {
    padding: 10px 24px;
    font-size: 0.95rem; /* Make button font smaller on smaller screens */
  }
}
</style>
