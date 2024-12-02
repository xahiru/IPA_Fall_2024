<template>
    <div class="login-form">
      <h2>Login</h2>
      <form @submit.prevent="handleSubmit">
        <div>
          <label for="username">Username:</label>
          <input type="text" id="username" v-model="username" required />
        </div>
        <div>
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="password" required />
        </div>
        <button type="submit">Submit</button>
      </form>
      <p v-if="submittedUsername">Welcome, {{ submittedUsername }}!</p >
    </div>
  </template>
  
  <script>
  export default {
    name: 'LoginForm',
    data() {
      return {
        username: '',
        password: '',
        submittedUsername: '',
      };
    },
    methods: {
      handleSubmit() {
        // Prevent default submission and display an alert
        alert(`Entered Username: ${this.username}`);
        // Set the submitted username to display the welcome message
        this.submittedUsername = this.username;
        // Optional: Clear the form inputs after submission
        this.username = '';
        this.password = '';
      },
    },
  };
  </script>
  
  <style scoped>
  .login-form {
    max-width: 300px;
    margin: auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  .login-form h2 {
    text-align: center;
  }
  
  .login-form label {
    display: block;
    margin: 10px 0 5px;
  }
  
  .login-form input {
    width: 100%;
    padding: 8px;
    margin-bottom: 10px;
  }
  
  .login-form button {
    width: 100%;
    padding: 10px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .login-form button:hover {
    background-color: #218838;
  }
  </style>