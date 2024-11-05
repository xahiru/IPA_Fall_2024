<template>
    <div class="login-form">
      <h2>Login</h2>
      <form @submit.prevent="handleSubmit">
        <div>
          <label for="username">Username:</label>
          <input type="text" id="username" v-model="username" />
        </div>
        <div>
          <label for="passworgit d">Password:</label>
          <input type="password" id="password" v-model="password" />
        </div>
        <button type="submit">Submit</button>
      </form>
  
      <div v-if="submittedUsername">
        <p>Welcome, {{ submittedUsername }}!</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: '',
        password: '',
        submittedUsername: null
      };
    },
    methods: {
      handleSubmit() {

        alert(`Username: ${this.username}`);
        this.submittedUsername = this.username;
      }
    }
  };
  </script>
  
  <style scoped>
  .login-form {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  h2 {
    text-align: center;
  }
  
  div {
    margin-bottom: 15px;
  }
  
  label {
    display: block;
  }
  
  input {
    width: 100%;
    padding: 8px;
    margin-top: 5px;
    box-sizing: border-box;
  }
  
  button {
    width: 100%;
    padding: 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #45a049;
  }
  </style>  