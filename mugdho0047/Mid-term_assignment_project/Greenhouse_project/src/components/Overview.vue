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
    <div class="abstract-background"></div>
    
    <nav class="navbar">
      <div class="logo">Greenhouse</div>
      <ul class="nav-links">
        <li><router-link to="/dashboard">Home</router-link></li>
        <li><router-link to="/over-view">Overview</router-link></li>
        <li><router-link to="/settings">Settings</router-link></li>
        <li><router-link to="/historical-data-chart">Logs</router-link></li>
        <li><a @click="logout">Logout</a></li>
      </ul>
    </nav>

    <main>
      <header>
        <h1>Overview</h1>
        <p>Summary of Greenhouse Performance</p>
      </header>

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
    </main>
  </div>
</template>
<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.dashboard {
  position: relative;
  background-color: #f4f7fc;
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
}

.navbar {
  position: fixed;
  top: 0;
  left: 0;
  height: 10%;
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.2rem 2rem;
  background-color: #34495e;
  color: #ffffff;
  border-bottom: 1px solid #2c3e50;
  box-shadow: 0 3px 5px rgba(0, 0, 0, 0.1);
  z-index: 100;
}

.logo {
  font-size: 2rem;
  font-weight: bold;
  color: #ffffff;
}

.nav-links {
  list-style: none;
  display: flex;
  gap: 20px;
}

.nav-links li a {
  text-decoration: none;
  color: #ecf0f1;
  font-size: 1rem;
  transition: color 0.3s ease;
}

.nav-links li a:hover {
  color: #1abc9c;
}

header h1 {
  font-size: 2.5rem;
  font-weight: bold;
  color: #032142;
}

header p {
  font-size: 1rem;
  font-weight: 300;
  color: rgba(255, 255, 255, 0.777);
}

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
</style>