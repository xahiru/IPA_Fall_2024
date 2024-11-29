<template>
  <div class="home-container">
    <header class="header">
      <h1 class="title">Greenhouse Farming System</h1>
      <p class="subtitle">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Tenetur recusandae quaerat dolorum at quos eos magnam qui earum! Molestias dignissimos, omnis nisi modi quo optio quibusdam est magnam odio alias!
      </p>
    </header>

    <div class="buttons">
      <router-link to="/login">
        <button class="button login-button">Login</button>
      </router-link>
      <router-link to="/signup">
        <button class="button signup-button">Signup</button>
      </router-link>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
const router = useRouter();

const afterLogin = () => {
  const user = localStorage.getItem("user");
  if (user) {
    router.push({ name: 'Dashboard' });
  }
};

afterLogin();
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.home-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: #0d1117;
  color: #c9d1d9;
  text-align: center;
  padding: 20px;
}

.header {
  margin-bottom: 30px;
}

.title {
  font-size: 2.5rem;
  font-weight: bold;
  color: #fefeff;
  margin-bottom: 10px;
}

.subtitle {
  font-size: 1rem;
  color: #8b949e;
  max-width: 600px;
  line-height: 1.5;
}

.buttons {
  display: flex;
  gap: 15px;
  margin-top: 30px;
}

.button {
  padding: 12px 24px;
  font-size: 1rem;
  font-weight: bold;
  color: #ffffff;
  background-color: #21262d;
  border: 2px solid transparent;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s ease, border 0.3s ease, transform 0.3s ease;
}

.button:hover {
  background-color: #30363d;
  transform: translateY(-3px);
  box-shadow: 0 8px 15px rgba(0, 0, 0, 0.3);
}

.login-button {
  background-color: #21262d;
}

.signup-button {
  background-color: #238636;
}

.signup-button:hover {
  background-color: #2ea043; 
}
</style>
