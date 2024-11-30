<template>
    <div class="dashboard">
      <h1>Greenhouse Monitoring Dashboard</h1>
  
      <div class="metrics-grid">
        <div class="metric-card">
          <h2>Temperature</h2>
          <p>{{ temperature }}°C</p>
        </div>
        <div class="metric-card">
          <h2>Humidity</h2>
          <p>{{ humidity }}%</p>
        </div>
        <div class="metric-card">
          <h2>Soil Moisture</h2>
          <p>{{ soilMoisture }}%</p>
        </div>
        <div class="metric-card">
          <h2>Light Levels</h2>
          <p>{{ lightLevel }} Lux</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "Dashboard",
    data() {
      return {
        temperature: 22,
        humidity: 55,
        soilMoisture: 30
      };
    },
  };
  </script>
  
  <style scoped>
  .dashboard {
    padding: 20px;
    background-color: #f9f9f9;
  }
  
  h1 {
    text-align: center;
    color: #264653;
    margin-bottom: 30px;
  }
  
  .metrics-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 20px;
    padding: 20px;
  }
  
  .metric-card {
    padding: 20px;
    background: #fff;
    border: 1px solid #e1e1e1;
    border-radius: 10px;
    text-align: center;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .metric-card h2 {
    font-size: 1.5rem;
    color: #2a9d8f;
  }
  
  .metric-card p {
    font-size: 1.2rem;
    color: #606c76;
    margin-top: 10px;
  }
  </style>
  