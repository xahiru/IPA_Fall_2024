<template>
  <div class="signup-page">
    <div class="signup-container max-w-md mx-auto p-4">
      <h1 class="text-2xl font-bold mb-4">Sign Up</h1>
      <form @submit.prevent="register" class="flex flex-col gap-4">
        <div>
          <label for="username" class="block font-medium">Username</label>
          <input
            id="username"
            type="text"
            v-model="username"
            required
            class="input-field"
            placeholder="Enter your username"
          />
        </div>
        <div>
          <label for="email" class="block font-medium">Email</label>
          <input
            id="email"
            type="email"
            v-model="email"
            required
            class="input-field"
            placeholder="Enter your email"
          />
        </div>
        <div>
          <label for="password" class="block font-medium">Password</label>
          <input
            id="password"
            type="password"
            v-model="password"
            required
            class="input-field"
            placeholder="Enter your password"
          />
        </div>
        <br>
        <button type="submit" class="btn-primary">Sign Up</button>
      </form>
      <p class="mt-4 text-center">
        Already have an account?
        <router-link to="/login" class="text-blue-500 hover:underline">Log in</router-link>
      </p>
    </div>
  </div>  
</template>
  
<script>
import axios from 'axios';

  export default {
    data() {
      return {
        username: '',
        email: '',
        password: '',
      };
    },
    methods: {
      async register() {
      try {
        const newUser = {
          username: this.username,
          email: this.email,
          password: this.password,
        };

        const response = await axios.post('http://localhost:3000/users', newUser);
        if (response.status === 201) {
          this.$router.push('/login');
        }
      } catch (error) {
        console.error('Registration failed:', error);
        alert('Something went wrong. Please try again.');
      }
    },
  },
};
</script>
  
<style scoped>
  .signup-page {
    background-image: url("src/assets/signup-background.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    height: 100vh;
    display: flex;
    flex-direction: column;
    text-align: center;
    align-items: center;
    justify-content: center;
  }
  .signup-container {
    background-color: #ffffff2d;
    border: 1px solid #e5e7eb;
    border-radius: 8px;
    padding: 2rem;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    width: 100%;
    max-width: 300px;
  }
  p {
    color: white;

  }
  
  .input-field {
    width: 100%;
    padding: 0.75rem;
    margin-top: 0.25rem;
    border: 1px solid #d1d5db;
    border-radius: 4px;
  }
  
  .btn-primary {
    background-color: #0666ff;
    color: white;
    padding: 0.75rem;
    font-weight: bold;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  .btn-primary:hover {
    background-color: #0051ff;
  }
</style>