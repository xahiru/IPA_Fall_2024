<template>
    <nav class="navbar">
      <ul class="navbar-links">
        <li><router-link to="/" class="navbar-link">Home</router-link></li>
        <li><router-link to="/login" class="navbar-link">Login</router-link></li>
        <li><router-link to="/signup" class="navbar-link">Signup</router-link></li>
        <li><router-link to="/about" class="navbar-link">About</router-link></li>
        <li><router-link to="/dashboard" class="navbar-link">DashBoard</router-link></li>
      </ul>
    </nav>
  </template>
  
  <script>
  export default {};
  </script>
  
  <style scoped>
  .navbar {
    background-color: #007bff;
    padding: 1rem;
    color: white;
  }
  
  .navbar-links {
    list-style: none;
    display: flex;
    justify-content: center;
    margin: 0;
    padding: 0;
  }
  
  .navbar-links li {
    margin: 0 0.8rem;
  }
  
  .navbar-link {
    color: white;
    text-decoration: none;
    font-size: 1.1rem;
  }
  
  .navbar-link:hover {
    text-decoration: underline;
  }
  </style>
  