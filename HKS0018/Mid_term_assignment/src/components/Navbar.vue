<template>
    <nav class="navbar">
      <div class="logo">Greenhouse Farming System</div>
      <ul class="nav-links">
        <li><router-link to="/dashboard" class="link">Home</router-link></li>
        <li><router-link to="/over-view" class="link">Overview</router-link></li>
        <li><router-link to="/settings" class="link">Settings</router-link></li>
        <li><router-link to="/logs" class="link">Logs</router-link></li>
        <li><a @click="logout" class="link">Logout</a></li>
      </ul>
    </nav>
  </template>
  
  <script>
  export default {
    methods: {
      logout() {
        localStorage.clear();
        this.$router.push('/');
      },
    },
  };
  </script>
  
  <style scoped>
  * {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.dashboard-layout {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #1e1e2f;
  color: #e0e0e0;
  padding: 1rem 2rem;
  position: fixed;
  width: 100%;
  top: 0;
  z-index: 10;
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
  color: #00e676;
}

.nav-links {
  list-style: none;
  display: flex;
  gap: 1.5rem;
}

.link {
  text-decoration: none;
  color: #e0e0e0;
  font-size: 1.1rem;
  transition: color 0.3s ease;
}

.link:hover {
  color: #00e676;
}
  </style>
  