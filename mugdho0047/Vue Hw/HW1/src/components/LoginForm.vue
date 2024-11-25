<template>
    <div>
      <form @submit.prevent="handleSubmit">
        <div>
          <label for="username">Username:</label>
          <input v-model="username" type="text" id="username" required />
        </div>
  
        <div>
          <label for="password">Password:</label>
          <input v-model="password" type="password" id="password" required />
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
        submittedUsername: ''
      };
    },
    methods: {
      handleSubmit() {
        // Prevent default form submission and display the entered username
        this.submittedUsername = this.username;
        alert(`Welcome, ${this.username}!`);
      }
    }
  };
  </script>
  
  <style scoped>
  /* Add any additional styles for the form here */
  form {
    max-width: 300px;
    margin: auto;
    padding: 1em;
    border: 1px solid #ccc;
    border-radius: 8px;
  }
  
  label {
    display: block;
    margin-bottom: 5px;
  }
  
  input {
    width: 100%;
    padding: 0.5em;
    margin-bottom: 1em;
  }
  
  button {
    width: 100%;
    padding: 0.5em;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #0056b3;
  }
  </style>  