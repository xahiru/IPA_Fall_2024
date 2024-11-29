<template>
  <div class="signup-page">
    <h1 class="title">Signup Form</h1>
    <form @submit.prevent="signupPage" class="signup-form">
      <input 
        v-model="username" 
        type="text" 
        placeholder="Username" 
        required 
        class="input-field" 
      />
      <input 
        v-model="email" 
        type="email" 
        placeholder="Email" 
        required 
        class="input-field" 
      />
      <input 
        v-model="password" 
        type="password" 
        placeholder="Password" 
        required 
        class="input-field" 
      />
      <button type="submit" class="button">Signup</button>
    </form>
    <p class="prompt">
      Already have an account? 
      <router-link to="/login" class="link">Login</router-link>
    </p>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { signup } from '../api/api';

const username = ref('');
const email = ref('');
const password = ref('');
const router = useRouter();

const signupPage = async () => {
  try {
    const response = await signup(username.value, email.value, password.value);
    if (response.success) {
      router.push({ name: 'Dashboard' });
    } else {
      alert('Signup failed: ' + (response.error || 'Unknown error'));
    }
  } catch (error) {
    alert('An error occurred during signup.');
  }
};
</script>

<style scoped>
.signup-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  padding: 20px;
  background: #0d1117; 
  color: #c9d1d9;
  border-radius: 10px;
}

.title {
  font-size: 2rem;
  font-weight: bold;
  color: #ffffff;
  margin-bottom: 20px;
}

.signup-form {
  display: flex;
  flex-direction: column;
  gap: 15px;
  width: 100%;
  max-width: 400px;
  background: rgba(255, 255, 255, 0.1);
  padding: 20px;
  border-radius: 8px;
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
  background-color: #238636;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.3s ease;
}

.button:hover {
  background-color: #2ea043;
  transform: translateY(-2px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
}

.prompt {
  margin-top: 20px;
  color: #8b949e;
}

.link {
  color: #58a6ff;
  text-decoration: underline;
  cursor: pointer;
}

.link:hover {
  color: #1f6feb;
}
</style>
