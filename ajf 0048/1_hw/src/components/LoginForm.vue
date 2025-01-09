<template>
    <div class="login-form">
      <form @submit.prevent="handleSubmit">
        <div class="form-group">
          <label for="username">Username:</label>
          <input 
            type="text" 
            id="username"
            v-model="username"
            required
          >
        </div>
  
        <div class="form-group">
          <label for="password">Password:</label>
          <input 
            type="password" 
            id="password"
            v-model="password"
            required
          >
        </div>
  
        <button type="submit">Login</button>
      </form>
  
      <div v-if="submittedUsername" class="welcome-message">
        Welcome, {{ submittedUsername }}!
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'LoginForm',
    data() {
      return {
        username: '',
        password: '',
        submittedUsername: ''
      }
    },
    methods: {
      handleSubmit() {
        alert(`Username submitted: ${this.username}`)
        this.submittedUsername = this.username
      }
    }
  }
  </script>
  
  <style scoped>
  .login-form {
    max-width: 300px;
    margin: 0 auto;
    padding: 20px;
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  label {
    display: block;
    margin-bottom: 5px;
  }
  
  input {
    width: 100%;
    padding: 8px;
    border: 1px solid #ddd;
    border-radius: 4px;
  }
  
  button {
    background-color: #4CAF50;
    color: white;
    padding: 10px 15px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #45a049;
  }
  
  .welcome-message {
    margin-top: 20px;
    color: #4CAF50;
    text-align: center;
  }
  </style>