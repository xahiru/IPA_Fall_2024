<template>
  <div id="dashboard">
    <!-- Navbar -->
    <nav class="navbar">
      <div class="logo">Greenhouse</div>
      
      <!-- Hamburger Icon for mobile -->
      <div class="hamburger" @click="toggleMenu">
        <span class="bar"></span>
        <span class="bar"></span>
        <span class="bar"></span>
      </div>
      
      <!-- Navbar Links -->
      <ul class="nav-links" :class="{'active': menuActive}">
        <li><router-link to="/">Home</router-link></li>
        <li><router-link to="/dashboard">Dashboard</router-link></li>
        <li><router-link to="/over-view">Overview</router-link></li>
        <li><router-link to="/settings">Settings</router-link></li>
        <li><router-link to="/historical-data-chart">Charts</router-link></li>
        <li><a @click="logout">Logout</a></li>
      </ul>
    </nav>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const menuActive = ref(false);

const toggleMenu = () => {
  menuActive.value = !menuActive.value;
};

const logout = async () => {
  localStorage.removeItem("user");
  window.location.href = '/login';
};
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Roboto', sans-serif;
  background: #f4f6f9;
  color: #333;
  padding-top: 70px;
}

.navbar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.2rem 2rem;
  background: #2d3e50;
  color: white;
  z-index: 100;
  transition: all 0.3s ease; /* Add smooth transition */
}

.logo {
  font-size: 1.8rem;
  font-weight: bold;
}

.nav-links {
  list-style: none;
  display: flex;
  gap: 30px;
}

.nav-links a {
  color: #ffffff;
  text-decoration: none;
  font-size: 1.1rem;
}

.hamburger {
  display: none;
  flex-direction: column;
  gap: 5px;
  cursor: pointer;
}

.hamburger .bar {
  width: 25px;
  height: 4px;
  background-color: white;
  border-radius: 5px;
}

@media (max-width: 768px) {
  .nav-links {
    display: none;
    width: 100%;
    flex-direction: column;
    gap: 1rem;
    position: absolute;
    top: 70px;
    left: 0;
    background-color: #2d3e50;
    padding: 1rem 0;
    z-index: -1; /* Fix issue where links appear behind navbar */
  }

  .nav-links.active {
    display: flex;
    z-index: 9999; /* Ensure the links show above other elements */
  }

  .hamburger {
    display: flex;
  }

  .nav-links li {
    width: 100%;
  }

  .nav-links a {
    padding: 0.5rem 1rem;
    font-size: 1.2rem;
  }
}
</style>
