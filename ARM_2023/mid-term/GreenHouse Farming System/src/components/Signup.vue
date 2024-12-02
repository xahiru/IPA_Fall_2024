<script setup>
import { ref } from 'vue'
import { signup } from '../api/api'
import { useRouter } from 'vue-router'

const username = ref('')
const email = ref('')
const password = ref('')
const router = useRouter()

const signup_page = async () => {
  console.log('Attempting to sign up with:', username.value, email.value, password.value)

  const response = await signup(username.value, email.value, password.value)
  console.log('Response from signup:', response)
  if (response.success) {
    router.push({ name: 'Dashboard' })
  } else {
    alert('Signup failed: ' + (response.error || 'Unknown error'))
  }
}
</script>

<template>
  <div id="bdy">
    <div class="login-page">
      <header class="header">
        <h1 class="title">Greenhouse Farming System</h1>
        <p class="subtitle">Create an account to get started</p>
      </header>

      <form class="login-form" @submit.prevent="signup_page">
        <label for="name">Full Name</label>
        <input
          type="text"
          id="name"
          class="input-field"
          v-model="username"
          placeholder="Enter your full name"
          required
        />

        <label for="email">Email Address</label>
        <input
          type="email"
          id="email"
          class="input-field"
          v-model="email"
          placeholder="Enter your email"
          required
        />

        <label for="password">Password</label>
        <input
          type="password"
          id="password"
          class="input-field"
          v-model="password"
          placeholder="Create a password"
          required
        />

        <button type="submit" class="button login-button">Sign Up</button>

        <p class="signup-prompt">
          Already have an account?
          <router-link to="/login" class="signup-link">Login here</router-link>
        </p>
      </form>
    </div>
  </div>
</template>

<style>
#bdy {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: 'Poppins', sans-serif;
  background: linear-gradient(135deg, #f0c27b, #4b1248);
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  margin: 0;
  color: #ffffff;
}

.login-page {
  text-align: center;
  max-width: 400px;
  width: 100%;
  background: rgba(255, 255, 255, 0.15);
  padding: 35px;
  border-radius: 15px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
}

.header {
  margin-bottom: 30px;
}

.title {
  font-size: 2.5rem;
  font-weight: 700;
  color: #ffffff;
  text-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
}

.subtitle {
  font-size: 1.1rem;
  color: #f0f0f0;
  margin-top: 5px;
  font-weight: 300;
  text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.2);
}

.login-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.input-field {
  padding: 12px 15px;
  font-size: 1rem;
  border-radius: 8px;
  outline: none;
  border: 1px solid #d1cfe2;
  background: rgba(255, 255, 255, 0.85);
  transition: all 0.3s ease;
}

.input-field:focus {
  background: #ffffff;
  border-color: #6c63ff;
}

.button {
  padding: 12px 20px;
  font-size: 1.1rem;
  font-weight: 600;
  color: white;
  background: linear-gradient(90deg, #6c63ff, #8e70c9);
  border: none;
  cursor: pointer;
  border-radius: 8px;
  transition: all 0.3s ease;
}

.button:hover {
  transform: scale(1.05);
  background: linear-gradient(90deg, #076322, #26a60d);
}

.signup-prompt {
  font-size: 0.95rem;
  color: #d1cfe2;
}

.signup-link {
  color: #ffffff;
  font-weight: 600;
  text-decoration: underline;
  transition: color 0.3s ease;
}

.signup-link:hover {
  color: #8e70c9;
  text-decoration: none;
}
</style>
