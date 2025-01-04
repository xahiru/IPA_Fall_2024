<template>
    <div>
      <h2>Login</h2>
 
      <form @submit.prevent="handleSubmit">
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
        submittedUsername: null
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

  form {
    max-width: 300px;
    margin: 0 auto;
  }
  input {
    width: 100%;
    padding: 8px;
    margin: 8px 0;
  }
  button {
    padding: 10px 15px;
    background-color: #007BFF;
    color: white;
    border: none;
    cursor: pointer;
  }
  button:hover {
    background-color: #0056b3;
  }
  </style>
  