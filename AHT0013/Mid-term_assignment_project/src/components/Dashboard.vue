<template>
  <div>
    <nav class="navbar">
      <div class="logo">Greenhouse</div>
      <ul class="nav-links">
        <li><router-link to="/dashboard">Home</router-link></li>
        <li><router-link to="/over-view">Overview</router-link></li>
        <li><router-link to="/settings">Settings</router-link></li>
        <li><router-link to="/logs">Logs</router-link></li>
        <li><a @click="logout">Logout</a></li>
      </ul>
    </nav>

    <div class="dashboard">
      <header>
        <h1>Dashboard</h1>
        <p>Real-time Monitoring of Greenhouse Conditions</p>
      </header>
      <div>
        <div class="metrics-grid">
          <div class="metric-card">
            <h3>🌡️ Temperature</h3>
            <div class="metric-value">{{ sensorData.temperature }}°C</div>
            <div class="status" :class="getStatusClass(sensorData.temperature, 'temperature', 18, 28)">
              {{ getStatus(sensorData.temperature, 'temperature', 18, 28) }}
            </div>
          </div>

          <div class="metric-card">
            <h3>💧 Humidity</h3>
            <div class="metric-value">{{ sensorData.humidity }}%</div>
            <div class="status" :class="getStatusClass(sensorData.humidity, 'humidity', 40, 80)">
              {{ getStatus(sensorData.humidity, 'humidity', 40, 80) }}
            </div>
          </div>

          <div class="metric-card">
            <h3>🌱 Soil Moisture</h3>
            <div class="metric-value">{{ sensorData.soilMoisture }}%</div>
            <div class="status" :class="getStatusClass(sensorData.soilMoisture, 'soil', 60, 90)">
              {{ getStatus(sensorData.soilMoisture, 'soil', 60, 90) }}
            </div>
          </div>

          <div class="metric-card">
            <h3>☀️ Light Level</h3>
            <div class="metric-value">{{ sensorData.lightLevel }} lux</div>
            <div class="status" :class="getStatusClass(sensorData.lightLevel, 'light', 600, 1000)">
              {{ getStatus(sensorData.lightLevel, 'light', 600, 1000) }}
            </div>
          </div>
        </div>

        <div class="charts-section">
          <div class="chart-card">
            <h3>Temperature History</h3>
            <SimpleLineChart 
              label="Temperature (°C)" 
              :data="temperatureHistory"
            />
          </div>
          <div class="chart-card">
            <h3>Humidity History</h3>
            <SimpleLineChart 
              label="Humidity (%)" 
              :data="humidityHistory"
            />
          </div>
        </div>

        <div class="update-info">
          Last Updated: {{ lastUpdated }}
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import { generateMockData } from '../../DB/mockData'
import SimpleLineChart from './charts/SimpleLineChart.vue'

export default {
  name: 'DashboardView',
  components: {
    SimpleLineChart
  },
  data() {
    return {
      sensorData: {
        temperature: 0,
        humidity: 0,
        soilMoisture: 0,
        lightLevel: 0
      },
      temperatureHistory: [],
      humidityHistory: [],
      loading: true,
      lastUpdated: '',
      updateInterval: null
    }
  },
  methods: {
    getStatus(value, type, defaultMin, defaultMax) {
      const saved = localStorage.getItem('alertSettings')
      const settings = saved ? JSON.parse(saved) : {
        temp: { min: defaultMin, max: defaultMax },
        humidity: { min: 40, max: 80 }
      }

      let min, max;
      if (type === 'temperature') {
        min = settings.temp.min;
        max = settings.temp.max;
      } else if (type === 'humidity') {
        min = settings.humidity.min;
        max = settings.humidity.max;
      } else {
        min = defaultMin;
        max = defaultMax;
      }

      if (value < min) return 'Low'
      if (value > max) return 'High'
      return 'Normal'
    },
    getStatusClass(value, type, defaultMin, defaultMax) {
      const status = this.getStatus(value, type, defaultMin, defaultMax)
      return `status-${status.toLowerCase()}`
    },
    async fetchData() {
      try {
        await new Promise(resolve => setTimeout(resolve, 500))
        const data = generateMockData()
        this.sensorData = data

        this.temperatureHistory.push(data.temperature)
        this.humidityHistory.push(data.humidity)

        if (this.temperatureHistory.length > 5) {
          this.temperatureHistory.shift()
          this.humidityHistory.shift()
        }

        const now = new Date()
        this.lastUpdated = now.toLocaleTimeString()
        this.loading = false
      } catch (error) {
        console.error('Error fetching data:', error)
      }
    },
    logout() {
      localStorage.clear()
      this.$router.push('/login')
    }
  },
  mounted() {
    const saved = localStorage.getItem('alertSettings')
    if (saved) {
      console.log('Loaded saved settings:', JSON.parse(saved))
    }

    for (let i = 0; i < 5; i++) {
      const data = generateMockData()
      this.temperatureHistory.push(data.temperature)
      this.humidityHistory.push(data.humidity)
    }

    this.fetchData()
    this.updateInterval = setInterval(this.fetchData, 5000)
  },
  beforeUnmount() {
    if (this.updateInterval) {
      clearInterval(this.updateInterval)
    }
  }
}
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
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
  background: rgb(255, 255, 255);
  color: #333;
  border-bottom: 1px solid #00000072;
  box-shadow: 0 3px 5px rgba(0, 0, 0, 0.05);
  z-index: 100;
}

.logo {
  font-size: 2rem;
  font-weight: bold;
  color: #000000;
}

.nav-links {
  list-style: none;
  display: flex;
  gap: 20px;
}

.nav-links li a {
  text-decoration: none;
  color: #2c3e50;
  font-size: 1rem;
  transition: color 0.3s ease;
}

.nav-links li a:hover {
  color: #1d7f0b;
}

.metrics-grid {
  display:grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  margin-top: 30px;
}
main {
  padding: 2rem 3rem;
}

header h1 {
  font-size: 2.2rem;
  font-weight: 700;
  color: #ffffff;
  margin-top: 270px;
}

header p {
  font-size: 1rem;
  color: #d7d7d7;
  font-weight: 300;
}

.metric-card {
  display:block;
  background-color: rgba(255, 255, 255, 0.26);
  padding: 1rem;
  height: 100px;
  width: 300px;
  border-radius: 16px;
  text-align:center;
  transform: translateY(-5px);
  box-shadow: 0 15px 30px rgba(4, 37, 1, 0.15);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.metric-value {
  font-size: 1.5em;
  font-weight: bold;
  margin-right: auto;
  color: #121212;
}

.status {
  display: inline-block;
  padding: 1px 10px;
  border-radius: 4px;
  font-size: 0.9em;
}

.status-normal {
  background-color: #28a745;
  color: white;
}

.status-high {
  background-color: #dc3545;
  color: white;
}

.status-low {
  background-color: #ffc107;
  color: black;
}

.charts-section {
  margin-top: 50px;
  display: flex;
  grid-template-columns: 1fr;
  gap: 25px;
}

.chart-card {
  background-color: rgba(255, 255, 255, 0.94);
  color: #28a745;
  height: 370px;
  width: 300px;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.update-info {
  text-align:center;
  margin-top: 5px;
  color: #d4d4d4;
  font-size: 0.7em;
}

@media (min-width: 1024px) {
    .charts-section {
      grid-template-columns: 1fr 1fr;
    }
  }
  
  @media (max-width: 768px) {
    .metrics-grid {
      grid-template-columns: 1fr 1fr;
    }
}
</style>