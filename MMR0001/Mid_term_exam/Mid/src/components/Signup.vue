<script setup>
import { ref } from 'vue';
import { signup } from '../components/api';
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


</script>

<template>
    <div id="bdy">
        <div class="login-page">
            <header class="header">
              <h1 class="title">Greenhouse Farming System</h1>
              <p class="subtitle">Signup to create an account</p>
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


<style scoped>

#bdy {
  font-family: 'Arial', sans-serif;
  background-color: #21153a; 
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0;
}


.login-page {
  background: rgba(255, 255, 255, 0.1);
  padding: 20px 30px;
  border-radius: 15px;
  box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
  text-align: center;
  width: 90%;
  max-width: 400px;
}

.header .title {
  font-size: 2rem;
  margin-bottom: 10px;
  text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
}

.header .subtitle {
  font-size: 1rem;
  margin-bottom: 20px;
  color: #f0f0f0;
}

.login-form {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.input-field {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 8px;
  font-size: 1rem;
  width: 100%;
  box-sizing: border-box;
  outline: none;
  transition: border-color 0.2s;
}

.input-field:focus {
  border-color: #88cc88;
}

.button {
  background-color: #2b580c;
  color: white;
  border: none;
  border-radius: 8px;
  padding: 10px 15px;
  font-size: 1rem;
  font-weight: bold;
  cursor: pointer;
  transition: background 0.3s, transform 0.2s;
}

.button:hover {
  background-color: #1e3d08;
  transform: scale(1.05);
}

.button:active {
  transform: scale(0.98);
}

.signup-prompt {
  margin-top: 10px;
  color: #f0f0f0;
}

.signup-link a {
  color: #88cc88;
  font-weight: bold;
  text-decoration: none;
}

.signup-link a:hover {
  text-decoration: underline;
}

@media (max-width: 600px) {
  .header .title {
    font-size: 1.8rem;
  }

  .header .subtitle {
    font-size: 0.9rem;
  }

  .button {
    font-size: 0.9rem;
  }
}
</style>
