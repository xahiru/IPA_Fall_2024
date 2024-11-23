<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const isMenuOpen = ref(false); // State to track menu visibility

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value;
};

const logout = async () => {
  localStorage.removeItem("user");
  window.location.href = '/login';
};
</script>

<template>
  <nav class="navbar">
    <div class="navbar-content">
      <div class="logo">Greenhouse</div>
      <!-- Hamburger menu for mobile -->
      <button class="hamburger" @click="toggleMenu">
        <span class="bar"></span>
        <span class="bar"></span>
        <span class="bar"></span>
      </button>
      <ul :class="['nav-links', { 'show': isMenuOpen }]">
        <li><router-link to="/" @click="isMenuOpen = false">Home</router-link></li>
        <li><router-link to="/dashboard" @click="isMenuOpen = false">Dashboard</router-link></li>
        <li><router-link to="/over-view" @click="isMenuOpen = false">Overview</router-link></li>
        <li><router-link to="/settings" @click="isMenuOpen = false">Settings</router-link></li>
        <li><router-link to="/historical-data-chart" @click="isMenuOpen = false">Logs</router-link></li>
        <li><a @click="logout">Logout</a></li>
      </ul>
    </div>
  </nav>
</template>

<style scoped>
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 1.2rem 2rem;
  background: #2d3e50;
  color: white;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  z-index: 100;
}
a:hover{
    cursor: pointer;
}
.navbar-content {
  width: 100%;
  max-width: 1200px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  font-size: 1.8rem;
  font-weight: bold;
  letter-spacing: 1px;
}

.nav-links {
  list-style: none;
  display: flex;
  gap: 30px;
  transition: all 0.3s ease-in-out;
}

.nav-links li a {
  text-decoration: none;
  color: white;
  font-size: 1.1rem;
  font-weight: 500;
  transition: color 0.3s ease;
}

.nav-links li a:hover {
  color: #3498db;
}

/* Hamburger menu styles */
.hamburger {
  display: none;
  flex-direction: column;
  gap: 5px;
  background: none;
  border: none;
  cursor: pointer;
}

.hamburger .bar {
  width: 25px;
  height: 3px;
  background: white;
  border-radius: 2px;
}

/* Responsive styles */
@media (max-width: 768px) {
  .hamburger {
    display: flex;
  }

  .nav-links {
    position: absolute;
    top: 100%;
    left: 0;
    width: 100%;
    flex-direction: column;
    gap: 15px;
    background: #2d3e50;
    text-align: center;
    transform: translateY(-200%);
    opacity: 0;
    pointer-events: none;
  }

  .nav-links.show {
    transform: translateY(0);
    opacity: 1;
    pointer-events: all;
  }

  .nav-links li a {
    font-size: 1rem;
  }

  .logo {
    font-size: 1.5rem;
  }
}

@media (max-width: 480px) {
  .logo {
    font-size: 1.2rem;
  }

  .nav-links li a {
    font-size: 0.9rem;
  }

  .hamburger .bar {
    width: 20px;
  }
}
</style>
