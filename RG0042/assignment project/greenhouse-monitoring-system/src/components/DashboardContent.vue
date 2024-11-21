<template>
  <div class="content">
    <h2>Dashboard Overview</h2>
    <div class="grid-container">
      <DataCard
        label="Temperature"
        unit="°C"
        :initialValue="23"
        :min="10"
        :max="15"
        :warningThreshold="28"
      />
      <DataCard
        label="Humidity"
        unit="%"
        :initialValue="65"
        :min="60"
        :max="80"
        autoUpdate="true"
      />
      <DataCard
        label="Soil Moisture"
        unit="%"
        :initialValue="45"
        :min="40"
        :max="60"
      />
      <DataCard
        label="Light Level"
        unit="lux"
        :initialValue="300"
        :min="100"
        :max="250"
      />
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
};
</script>

<style scoped>
.content {
  padding: 2rem;
  background-color: #f9f9f9;
  min-height: 100vh; /* Ensure it covers the entire viewport height */
  font-family: 'Roboto', sans-serif;
  color: #333;
}

.content h2 {
  font-size: 2rem;
  color: #2c3e50;
  margin-bottom: 1.5rem;
  text-align: center;
  font-weight: 700;
  letter-spacing: 1px;
}

.grid-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  justify-content: center;
  align-items: stretch;
}

.card {
  background: linear-gradient(145deg, #ffffff, #e6e6e6);
  box-shadow: 4px 4px 8px #d1d1d1, -4px -4px 8px #ffffff;
  border-radius: 12px;
  padding: 1.5rem;
  text-align: center;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 6px 6px 12px #c0c0c0, -6px -6px 12px #ffffff;
}

.card span {
  display: block;
  font-size: 1.2rem;
  font-weight: 500;
  margin-top: 0.5rem;
  color: #555;
}

.card strong {
  font-size: 1.8rem;
  font-weight: 700;
  color: #2c3e50;
}

@media (max-width: 768px) {
  .content {
    padding: 1.5rem;
  }

  .grid-container {
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
  }

  .card {
    padding: 1rem;
  }
}
</style>