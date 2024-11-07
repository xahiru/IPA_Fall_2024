<template>
    <div class="metrics-container">
      
      <div class="metric-card">
        <h3>Temperature</h3>
        <p>{{ temperature }} °C</p>
      </div>
  
      <div class="metric-card">
        <h3>Humidity</h3>
        <p>{{ humidity }} %</p>
      </div>
  
      <div class="metric-card">
        <h3>Soil Moisture</h3>
        <p>{{ soilMoisture }} %</p>
      </div>
  
      <div class="metric-card">
        <h3>Light Level</h3>
        <p>{{ lightLevel }} lux</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'MetricsDisplay',
    data() {
      return {
        temperature: 22, 
        humidity: 50,   
        soilMoisture: 65, 
        lightLevel: 800,  
      };
    },
    mounted() {
     
      this.fetchMetrics();
    },
    methods: {
     
      fetchMetrics() {
      
        setInterval(() => {
          this.temperature = (Math.random() * (30 - 20) + 20).toFixed(1); 
          this.humidity = (Math.random() * 20 + 40).toFixed(1);
          this.soilMoisture = (Math.random() * 30 + 50).toFixed(1); 
          this.lightLevel = Math.floor(Math.random() * (1000 - 500) + 500); //
        }, 5000); 
      },
    },
  };
  </script>
  
  <style scoped>
  .metrics-container {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
    padding: 20px;
  }
  
  .metric-card {
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    text-align: center;
    transition: transform 0.3s ease;
  }
  
  .metric-card:hover {
    transform: translateY(-5px);
  }
  
  .metric-card h3 {
    font-size: 1.5em;
    margin-bottom: 10px;
  }
  
  .metric-card p {
    font-size: 1.2em;
    color: #333;
  }
  </style>
  