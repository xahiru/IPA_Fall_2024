<template>
     <div id="bdy">
        <div class="signup-page">
            <header class="header">
              <h1 class="title">Greenhouse Farming System</h1>
              <p class="subtitle">Signup to register an account</p>
            </header>
          </div>
    <div class="signup-container">
      <h2>Sign Up</h2>
      <form @submit.prevent="handleSignup">
        <div class="form-group">
          <label for="username">Username:</label>
          <input
            type="text"
            id="username"
            class="input-field" placeholder="Enter your username"
            v-model="username"
            required
          />
        </div>
  
        <div class="form-group">
          <label for="email">Email:</label>
          <input
            type="email"
            id="email"
            class="input-field" placeholder="Enter your email"
            v-model="email"
            required
          />
        </div>
  
        <div class="form-group">
          <label for="password">Password:</label>
          <input
            type="password"
            id="password"
            class="input-field" placeholder="Enter your password"
            v-model="password"
            required
          />
        </div>
  
        <button type="submit">Sign Up</button>
        <p class="login-prompt">Already have an account? <a href="/login" class="Login-link">Login Here</a></p>
      </form>
      <p v-if="message">{{ message }}</p>
    </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'SignupPage',
    data() {
      return {
        username: '',
        email: '',
        password: '',
        message: '', 
      };
    },
    methods: {
      handleSignup() {
        this.message = `Welcome, ${this.username}! You have successfully signed up.`;
        this.username = '';
        this.email = '';
        this.password = '';
      },
    },
  };
  </script>
  
  <style scoped>
  .signup-container {
    font-family: 'Roboto', sans-serif;
    max-width: 300px;
    width: 100%;
    margin: 0 auto;
    padding: 5em;
    border: 1px solid #a59696;
    border-radius: 5px;
    background: linear-gradient(135deg, #a3e5b0, #56ab2f);
    align-items: center;
    color: #f8faf8;
  }
  h2 {
    text-align: center;
  }
  .form-group {
    margin-bottom: 1em;
  }
  label {
    display: block;
    margin-bottom: 0.5em;
  }
  input {
    width: 100%;
    padding: 0.5em;
    border: 1px solid #ccc;
    border-radius: 4px;
    background: #f8faf8;
  }
  button {
    width: 100%;
    padding: 0.75em;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  button:hover {
    background-color: #619863;
  }
  p {
    text-align: center;
    margin-top: 1em;
    color: #f8faf8;
  }
  </style>
  