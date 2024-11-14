<template>
  <v-container fluid>
    <v-row>
      <v-col cols="12">
        <h1 class="text-h4 mb-6 text-primary font-weight-bold">
          <v-icon large color="primary" class="mr-2">mdi-view-dashboard</v-icon>
          Greenhouse Overview
        </h1>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12" sm="6" md="3">
        <v-hover v-slot="{ isHovering, props }">
          <v-card
            v-bind="props"
            :elevation="isHovering ? 8 : 2"
            class="metric-card"
          >
            <v-card-text class="d-flex flex-column align-center">
              <v-icon size="48" color="error" class="mb-2"
                >mdi-thermometer</v-icon
              >
              <div class="text-h4 mb-2">{{ temperature.toFixed(1) }}°C</div>
              <div class="text-subtitle-1">Temperature</div>
              <v-progress-linear
                :model-value="temperaturePercentage"
                :color="temperatureColor"
                height="4"
                rounded
              ></v-progress-linear>
            </v-card-text>
          </v-card>
        </v-hover>
      </v-col>

      <v-col cols="12" sm="6" md="3">
        <v-hover v-slot="{ isHovering, props }">
          <v-card
            v-bind="props"
            :elevation="isHovering ? 8 : 2"
            class="metric-card"
          >
            <v-card-text class="d-flex flex-column align-center">
              <v-icon size="48" color="blue" class="mb-2">mdi-water</v-icon>
              <div class="text-h4 mb-2">{{ humidity.toFixed(1) }}%</div>
              <div class="text-subtitle-1">Humidity</div>
              <v-progress-linear
                :model-value="humidity"
                color="blue"
                height="4"
                rounded
              ></v-progress-linear>
            </v-card-text>
          </v-card>
        </v-hover>
      </v-col>

      <v-col cols="12" sm="6" md="3">
        <v-hover v-slot="{ isHovering, props }">
          <v-card
            v-bind="props"
            :elevation="isHovering ? 8 : 2"
            class="metric-card"
          >
            <v-card-text class="d-flex flex-column align-center">
              <v-icon size="48" color="brown" class="mb-2"
                >mdi-water-percent</v-icon
              >
              <div class="text-h4 mb-2">{{ soilMoisture.toFixed(1) }}%</div>
              <div class="text-subtitle-1">Soil Moisture</div>
              <v-progress-linear
                :model-value="soilMoisture"
                color="brown"
                height="4"
                rounded
              ></v-progress-linear>
            </v-card-text>
          </v-card>
        </v-hover>
      </v-col>

      <v-col cols="12" sm="6" md="3">
        <v-hover v-slot="{ isHovering, props }">
          <v-card
            v-bind="props"
            :elevation="isHovering ? 8 : 2"
            class="metric-card"
          >
            <v-card-text class="d-flex flex-column align-center">
              <v-icon size="48" color="orange" class="mb-2"
                >mdi-white-balance-sunny</v-icon
              >
              <div class="text-h4 mb-2">{{ lightLevel.toFixed(0) }} lux</div>
              <div class="text-subtitle-1">Light Level</div>
              <v-progress-linear
                :model-value="lightLevel / 20"
                color="orange"
                height="4"
                rounded
              ></v-progress-linear>
            </v-card-text>
          </v-card>
        </v-hover>
      </v-col>
    </v-row>

    <v-row class="mt-6">
      <v-col cols="12">
        <v-card class="chart-container" elevation="2">
          <v-card-title class="d-flex align-center">
            <v-icon color="primary" class="mr-2">mdi-chart-line</v-icon>
            Real-Time Metrics
          </v-card-title>
          <v-card-text>
            <div style="height: 400px; position: relative">
              <GreenhouseChart />
            </div>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>

  <v-row class="mt-6">
    <v-col cols="12">
      <ControlPanel />
    </v-col>
  </v-row>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";

const temperature = ref(25);
const humidity = ref(60);
const soilMoisture = ref(45);
const lightLevel = ref(1200);

const temperaturePercentage = computed(() => (temperature.value / 40) * 100);
const temperatureColor = computed(() => {
  if (temperature.value > 30) return "error";
  if (temperature.value > 25) return "warning";
  return "success";
});

onMounted(() => {
  setInterval(updateMetrics, 5000);
});

function updateMetrics() {
  temperature.value = Math.random() * (30 - 20) + 20;
  humidity.value = Math.random() * (80 - 40) + 40;
  soilMoisture.value = Math.random() * (100 - 20) + 20;
  lightLevel.value = Math.random() * (2000 - 100) + 100;
}
</script>

<style scoped>
.metric-card {
  transition: all 0.3s ease;
}

.metric-card:hover {
  transform: translateY(-5px);
}

.chart-container {
  height: 400px;
}
</style>
