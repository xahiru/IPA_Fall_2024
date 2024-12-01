<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import { useRouter } from 'vue-router';
import SimpleLineChart from './SimpleLineChart.vue';

const router = useRouter();
const metrics = ref([]);
const temperatureHistory = ref([]);
const humidityHistory = ref([]);
const lastUpdated = ref('');
const intervalId = ref(null);

const fetchData = async () => {
  try {
    const response = await fetch('../../Data/data.json');
    metrics.value = await response.json();
    temperatureHistory.value.push(parseFloat(metrics.value[0]?.value || 0));
    humidityHistory.value.push(parseFloat(metrics.value[1]?.value || 0));
    if (temperatureHistory.value.length > 5) temperatureHistory.value.shift();
    if (humidityHistory.value.length > 5) humidityHistory.value.shift();
    const now = new Date();
    lastUpdated.value = now.toLocaleTimeString();
  } catch (error) {
    console.error('Error fetching data:', error);
  }
};

const generateRandomValue = (min, max, unit = '') => {
  return `${(Math.random() * (max - min) + min).toFixed(1)}${unit}`;
};

const updateMetrics = () => {
  metrics.value = [
    { ...metrics.value[0], value: generateRandomValue(15, 16, '°C') },
    { ...metrics.value[1], value: generateRandomValue(67, 68, '%') },
    { ...metrics.value[2], value: generateRandomValue(45, 45.5, '%') },
    { ...metrics.value[3], value: generateRandomValue(300, 312, ' lux') },
  ];
};

const logout = () => {
  localStorage.removeItem('user');
  router.push({ name: 'Login' });
};

onMounted(async () => {
  const user = localStorage.getItem('user');
  if (!user) {
    router.push({ name: 'Login' });
    return;
  }
  await fetchData();
  intervalId.value = setInterval(() => {
    updateMetrics();
    fetchData();
  }, 3000);
});

onUnmounted(() => {
  clearInterval(intervalId.value);
});
</script>

<template>
  <div id="dashboard">
    <nav class="navbar">
      <div class="logo">Greenhouse</div>
      <ul class="nav-links">
        <li><router-link to="/dashboard">Home</router-link></li>
        <li><router-link to="/over-view">Overview</router-link></li>
        <li><router-link to="/settings">Settings</router-link></li>
        <li><a @click="logout">Logout</a></li>
      </ul>
    </nav>

    <main>
      <header>
        <h1>Dashboard</h1>
        <p>Real-time Monitoring of Greenhouse Conditions</p>
      </header>

      <section class="metrics">
        <div
          v-for="(metric, index) in metrics"
          :key="index"
          class="card"
          :style="{ borderLeft: `5px solid ${metric.color}` }"
        >
          <h2>{{ metric.title }}</h2>
          <p>{{ metric.value }}</p>
        </div>
      </section>

      <section class="charts-section">
        <div class="chart-card">
          <h3>Temperature History</h3>
          <SimpleLineChart label="Temperature (°C)" :data="temperatureHistory" />
        </div>
        <div class="chart-card">
          <h3>Humidity History</h3>
          <SimpleLineChart label="Humidity (%)" :data="humidityHistory" />
        </div>
      </section>

      <div class="update-info">Last Updated: {{ lastUpdated }}</div>
    </main>
  </div>
</template>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #2e7d32;
  padding: 10px 20px;
  color: white;
}

.navbar .logo {
  font-size: 1.5rem;
  font-weight: bold;
}

.navbar .nav-links {
  display: flex;
  list-style: none;
  gap: 20px;
}

.navbar .nav-links li a {
  color: white;
  text-decoration: none;
  font-weight: bold;
  padding: 5px 10px;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}

.navbar .nav-links li a:hover {
  background-color: #1b5e20;
}

header {
  text-align: center;
  padding: 20px 10px;
}

header h1 {
  font-size: 2rem;
  color: #2e7d32;
}

header p {
  font-size: 1rem;
  color: #555;
}

.metrics {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  max-width: 1200px;
  margin: 20px auto;
  padding: 0 15px;
}

.card {
  background-color: white;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  padding: 20px;
  transition: transform 0.2s ease;
  position: relative;
}

.card:hover {
  transform: scale(1.02);
}

.card h2 {
  color: #2e7d32;
  font-size: 1.5rem;
}

.card p {
  font-size: 1.2rem;
  font-weight: bold;
}

.charts-section {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
  padding: 20px;
  margin-top: 30px;
}

.chart-card {
  background: radial-gradient(circle, #ffffff, #f1f8e9);
  border: 2px solid #c5e1a5;
  border-radius: 20px;
  padding: 15px;
  box-shadow: 0 6px 10px rgba(0, 0, 0, 0.2);
  transition: transform 0.2s ease-in-out, box-shadow 0.3s ease;
}

.chart-card:hover {
  transform: scale(1.05);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
}

.chart-card h3 {
  font-size: 1.3rem;
  color: #558b2f;
  text-align: center;
  margin-bottom: 15px;
  font-weight: bold;
}

.chart-card canvas {
  display: block;
  margin: 0 auto;
  max-width: 100%;
  height: auto;
  border-radius: 10px;
  border: 1px solid #c5e1a5;
  background-color: #ffffff;
}

@media (max-width: 768px) {
  .charts-section {
    grid-template-columns: 1fr;
    gap: 15px;
  }

  .chart-card {
    width: 100%;
  }
}


.update-info {
  text-align: center;
  margin-top: 10px;
  font-size: 0.9rem;
  color: #555;
}
</style>