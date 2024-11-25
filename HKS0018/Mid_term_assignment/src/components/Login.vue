<template>
    <div>
      <h1>Login Page</h1>
      <form @submit.prevent="handleLogin">
        <div>
          <label for="username">Username:</label>
          <input
            type="text"
            id="username"
            v-model="username"
            placeholder="Enter your username"
            required
          />
        </div>
        
        <div>
          <label for="password">Password:</label>
          <input
            type="password"
            id="password"
            v-model="password"
            placeholder="Enter your password"
            required
          />
        </div>
  
        <button type="submit">Login</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: "Login",
    data() {
      return {
        username: "",
        password: "",
      };
    },
    methods: {
      handleLogin() {
        
        if (this.username && this.password) {
          alert(`Logging in with Username: ${this.username} and Password: ${this.password}`);

          this.username = "";
          this.password = "";
        } else {
          alert("Please fill in all fields.");
        }
      },
    },
  };
  </script>
  
  <style>

  form {
    background-color: #369970;
    display: flex;
    flex-direction: column;
    width: 300px;
    margin: 20px auto;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 5px;
  }
  label {
    margin-top: 10px;
    font-weight: bold;
  }
  input {
    margin: 5px 0 15px;
    padding: 8px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  button {
    padding: 10px;
    background-color: #42b983;
    color: white;
    font-weight: bold;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  button:hover {
    background-color: #369970;
  }
  </style>
  