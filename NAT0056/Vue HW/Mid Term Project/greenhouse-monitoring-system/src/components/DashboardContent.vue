<template>
    <div>
      <header class="header">
        <h2 aria-label="Dashboard Overview">📊 Dashboard Overview</h2>
        <p class="subtitle">Monitor environmental metrics in real-time</p>
      </header>
  
      <main class="cards-container">
        <!-- Large Cards -->
        <section class="row large-cards">
          <DataCard
            label="Temperature"
            unit="°C"
            :value="metrics.temperature"
            :min="20"
            :max="30"
            :warningThreshold="thresholds.temperature"
            description="Real-time monitoring of room temperature."
            icon="🔥"
            :isWarning="metrics.temperature > thresholds.temperature"
          />
          <DataCard
            label="Humidity"
            unit="%"
            :value="metrics.humidity"
            :min="50"
            :max="70"
            :warningThreshold="thresholds.humidity"
            description="Keeps track of air humidity for ideal conditions."
            icon="🌫️"
            :isWarning="metrics.humidity > thresholds.humidity"
          />
        </section>
  
        <!-- Small Cards -->
        <section class="row small-cards">
          <DataCard
            label="Soil Moisture"
            unit="%"
            :value="metrics.soilMoisture"
            :min="40"
            :max="50"
            :warningThreshold="thresholds.soilMoisture"
            description="Ensures soil has adequate water levels."
            icon="🪴"
            :isWarning="metrics.soilMoisture < thresholds.soilMoisture"
          />
          <DataCard
            label="Light Level"
            unit="lux"
            :value="metrics.lightLevel"
            :min="200"
            :max="350"
            :warningThreshold="thresholds.lightLevel"
            description="Measures light intensity for plant growth."
            icon="☀️"
            :isWarning="metrics.lightLevel < thresholds.lightLevel"
          />
        </section>
      </main>
    </div>
  </template>
  
  <script>
  import DataCard from "@/components/DataCard.vue";
  
  export default {
    name: "DashboardContent",
    components: {
      DataCard,
    },
    data() {
      return {
        metrics: {
          temperature: 23,
          humidity: 60,
          soilMoisture: 45,
          lightLevel: 300,
        },
        thresholds: {
          temperature: 25,
          humidity: 65,
          soilMoisture: 50,
          lightLevel: 250,
        },
      };
    },
  };
  </script>
  
  