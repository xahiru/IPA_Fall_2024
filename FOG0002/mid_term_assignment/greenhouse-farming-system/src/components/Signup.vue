<script setup>
import { ref, onMounted } from 'vue';
import { signup } from '../api/api';
import { useRouter } from 'vue-router';

const username = ref('');
const email = ref('');
const password = ref('');
const router = useRouter();

const signup_page = async () => {
    console.log("Attempting to sign up with:", username.value, email.value, password.value);

    const response = await signup(username.value, email.value, password.value);
    console.log("Response from signup:", response);
    if (response.success) {
        router.push({ name: 'Dashboard' });
    } else {
        alert("Signup failed: " + (response.error || "Unknown error"));
    }
};

onMounted(() => {
    const user = localStorage.getItem("user");
    if (user) {
        router.push({ name: 'Dashboard' });
    }
});

</script>

<template>
    <div id="bdy">
        <div class="login-page">
            <header class="header">
              <h1 class="title">Greenhouse Farming System</h1>
              <p class="subtitle">Login to access your dashboard</p>
            </header>
          
            <form class="login-form" @submit.prevent="signup_page">
                <label for="name">Name</label>
                <input type="name" id="name" class="input-field" v-model="username" placeholder="Enter your name" required>
              <label for="email">Email</label>
              <input type="email" id="email" class="input-field" v-model="email" placeholder="Enter your email" required>
          
              <label for="password">Password</label>
              <input type="password" id="password" class="input-field" v-model="password" placeholder="Enter your password" required>
          
              <button type="submit" class="button login-button">Signup</button>
              
              <p class="signup-prompt signup-link" > Already have an account?<router-link to="/login"> Login here</router-link></p>
             </form>
          </div>
          
    </div>
</template>


<style>
#bdy{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }
  
  body {
    font-family: 'Roboto', sans-serif;
    background: linear-gradient(135deg, #a3e5b0, #56ab2f);
    color: #333;
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
  }
  
  .header {
    margin-bottom: 30px;
  }
  
  .title {
    font-size: 2.5rem;
    font-weight: 700;
    color: #ffffff;
    text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.3);
  }
  
  .subtitle {
    font-size: 1rem;
    color: #e0ffe6;
    margin-top: 10px;
    text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.2);
  }
  
  .login-form {
    display: flex;
    flex-direction: column;
    gap: 15px;
    background: rgba(255, 255, 255, 0.15);
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  }
  
  .input-field {
    padding: 10px 15px;
    font-size: 1rem;
    border: none;
    border-radius: 5px;
    outline: none;
    background: rgba(255, 255, 255, 0.8);
  }
  
  .input-field:focus {
    background: #ffffff;
  }
  
  .button {
    padding: 12px 20px;
    font-size: 1rem;
    font-weight: 600;
    color: white;
    background-color: #3498db;
    border: none;
    cursor: pointer;
    border-radius: 8px;
    transition: 0.3s ease;
  }
  
  .button:hover {
    background-color: #2980b9;
  }
  
  .signup-prompt {
    margin-top: 20px;
    font-size: 0.9rem;
    color: #e0ffe6;
  }
  
  .signup-link {
    color: #ffffff;
    font-weight: 500;
    text-decoration: underline;
  }
  
  .signup-link:hover {
    color: #b0d8b0;
    text-decoration: none;
  }
  
</style>