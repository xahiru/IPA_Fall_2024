<template>
  <div class="login-container">
    <header>
      <h1 class="title">Dashboard Login</h1>
    </header>

    <form @submit.prevent="login_page" class="login-form">
      <input 
        v-model="email" 
        type="email" 
        placeholder="Enter your email" 
        class="input-field" 
        required 
      />
      <input 
        v-model="password" 
        type="password" 
        placeholder="Enter your password" 
        class="input-field" 
        required 
      />
      <button type="submit" class="button">Login</button>
      <p class="signup-prompt">
        Don't have an account? 
        <router-link to="/signup" class="signup-link">Sign up here</router-link>
      </p>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { login } from '../api/api';

const email = ref('');
const password = ref('');
const router = useRouter();

const login_page = async () => {
  const response = await login(email.value, password.value);
  if (response.success) {
    router.push({ name: 'Dashboard' });
  } else {
    alert(`Login failed: ${response.error || 'Unknown error'}`);
  }
};
</script>

<style scoped>
.login-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  padding: 20px;
  background: #0d1117;
  color: #c9d1d9;
}

.title {
  font-size: 2rem;
  font-weight: bold;
  color: #fcfcfc;
  margin-bottom: 15px;
}

.subtitle {
  font-size: 1.2rem;
  color: #8b949e;
  margin-bottom: 25px;
}

.login-form {
  display: flex;
  flex-direction: column;
  gap: 15px;
  background: rgba(255, 255, 255, 0.1);
  padding: 20px;
  border-radius: 10px;
  width: 100%;
  max-width: 400px;
  box-shadow: 0 8px 15px rgba(0, 0, 0, 0.5);
}

.input-field {
  padding: 12px;
  font-size: 1rem;
  border: none;
  border-radius: 5px;
  background: rgba(255, 255, 255, 0.2);
  color: #ffffff;
}

.input-field::placeholder {
  color: #b1b1b1;
}

.input-field:focus {
  background: rgba(255, 255, 255, 0.3);
  outline: none;
}

.button {
  padding: 12px;
  font-size: 1rem;
  font-weight: bold;
  color: white;
  background: #238636;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.3s ease;
}

.button:hover {
  background-color: #2ea043;
  transform: translateY(-2px);
}

.signup-prompt {
  margin-top: 15px;
  color: #8b949e;
  font-size: 0.9rem;
}

.signup-link {
  color: #58a6ff;
  text-decoration: underline;
}

.signup-link:hover {
  color: #1f6feb;
}
</style>
