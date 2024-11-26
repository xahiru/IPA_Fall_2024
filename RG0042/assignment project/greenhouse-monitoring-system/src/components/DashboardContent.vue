<template>
  <div class="content-container">
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
        temperature: 28,
        humidity: 65,
        soilMoisture: 40,
        lightLevel: 300,
      },
    };
  },
};
</script>

<style scoped>
.header {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  margin-bottom: 2rem;
}

.cards-container {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.row {
  display: flex;
  justify-content: center;
  gap: 2rem;
}

.row > div {
  flex: 1;
  height: 200px;
  max-width: 350px;
}

.row > div {
  background-color: #ffffff;
  border-radius: 12px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s, box-shadow 0.2s;
}

.row > div:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

@media (max-width: 768px) {
  .header h2 {
    font-size: 1.6rem;
  }

  .cards-container {
    gap: 1.5rem;
  }

  .row {
    flex-direction: column;
    gap: 1.5rem;
  }

  .row > div {
    max-width: 100%;
    height: auto;
  }
}

@media (max-width: 480px) {
  .header h2 {
    font-size: 1.4rem;
  }

  .content-container {
    padding: 1rem;
  }
}
</style>