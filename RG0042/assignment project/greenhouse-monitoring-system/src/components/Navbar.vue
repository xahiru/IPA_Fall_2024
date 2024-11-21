<template>
    <nav class="navbar">
      <router-link to="/" class="logo">Greenhouse Dashboard</router-link>
      <div class="nav-links">
        <router-link to="/overview">Overview</router-link>
        <router-link to="/settingspanel">Settings</router-link>
        <router-link to="/logs">Logs</router-link>
        <router-link to="/login">Logout</router-link>
      </div>
    </nav>
  </template>
  
  <script>
  export default {
    name: "Navbar",
  
    methods: {
      logout() {
        localStorage.removeItem('isAuthenticated'); // Remove the auth flag
        this.$router.push('/login'); // Redirect to login page
      }
    }
  };
  </script>
  
  <style scoped>
  .navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem;
    background-color: #3b82f6;
    color: white;
  }
  
  .logo {
    font-size: 1.5rem;
    font-weight: bold;
    color: white;
    text-decoration: none;
  }
  
  .nav-links a {
    margin: 0 1rem;
    color: white;
    text-decoration: none;
  }
  
  .nav-links a:hover {
    text-decoration: underline;
  }
  </style>