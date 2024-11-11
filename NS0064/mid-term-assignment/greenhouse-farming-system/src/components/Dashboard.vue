<template>
    <div id="dashboard">
      <!-- Navbar -->
      <nav class="navbar">
        <div class="logo">Greenhouse</div>
        <ul class="nav-links">
          <li><router-link to="/overview">Overview</router-link></li>
          <li><router-link to="/settings">Settings</router-link></li>
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
          <!-- Looping through the cards data with v-for -->
          <div 
            v-for="(card, index) in cards" 
            :key="index" 
            :class="['card', card.class]"
          >
            <div class="card-icon">
              <i :class="card.icon"></i>
            </div>
            <h2>{{ card.title }}</h2>
            <p>{{ card.value }}</p>
          </div>
        </section>
      </main>
    </div>
</template>

<script setup>
import { ref } from 'vue';
const cards = ref([
  {
    title: 'Temperature',
    value: '24°C',
    icon: 'fas fa-thermometer-half',
    class: 'temperature-card'
  },
  {
    title: 'Humidity',
    value: '65%',
    icon: 'fas fa-tint',
    class: 'humidity-card'
  },
  {
    title: 'Soil Moisture',
    value: '45%',
    icon: 'fas fa-water',
    class: 'moisture-card'
  },
  {
    title: 'Light Level',
    value: '300 lux',
    icon: 'fas fa-sun',
    class: 'light-card'
  }
]);

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
  background: #f5f5f7;
  color: #333;
}
a:hover{
  cursor: pointer;
}
#dashboard {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background-color: #003366;
  color: #ffffff;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 100;
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
}

.nav-links {
  list-style: none;
  display: flex;
  gap: 1.5rem;
}

.nav-links a {
  color: #ffffff;
  text-decoration: none;
  font-weight: 500;
}

.nav-links a:hover {
  color: #00aaff;
}

main {
  padding: 2rem;
  margin-top: 80px;
  flex: 1;
}

header h1 {
  font-size: 2.2rem;
  font-weight: bold;
  color: #003366;
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
