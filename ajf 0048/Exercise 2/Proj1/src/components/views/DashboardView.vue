<template>
  <v-container fluid>
    <v-row>
      <v-col cols="12">
        <h1 class="text-h4 mb-6">
          <v-icon size="36" color="primary" class="mr-2">mdi-view-dashboard</v-icon>
          Greenhouse Dashboard
        </h1>
      </v-col>
    </v-row>

    <v-row>
      <v-col v-for="(value, key) in metrics" :key="key" cols="12" sm="6" md="4">
        <v-card class="metric-card">
          <v-card-text class="d-flex flex-column align-center">
            <v-icon size="48" :color="getMetricColor(key)" class="mb-2">{{ getMetricIcon(key) }}</v-icon>
            <div class="text-h4 mb-2">{{ value.toFixed(1) }}</div>
            <div class="text-subtitle-1">{{ key }}</div>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import api from '../../services/api';

const metrics = ref({})
let intervalId

const getMetricIcon = (metric) => {
  const icons = {
    temperature: 'mdi-thermometer',
    humidity: 'mdi-water',
    soilMoisture: 'mdi-water-percent',
    lightLevel: 'mdi-white-balance-sunny',
    co2Level: 'mdi-molecule-co2',
    nutrientLevel: 'mdi-leaf'
  }
  return icons[metric]
}

const getMetricColor = (metric) => {
  const colors = {
    temperature: 'error',
    humidity: 'blue',
    soilMoisture: 'brown',
    lightLevel: 'orange',
    co2Level: 'grey-darken-1',
    nutrientLevel: 'green'
  }
  return colors[metric]
}

const fetchMetrics = async () => {
  const data = await api.getMetrics()
  metrics.value = data
}

onMounted(() => {
  fetchMetrics()
  intervalId = setInterval(fetchMetrics, 5000)
})

onUnmounted(() => {
  if (intervalId) clearInterval(intervalId)
})
</script>