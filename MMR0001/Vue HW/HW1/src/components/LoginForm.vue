<template>
    <div>
      <h1>Login Page</h1>
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
      <div v-if="submittedUsername">
        <p>Welcome, {{ submittedUsername }}!</p>
      </div>

      <router-link to="/expression-demo">Go to ExpressionDemo</router-link>

      <router-link  to="/event-demo">Go to EventDemo</router-link>
      
      <router-link to="/toggle-visibility">Go to ToggleVisibility</router-link>
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
        alert(`Submitted Username: ${this.username}`); 
      }
    }
  };
  </script>
  
  <style scoped>
  </style>  