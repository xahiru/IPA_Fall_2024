<template>
    <div>
      <Navbar/>
      <div class="chart">
        <header>
          <h1>Charts</h1>
          <p>Real-time Monitoring of Greenhouse Conditions</p>
        </header>
      </div>
  
      <div class="charts-grid">
        <div class="chart-card">
          <h3>Temperature History</h3>
          <LineChart 
            label="Temperature (°C)" 
            :data="temperatureHistory" 
          />
        </div>
        <div class="chart-card">
          <h3>Humidity History</h3>
          <LineChart 
            label="Humidity (%)" 
            :data="humidityHistory" 
          />
        </div>
        <div class="chart-card">
          <h3>Soil Moisture History</h3>
          <LineChart 
            label="Humidity (%)" 
            :data="humidityHistory" 
          />
        </div>
        <div class="chart-card">
          <h3>Light Level History</h3>
          <LineChart 
            label="Humidity (%)" 
            :data="humidityHistory" 
          />
        </div>
      </div>
  
      <div class="update-info">
        Last Updated: {{ lastUpdated }}
      </div>
    </div>
</template>
  
<script>
  import { generateMockData } from '../../public/mockData'; // Adjust the path if necessary
  import LineChart from '../LineChart.vue';
  import Navbar from './Navbar.vue';
  
  export default {
    name: 'Charts',
    components: {
      LineChart,
      Navbar,
    },
    data() {
      return {
        sensorData: {
          temperature: 0,
          humidity: 0,
          soilMoisture: 0,
          lightLevel: 0,
        },
        temperatureHistory: [],
        humidityHistory: [],
        loading: true,
        lastUpdated: '',
        updateInterval: null,
      };
    },
    methods: {
      async fetchData() {
        try {
          const data = generateMockData();
          this.sensorData = data;
  
          this.temperatureHistory.push(data.temperature);
          this.humidityHistory.push(data.humidity);
  
          if (this.temperatureHistory.length > 10) {
            this.temperatureHistory.shift();
          }
          if (this.humidityHistory.length > 10) {
            this.humidityHistory.shift();
          }
  
          const now = new Date();
          this.lastUpdated = now.toLocaleTimeString();
          this.loading = false;
        } catch (error) {
          console.error('Error fetching data:', error);
        }
      },
      logout() {
        localStorage.clear();
        this.$router.push('/login');
      },
    },
    mounted() {
      for (let i = 0; i < 5; i++) {
        const data = generateMockData();
        this.temperatureHistory.push(data.temperature);
        this.humidityHistory.push(data.humidity);
      }
  
      this.fetchData();
      this.updateInterval = setInterval(this.fetchData, 5000);
    },
    beforeUnmount() {
      if (this.updateInterval) {
        clearInterval(this.updateInterval);
      }
    },
  };
</script>
  
<style scoped>
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
  
  
  .charts-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1.5rem;
  }
  
  
  .chart-card {
    background-color: #ffffff;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    padding: 1.5rem;
    text-align: center;
    min-height: 250px;
  }
  
  
  .chart-card h3 {
    font-size: 1.25rem;
    color: #333;
    margin-bottom: 1rem;
  }
  
  
  .update-info {
    text-align: center;
    margin-top: 1.5rem;
    font-size: 0.9rem;
    color: #6c757d;
  }
  
  @media (max-width: 768px) {
    .charts-grid {
      grid-template-columns: 1fr;
    }
    .chart-card h3 {
      font-size: 1.1rem;
    }
  }
</style>