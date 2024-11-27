<template>
  <div class="dashboard-layout">
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

    <main class="dashboard">
      <header>
        <h1>Dashboard</h1>
        <p>Real-time update</p>
      </header>

      <div class="metrics-grid">
        <div 
          class="metric-card" 
          v-for="metric in metrics" 
          :key="metric.name"
        >
          <h3>{{ metric.icon }} {{ metric.name }}</h3>
          <div class="metric-value">{{ metric.value }}</div>
          <div 
            class="status" 
            :class="getStatusClass(metric)"
          >
            {{ getStatus(metric) }}
          </div>
        </div>
      </div>

      <div class="charts-section">
        <ChartHistory 
          title="Temperature Chart History" 
          :label="'Temperature (°C)'" 
          :data="temperatureHistory" 
        />
        <ChartHistory 
          title="Humidity Chart History" 
          :label="'Humidity (%)'" 
          :data="humidityHistory" 
        />
      </div>

      <div class="update-info">Last Updated: {{ lastUpdated }}</div>
    </main>
  </div>
</template>

<script>
import { generateMockData } from '../../db/mockData';
import ChartHistory from './charts/ChartHistory.vue';

export default {
  components: { ChartHistory },
  data() {
    return {
      metrics: [
        { name: 'Temperature', icon: '🌡️', value: 0, type: 'temperature', min: 18, max: 28 },
        { name: 'Humidity', icon: '💧', value: 0, type: 'humidity', min: 40, max: 80 },
        { name: 'Soil Moisture', icon: '🌱', value: 0, type: 'soil', min: 60, max: 90 },
        { name: 'Light Level', icon: '☀️', value: 0, type: 'light', min: 600, max: 1000 }
      ],
      temperatureHistory: [],
      humidityHistory: [],
      lastUpdated: ''
    };
  },
  methods: {
    getStatus(metric) {
      if (metric.value < metric.min) return 'Low';
      if (metric.value > metric.max) return 'High';
      return 'Normal';
    },
    getStatusClass(metric) {
      return `status-${this.getStatus(metric).toLowerCase()}`;
    },
    fetchData() {
      const data = generateMockData();
      this.metrics[0].value = data.temperature;
      this.metrics[1].value = data.humidity;
      this.metrics[2].value = data.soilMoisture;
      this.metrics[3].value = data.lightLevel;

      this.updateChartData(this.temperatureHistory, data.temperature);
      this.updateChartData(this.humidityHistory, data.humidity);

      this.lastUpdated = new Date().toLocaleTimeString();
    },
    updateChartData(history, value) {
      history.push(value);
      if (history.length > 12) history.shift(); // Limit to last 12 entries
    },
    logout() {
      localStorage.clear();
      this.$router.push('/login');
    }
  },
  mounted() {
    this.fetchData();
    setInterval(this.fetchData, 5000);
  }
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

.dashboard {
  margin-top: 80px;
  padding: 2rem;
  flex: 1;
}

.metrics-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin-top: 30px;
}

.metric-card {
  background: #2e2e48;
  color: #fff;
  padding: 1rem;
  border-radius: 10px;
  text-align: center;
  transition: transform 0.2s ease;
}

.metric-card:hover {
  transform: scale(1.05);
}

.metric-value {
  font-size: 1.5em;
  font-weight: bold;
  margin-top: 5px;
}

.status {
  margin-top: 10px;
  padding: 5px 10px;
  border-radius: 5px;
  font-size: 0.9rem;
}

.status-low {
  background: #f39c12;
}

.status-high {
  background: #e74c3c;
}

.status-normal {
  background: #27ae60;
}

.charts-section {
  margin-top: 40px;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
  padding: 1.5rem;
  background-color: #1c1c2d; 
  border-radius: 15px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3); 
}

.chart-wrapper {
  background-color: #2a2a40;
  padding: 1rem;
  border-radius: 10px;
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.4);
  transition: transform 0.3s ease-in-out;
}

.chart-wrapper:hover {
  transform: translateY(-5px);
}

.update-info {
  margin-top: 20px;
  color: #8c9ba5;
  text-align: center;
  font-size: 0.9rem;
}

</style>
