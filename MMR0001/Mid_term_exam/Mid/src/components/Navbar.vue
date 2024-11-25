<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const isMenuOpen = ref(false); 

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
     
      <button class="phone" @click="toggleMenu">
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
  background-color: #2b580c; 
  padding: 10px 20px;
  color: white;
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: relative;
  z-index: 1000;
}

.navbar-content {
  display: flex;
  align-items: center;
  width: 100%;
  justify-content: space-between;
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
}

.nav-links {
  display: flex;
  list-style: none;
  gap: 20px;
  margin: 0;
  padding: 0;
}

.nav-links li {
  display: inline-block;
}

.nav-links a {
  text-decoration: none;
  color: white;
  font-size: 1rem;
  transition: color 0.3s;
}

.nav-links a:hover {
  color: #a3d9a5; 
}

.phone {
  display: none;
  flex-direction: column;
  justify-content: space-around;
  height: 24px;
  width: 30px;
  background: none;
  border: none;
  cursor: pointer;
}

.phone .bar {
  width: 100%;
  height: 3px;
  background-color: white;
  border-radius: 2px;
  transition: 0.3s ease-in-out;
}

@media (max-width: 768px) {
  .phone {
    display: flex;
  }

  .nav-links {
    display: none;
    position: absolute;
    top: 60px;
    right: 0;
    background-color: #2b580c;
    flex-direction: column;
    gap: 10px;
    padding: 20px;
    border-radius: 0 0 10px 10px;
    width: 100%;
  }

  .nav-links.show {
    display: flex;
  }

  .nav-links li {
    text-align: center;
    width: 100%;
  }
}
</style>
