<template>
    <div class="data-display">
      <h2>Greenhouse Metrics</h2>
      <div class="metrics-grid">
        <div class="metric-card" v-for="metric in metrics" :key="metric.name">
          <h3>{{ metric.name }}</h3>
          <p>{{ metric.value }} {{ metric.unit }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "DataDisplay",
    data() {
      return {
        metrics: [
          { name: "Temperature", value: 24, unit: "°C" },
          { name: "Humidity", value: 55, unit: "%" },
          { name: "Soil Moisture", value: 35, unit: "%" },
          { name: "Light Level", value: 400, unit: "lux" },
        ],
      };
    },
  };
  </script>
  
  <style scoped>
  .data-display {
    text-align: center;
  }
  
  .metrics-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
    gap: 20px;
    margin-top: 20px;
  }
  
  .metric-card {
    background: #42b983;
    color: white;
    padding: 20px;
    border-radius: 8px;
    text-align: center;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  }
  </style>
  