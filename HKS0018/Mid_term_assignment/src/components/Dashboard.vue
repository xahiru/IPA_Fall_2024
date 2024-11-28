<template>
  <div class="dashboard-layout">
    <Navbar />

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
        <div class="chart-row">
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
        <div class="chart-row">
          <ChartHistory
            title="Soil Moisture Chart History"
            :label="'Soil Moisture (%)'"
            :data="soilMoistureHistory"
          />
          <ChartHistory
            title="Light Level Chart History"
            :label="'Light Level (lux)'"
            :data="lightLevelHistory"
          />
        </div>
      </div>

      <div class="update-info">Last Updated: {{ lastUpdated }}</div>
    </main>
  </div>
</template>

<script>
import Navbar from "../components/Navbar.vue";
import { generateMockData } from "../../db/mockData";
import ChartHistory from "./charts/ChartHistory.vue";

export default {
  components: { Navbar, ChartHistory },
  data() {
    return {
      metrics: [
        { name: "Temperature", icon: "🌡️", value: 0, type: "temperature", min: 18, max: 28 },
        { name: "Humidity", icon: "💧", value: 0, type: "humidity", min: 40, max: 80 },
        { name: "Soil Moisture", icon: "🌱", value: 0, type: "soil", min: 60, max: 90 },
        { name: "Light Level", icon: "☀️", value: 0, type: "light", min: 600, max: 1000 }
      ],
      temperatureHistory: [],
      humidityHistory: [],
      soilMoistureHistory: [],
      lightLevelHistory: [],
      lastUpdated: ""
    };
  },
  methods: {
    getStatus(metric) {
      if (metric.value < metric.min) return "Low";
      if (metric.value > metric.max) return "High";
      return "Normal";
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
      this.updateChartData(this.soilMoistureHistory, data.soilMoisture);
      this.updateChartData(this.lightLevelHistory, data.lightLevel);

      this.lastUpdated = new Date().toLocaleTimeString();
    },
    updateChartData(history, value) {
      history.push(value);
      if (history.length > 12) history.shift();
    },
    logout() {
      localStorage.clear();
      this.$router.push("/login");
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

.dashboard {
  margin-top: 80px;
  padding: 1.5rem;
  flex: 1;
}

.metrics-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 16px;
  margin-top: 20px;
}

.metric-card {
  background: #2e2e48;
  color: #fff;
  padding: 0.75rem;
  border-radius: 8px;
  text-align: center;
  transition: transform 0.2s ease;
}

.metric-card:hover {
  transform: scale(1.05);
}

.metric-value {
  font-size: 1.4em;
  font-weight: bold;
  margin-top: 5px;
}

.status {
  margin-top: 8px;
  padding: 4px 8px;
  border-radius: 5px;
  font-size: 0.85rem;
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
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); /* Auto-fit charts */
  gap: 20px;
  margin-top: 30px;
  padding: 1rem;
  background-color: #1c1c2d;
  border-radius: 12px;
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.3);
}

.chart-container {
  background-color: #2e2e48;
  padding: 1rem;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
}

.update-info {
  margin-top: 15px;
  color: #8c9ba5;
  text-align: center;
  font-size: 0.85rem;
}
</style>


