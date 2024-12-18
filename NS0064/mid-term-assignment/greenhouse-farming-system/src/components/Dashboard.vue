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
        <li><router-link to="/overview">Overview</router-link></li>
        <li><router-link to="/settings">Settings</router-link></li>
        <li><router-link to="/charts">Charts</router-link></li>
        <li><a @click="logout">Logout</a></li>
      </ul>
    </nav>
  
      <!-- Main Content -->
      <main>
        <header>
          <h1>Dashboard</h1>
          <p>Real-time Monitoring of Greenhouse Conditions</p>
        </header>
  
        <!-- Metrics Section -->
        <section class="metrics">
          <div 
          v-for="(data, index) in data" 
          :key="index" 
          class="card" 
          :style="{ borderLeft: `5px solid ${data.color}` }"
        >
          <h2>{{ data.title }}</h2>
          <p>{{ data.value }}</p>
        </div>
        </section>
      </main>
    </div>
</template>

<script setup>
import { ref,onMounted } from 'vue';
import { useRoute } from 'vue-router';

const router= useRoute();
const data = ref([]);
const menuActive = ref(false);
  
  const toggleMenu = () => {
    menuActive.value = !menuActive.value;
  };
  
  const logout = async () => {
    localStorage.removeItem("user");
    window.location.href = '/login';
  };
const getData = async () => {
  try {
    const result = await fetch('../../Database/data.json'); 
    data.value = await result.json();
  } catch (error) {
    console.error('Errors :', error);
  }
};

onMounted(getData);



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
  a:hover{
    cursor: pointer;
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

main {
  padding: 2rem;
  margin-top: 80px;
  flex: 1;
}

header h1 {
  font-size: 2.2rem;
  font-weight: bold;
  color: #34495e;
}

header p {
  font-size: 1rem;
  color: #666666;
  margin-top: 0.5rem;
}

.metrics {
  display: grid;
  gap: 1.5rem;
  margin-top: 1.5rem;
}

@media (min-width: 1024px) {
  .metrics {
    grid-template-columns: repeat(4, 1fr);
  }
}

@media (min-width: 768px) and (max-width: 1023px) {
  .metrics {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 767px) {
  .metrics {
    grid-template-columns: 1fr;
  }
}

.card {
  background: #ffffff;
  border-radius: 8px;
  padding: 1.5rem;
  text-align: center;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
}

.card-icon {
  font-size: 2rem;
  color: #007acc;
  margin-bottom: 0.5rem;
}

.card h2 {
  font-size: 1.4rem;
  color: #333333;
  margin-bottom: 0.5rem;
}

.card p {
  font-size: 1.8rem;
  font-weight: bold;
  color: #333333;
}

.temperature-card .card-icon {
  color: #e74c3c;
}

.humidity-card .card-icon {
  color: #3498db;
}

.moisture-card .card-icon {
  color: #16a085;
}

.light-card .card-icon {
  color: #f39c12;
}
</style>
