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
      
      <p v-if="submittedUsername">Welcome, {{ submittedUsername }}!</p>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: '',
        password: '',
        submittedUsername: ''
      };
    },
    methods: {
      handleSubmit() {
        this.submittedUsername = this.username;
        alert(`Welcome, ${this.username}!`);
      }
    }
  };
  </script>
  
  <style scoped>
  .login-form {
    max-width: 300px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
  }
  
  h2 {
    text-align: center;
  }
  
  form {
    display: flex;
    flex-direction: column;
  }
  
  div {
    margin-bottom: 10px;
  }
  
  label {
    font-weight: bold;
  }
  
  input {
    padding: 8px;
    font-size: 1rem;
    width: 100%;
    box-sizing: border-box;
  }
  
  button {
    padding: 10px;
    background-color: #473fae;
    color: white;
    border: none;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #160946;
  }
  
  p {
    text-align: center;
    margin-top: 10px;
    font-size: 1rem;
    color: #333;
  }
  </style>  