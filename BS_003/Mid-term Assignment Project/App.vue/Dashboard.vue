<template>
  <div>
    <h2>Greenhouse Dashboard</h2>
    <div class="card">
      <h3>Temperature</h3>
      <p>{{ temperature }} °C</p>
    </div>

    <div class="card">
      <h3>Humidity</h3>
      <p>{{ humidity }} %</p>
    </div>

    <div class="card">
      <h3>Soil Moisture</h3>
      <p>{{ soilMoisture }} %</p>
    </div>

    <div class="card">
      <h3>Light Level</h3>
      <p>{{ lightLevel }} lux</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      temperature: null,
      humidity: null,
      soilMoisture: null,
      lightLevel: null,
    };
  },
  created() {
    this.fetchData();
    setInterval(this.fetchData, 5000);
  },
  methods: {
    fetchData() {
      axios.get('/api/greenhouse-metrics').then((response) => {
        const data = response.data;
        this.temperature = data.temperature;
        this.humidity = data.humidity;
        this.soilMoisture = data.soilMoisture;
        this.lightLevel = data.lightLevel;
      });
    },
  },
};
</script>

<style scoped>
.card {
  border: 1px solid #ddd;
  padding: 20px;
  margin: 10px;
}
</style>
