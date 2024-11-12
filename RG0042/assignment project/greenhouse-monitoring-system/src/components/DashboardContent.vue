<template>
    <div class="content">
        <h2>Dashboard Overview</h2>
        <div class="grid-container">
            <div class="card"> Temprature: 23°C</div>
            <div class="card"> Humidity: 65%</div>
            <div class="card">Soil Moisture: 45%</div>
            <div class="card">Light Level: 300 lux</div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "DashboardContent",
    };
</script>

<style scoped>
  .content {
    padding: 2rem;
  }
  
  .grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
  }

  .card {
    background-color: #ffffff;
    padding: 1rem;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    text-align: center;
  }
</style>