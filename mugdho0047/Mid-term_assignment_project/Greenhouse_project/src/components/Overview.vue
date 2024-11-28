<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const overviewData = ref([]);

onMounted(() => {
    const user = localStorage.getItem("user");
    if (!user) {
        router.push({ name: 'Login' });
    }
});

const logout = async () => {
    localStorage.removeItem("user");
    router.push({ name: 'Login' });
};

const fetchOverviewData = async () => {
    try {
        const response = await fetch('../../DB/Data.json');
        overviewData.value = await response.json();
    } catch (error) {
        console.error('Error fetching overview data:', error);
    }
};

onMounted(fetchOverviewData);
</script>

<template>
  <div id="overview">
    <!-- Abstract Background -->
    <div class="abstract-background"></div>
    
    <!-- Navbar -->
    <nav class="navbar">
      <div class="logo">Greenhouse Dashboard</div>
      <ul class="nav-links">
        <li><router-link to="/dashboard">Home</router-link></li>
        <li><router-link to="/over-view">Overview</router-link></li>
        <li><router-link to="/settings">Settings</router-link></li>
        <li><router-link to="/historical-data-chart">Logs</router-link></li>
        <li><a @click="logout">Logout</a></li>
      </ul>
    </nav>

    <!-- Main Content -->
    <main>
      <!-- Header -->
      <header>
        <h1>Overview</h1>
        <p>Summary of Greenhouse Performance</p>
      </header>

      <!-- Parameters Description -->
      <section class="parameters-description">
        <p>
          Our dashboard provides an intuitive, real-time summary of greenhouse conditions. By monitoring key metrics like temperature, humidity, soil moisture, and light levels, we empower farmers and greenhouse managers to effectively manage the environment for optimal crop growth. Below is an overview of each parameter and its significance:
        </p>
        <ul>
          <li><strong>Temperature:</strong> Essential for optimal plant growth, temperature is displayed in real time, allowing users to maintain ideal levels and adjust as needed.</li>
          <li><strong>Humidity:</strong> Appropriate humidity levels support plant health and productivity. Our system continuously tracks changes, alerting users to any fluctuations that may impact crop quality.</li>
          <li><strong>Soil Moisture:</strong> A key factor for plant hydration and nutrient absorption, soil moisture monitoring helps users ensure adequate watering without overwatering.</li>
          <li><strong>Light Level:</strong> As plants rely on light for photosynthesis, our dashboard tracks light exposure, helping users adjust artificial lighting for maximum yield and efficiency.</li>
        </ul>
      </section>

      <!-- Overview Metrics -->
      <section class="overview-metrics">
        <div 
          v-for="(data, index) in overviewData" 
          :key="index" 
          class="card"
        >
          <div class="card-icon" :style="{ backgroundColor: data.color + '20' }">
            <span :style="{ color: data.color }">📊</span>
          </div>
          <div class="card-content">
            <h2>{{ data.title }}</h2>
            <p class="overview-value">{{ data.value }}</p>
            <p class="overview-label">{{ data.description }}</p>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<style scoped>
/* General Styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Roboto', sans-serif;
  background: #f4f7fa;
  color: #333;
}

/* Abstract Background */
.abstract-background {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #ff8a00, #e52e71, #8921aa);
  z-index: -1;
}

.abstract-background::before,
.abstract-background::after {
  content: '';
  position: absolute;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 50%;
  pointer-events: none;
}

.abstract-background::before {
  width: 400px;
  height: 400px;
  top: -50px;
  left: -100px;
}

.abstract-background::after {
  width: 300px;
  height: 300px;
  bottom: -50px;
  right: -100px;
}

/* Navbar */
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background: rgba(255, 255, 255, 0.9);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  z-index: 100;
}

.nav-links {
  list-style: none;
  display: flex;
  gap: 1.5rem;
}

.nav-links li a {
  text-decoration: none;
  font-size: 1rem;
  color: #333;
  transition: color 0.3s ease;
}

.nav-links li a:hover {
  color: #e52e71;
}

/* Main Content */
main {
  padding: 2rem 3rem;
  margin-top: 80px;
  color: #fff;
}

header h1 {
  font-size: 2.5rem;
  font-weight: bold;
  color: #ffffff;
}

header p {
  font-size: 1rem;
  font-weight: 300;
  color: rgba(255, 255, 255, 0.7);
}

/* Parameters Description */
.parameters-description {
  font-size: 1rem;
  color: #333;
  background-color: #ffffff;
  padding: 1.5rem;
  border-radius: 8px;
  margin-top: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
}

.parameters-description ul {
  margin-top: 10px;
  padding-left: 1.2rem;
}

.parameters-description li {
  margin-bottom: 10px;
}

/* Overview Metrics */
.overview-metrics {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
  margin-top: 30px;
}

.card {
  background: linear-gradient(135deg, #ffffff, #f9f9fb);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15);
  border-radius: 15px;
  display: flex;
  align-items: center;
  padding: 1.5rem;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
  transform: translateY(-10px);
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.2);
}

.card-icon {
  width: 70px;
  height: 70px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  margin-right: 1.5rem;
}

.card-content h2 {
  font-size: 1.5rem;
  color: #333;
}

.overview-value {
  font-size: 2rem;
  font-weight: 700;
  color: #2c3e50;
}

.overview-label {
  font-size: 0.9rem;
  color: #95a5a6;
}
</style>