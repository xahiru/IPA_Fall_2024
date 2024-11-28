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
        <p class="subtitle">Enhancing growth with data-driven insights</p>
      </header>
    
      <section class="info-section">
        <div class="highlight">
        </div>
        <ul class="features-list">
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

.home {
    text-align: center;
    background: rgba(255, 255, 255, 0.1);
    padding: 50px;
    border-radius: 20px;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
    max-width: 550px;
    width: 100%;
    animation: fadeIn 1s ease;
}

@keyframes fadeIn {
  from { opacity: 0; transform: scale(0.9); }
  to { opacity: 1; transform: scale(1); }
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