<template>
    <div class="login-form-container">
      <div class="login-form">
        <h2>Login</h2>
        <form @submit.prevent="handleSubmit">
          <div class="form-group">
            <label for="username">Username</label>
            <input
              type="text"
              id="username"
              v-model="username"
              required
              placeholder="Enter your username"
            />
          </div>
          <div class="form-group">
            <label for="password">Password</label>
            <input
              type="password"
              id="password"
              v-model="password"
              required
              placeholder="Enter your password"
            />
          </div>
          <button type="submit">Login</button>
        </form>
        <div v-if="welcomeMessage" class="welcome-message">
          {{ welcomeMessage }}
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: '',
        password: '',
        welcomeMessage: ''
      };
    },
    methods: {
      handleSubmit() {
        this.welcomeMessage = `Welcome, ${this.username}!`;
  
        if (Notification.permission === "granted") {
          new Notification(`Welcome, ${this.username}!`);
        } else if (Notification.permission !== "denied") {
          Notification.requestPermission().then((permission) => {
            if (permission === "granted") {
              new Notification(`Welcome, ${this.username}!`);
            }
          });
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .login-form-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }
  
  .login-form {
    background: #f7f1f1;
    padding: 30px 30px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    text-align: center;
    width: 100%;
    max-width: 350px;
    box-sizing: border-box;
  }
  
  h2 {
    margin-bottom: 20px;
    color: #333;
  }
  
  .form-group {
    margin-bottom: 15px;
    text-align: left;
  }
  
  label {
    display: block;
    font-weight: bold;
    margin-bottom: 5px;
    color: #555;
  }
  
  input[type="text"],
  input[type="password"] {
    width: 100%;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
    box-sizing: border-box;
  }
  
  input[type="text"]:focus,
  input[type="password"]:focus {
    border-color: #031321;
    outline: none;
  }
  
  button {
    background-color: #6fcf4f;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
    width: 100%;
  }
  
  button:hover {
    background-color: #d46161;
  }
  
  .welcome-message {
    margin-top: 20px;
    color: green;
    font-weight: bold;
  }
  </style>
  