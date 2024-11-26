<template>
  <div>
    <div class="header">
      <h2>📊 Dashboard Overview</h2>
      <p class="subtitle">Monitor environmental metrics in real-time</p>
    </div>

    <div class="cards-container">
      <div class="row large-cards">
        <DataCard
          label="Temperature"
          unit="°C"
          :initialValue="23"
          :min="20"
          :max="30"
          :warningThreshold="thresholds.temperature"
          description="Real-time monitoring of room temperature."
          icon="🌡️"
        />
        <DataCard
          label="Humidity"
          unit="%"
          :initialValue="60"
          :min="50"
          :max="70"
          :warningThreshold="thresholds.humidity"
          description="Keeps track of air humidity for ideal conditions."
          icon="💧"
        />
      </div>
      <div class="row small-cards">
        <DataCard
          label="Soil Moisture"
          unit="%"
          :initialValue="45"
          :min="40"
          :max="50"
          :warningThreshold="thresholds.soilMoisture"
          description="Ensures soil has adequate water levels."
          icon="🌱"
        />
        <DataCard
          label="Light Level"
          unit="lux"
          :initialValue="300"
          :min="200"
          :max="350"
          :warningThreshold="thresholds.lightLevel"
          description="Measures light intensity for plant growth."
          icon="💡"
        />
      </div>
    </div>
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
      thresholds: {
        temperature: 23,
        humidity: 60,
        soilMoisture: 45,
        lightLevel: 300,
      },
    };
  },
};
</script>

<style scoped>
.header {
  text-align: center;
  margin-bottom: 3rem;
}

.header h2 {
  font-size: 2rem;
  color: #2c3e50;
  font-weight: bold;
}

.subtitle {
  font-size: 1rem;
  color: #7f8c8d;
}

.cards-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  gap: 2rem;
  margin-top: 2rem;
}

.row {
  display: flex;
  gap: 2rem;
  justify-content: space-between;
  flex-wrap: wrap;
}

@media (max-width: 768px) {
  .cards-container {
    gap: 1.5rem;
  }

  .row {
    flex-direction: column;
    gap: 1.5rem;
  }
}
</style>