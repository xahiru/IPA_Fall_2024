<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';

const name = ref('');
const email = ref('');
const password = ref('');
const router = useRouter();

async function signup() {
  try {
    let result = await axios.post("http://localhost:3000/user", {
      name: name.value,
      email: email.value,
      password: password.value
    });

    if (result.status === 201) {
      localStorage.setItem("user", JSON.stringify(result.data));
      router.push({ name: 'Home' });
    }
  } catch (error) {
    console.error("Error signing up:", error);
  }
}

onMounted(() => {
  let user = localStorage.getItem("user");
  if (user) {
    router.push({ name: "Home" });
  }
});
</script>

<template>
  <main id="signup-page">
    <section class="signup-container">
      <header class="signup-header">
        <h1 class="signup-title">Join EcoGrow</h1>
        <p class="signup-subtitle">Create an account to start managing your greenhouse</p>
      </header>
      
      <form class="signup-form" @submit.prevent="signup">
        
        <label for="name" class="input-label">Name</label>
        <input type="test" id="name" class="input-field" v-model="name" placeholder="Enter your name" required>

        <label for="email" class="input-label">Email</label>
        <input type="email" id="email" class="input-field" v-model="email" placeholder="Enter your email" required>
        
        <label for="password" class="input-label">Password</label>
        <input type="password" id="password" class="input-field" v-model="password" placeholder="Create a password" required>
        
        <button type="submit" class="signup-btn">Sign Up</button>
      </form>
      
      <footer class="signup-footer">
        <p class="login-link">
          Already have an account? 
          <router-link to="/login" class="login-link-text">Log in here</router-link>
        </p>
      </footer>
    </section>
  </main>
</template>

<style scoped>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

#signup-page {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: #e0f7f4;
  font-family: 'Arial', sans-serif;
  padding: 2rem;
}

.signup-container {
  background-color: #ffffff;
  padding: 2rem;
  width: 100%;
  max-width: 400px;
  border-radius: 12px;
  box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.signup-header {
  margin-bottom: 2rem;
}

.signup-title {
  font-size: 2rem;
  color: #2c3e50;
}

.signup-subtitle {
  font-size: 1rem;
  color: #7f8c8d;
}

.signup-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.input-label {
  text-align: left;
  font-size: 0.9rem;
  color: #555555;
}

.input-field {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-size: 1rem;
}

.input-field:focus {
  outline: none;
  border-color: #2ecc71;
  box-shadow: 0 0 8px rgba(46, 204, 113, 0.2);
}

.signup-btn {
  background-color: #2ecc71;
  color: white;
  padding: 0.75rem;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.signup-btn:hover {
  background-color: #27ae60;
}

.signup-footer {
  margin-top: 1.5rem;
}

.login-link {
  font-size: 0.9rem;
  color: #7f8c8d;
}

.login-link-text {
  color: #3498db;
  text-decoration: none;
  font-weight: bold;
}

.login-link-text:hover {
  text-decoration: underline;
}
</style>
