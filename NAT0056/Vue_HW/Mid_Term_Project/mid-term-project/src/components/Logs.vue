<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { Line } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, LineElement, CategoryScale, LinearScale } from 'chart.js';

ChartJS.register(Title, Tooltip, Legend, LineElement, CategoryScale, LinearScale);

const router = useRouter();
const logs = ref([]);
const timePeriod = ref('24h'); // default time period is 24 hours

const historicalData = ref({
  labels: [],  // time labels for x-axis
  datasets: [
    {
      label: 'Temperature',
      data: [],
      borderColor: '#FF5733',
      backgroundColor: 'rgba(255, 87, 51, 0.2)',
      fill: true,
      tension: 0.3
    },
    {
      label: 'Humidity',
      data: [],
      borderColor: '#4CAF50',
      backgroundColor: 'rgba(76, 175, 80, 0.2)',
      fill: true,
      tension: 0.3
    }
  ]
});

onMounted(() => {
  const user = localStorage.getItem("user");
  if (!user) {
    router.push({ name: 'Login' });
  }
  fetchLogs();
  fetchHistoricalData(timePeriod.value);
});

const fetchLogs = async () => {
  try {
    const response = await fetch('../../DB/logs.json');
    logs.value = await response.json();
  } catch (error) {
    console.error('Error fetching logs:', error);
  }
};

const fetchHistoricalData = async (period) => {
  // This is a mock for the data, you can replace it with real API data
  let labels = [];
  let tempData = [];
  let humidityData = [];

  if (period === '24h') {
    labels = ['12:00', '3:00', '6:00', '9:00', '12:00', '15:00', '18:00'];
    tempData = [22, 24, 23, 25, 26, 24, 23];
    humidityData = [60, 65, 62, 70, 75, 68, 65];
  } else if (period === '1w') {
    labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];
    tempData = [21, 22, 23, 24, 26, 28, 25];
    humidityData = [58, 62, 64, 70, 73, 72, 69];
  }

  historicalData.value = {
    labels: labels,
    datasets: [
      { ...historicalData.value.datasets[0], data: tempData },
      { ...historicalData.value.datasets[1], data: humidityData }
    ]
  };
};

const changeTimePeriod = (period) => {
  timePeriod.value = period;
  fetchHistoricalData(period);
};

const logout = async () => {
  localStorage.removeItem("user");
  router.push({ name: 'Login' });
};
</script>

<template>
  <div id="logs">
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
        <h1>Logs</h1>
        <p>System Logs for Greenhouse Monitoring</p>
      </header>

      <section class="time-period">
        <button @click="changeTimePeriod('24h')">Last 24 Hours</button>
        <button @click="changeTimePeriod('1w')">Last Week</button>
      </section>

      <section class="chart-container">
        <Line :data="historicalData" />
      </section>

      <section class="logs">
        <div v-for="(log, index) in logs" :key="index" class="log-card">
          <div class="log-card-icon" :style="{ backgroundColor: log.level === 'error' ? '#e74c3c' : log.level === 'warning' ? '#f39c12' : '#2ecc71' }">
            <span>{{ log.level === 'error' ? '⚠️' : log.level === 'warning' ? '⚡' : '✅' }}</span>
          </div>
          <div class="log-card-content">
            <h2>{{ log.message }}</h2>
            <p class="log-time">{{ new Date(log.timestamp).toLocaleString() }}</p>
            <p class="log-action">Action: {{ log.action }}</p>
            <p class="log-user">User: {{ log.user }}</p>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<style scoped>
/* Your existing styles go here */

/* Add a style for the chart container */
.chart-container {
  margin-top: 2rem;
  padding: 1rem;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.time-period {
  display: flex;
  gap: 20px;
  margin-top: 2rem;
}

.time-period button {
  padding: 0.6rem 1.2rem;
  font-size: 1rem;
  border: none;
  background-color: #3498db;
  color: white;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.time-period button:hover {
  background-color: #2980b9;
}
</style>
