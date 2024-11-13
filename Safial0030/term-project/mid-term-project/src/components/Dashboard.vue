<!-- eslint-disable vue/multi-word-component-names -->
<!-- eslint-disable no-unused-vars -->
<!-- eslint-disable no-unused-vars -->
<!-- eslint-disable no-unused-vars -->
<!-- eslint-disable no-unused-vars -->
<!-- eslint-disable vue/multi-word-component-names -->
// eslint-disable-next-line vue/multi-word-component-names
<template>
  <div class="container dashboard-content">
    <h1 class="text-center mb-4">Dashboard</h1>
    <div class="row">
      <div class="col-md-3">
        <div class="card bg-success text-white mb-4">
          <div class="card-body">
            <h5 class="card-title">Temperature (°C)</h5>
            <p class="card-text">{{ data.temperature }}</p>
          </div>
        </div>
      </div>
      <div class="col-md-3">
        <div class="card bg-info text-white mb-4">
          <div class="card-body">
            <h5 class="card-title">Humidity (%)</h5>
            <p class="card-text">{{ data.humidity }}</p>
          </div>
        </div>
      </div>
      <div class="col-md-3">
        <div class="card bg-warning text-dark mb-4">
          <div class="card-body">
            <h5 class="card-title">Soil Moisture (%)</h5>
            <p class="card-text">{{ data.soilMoisture }}</p>
          </div>
        </div>
      </div>
      <div class="col-md-3">
        <div class="card bg-danger text-white mb-4">
          <div class="card-body">
            <h5 class="card-title">Light Level (lux)</h5>
            <p class="card-text">{{ data.lightLevel }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      data: {
        temperature: 20,
        humidity: 60,
        soilMoisture: 30,
        lightLevel: 500,
      },
    };
  },
  mounted() {
    this.fetchData();
    setInterval(this.fetchData, 5000);
  },
  methods: {
    fetchData() {
      const simulatedData = {
        temperature: Math.floor(Math.random() * 30) + 10,
        humidity: Math.floor(Math.random() * 100),
        soilMoisture: Math.floor(Math.random() * 100),
        lightLevel: Math.floor(Math.random() * 1000),
      };
      this.data = simulatedData;
    },
  },
};
</script>

<style scoped>
.dashboard-content {
  margin-top: 100px; /* Adjust this value according to the navbar height */
}

.card {
  border-radius: 10px;
}

.card-title {
  font-weight: bold;
}
</style>