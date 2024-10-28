<template>
    <v-container>
      <h2 class="text-h4 mb-4">Greenhouse Metrics</h2>
      <v-row>
        <v-col cols="12" sm="6" md="3">
          <v-card elevation="2">
            <v-card-title class="text-subtitle-1">Temperature</v-card-title>
            <v-card-text>
              <div class="text-h4">{{ temperature }}°C</div>
              <v-progress-linear
                :model-value="temperature"
                :color="temperature > 30 ? 'error' : 'success'"
                height="8"
              ></v-progress-linear>
            </v-card-text>
          </v-card>
        </v-col>
  
        <v-col cols="12" sm="6" md="3">
          <v-card elevation="2">
            <v-card-title class="text-subtitle-1">Humidity</v-card-title>
            <v-card-text>
              <div class="text-h4">{{ humidity }}%</div>
              <v-progress-linear
                :model-value="humidity"
                color="info"
                height="8"
              ></v-progress-linear>
            </v-card-text>
          </v-card>
        </v-col>
  
        <v-col cols="12" sm="6" md="3">
          <v-card elevation="2">
            <v-card-title class="text-subtitle-1">Soil Moisture</v-card-title>
            <v-card-text>
              <div class="text-h4">{{ soilMoisture }}%</div>
              <v-progress-linear
                :model-value="soilMoisture"
                color="primary"
                height="8"
              ></v-progress-linear>
            </v-card-text>
          </v-card>
        </v-col>
  
        <v-col cols="12" sm="6" md="3">
          <v-card elevation="2">
            <v-card-title class="text-subtitle-1">Light Level</v-card-title>
            <v-card-text>
              <div class="text-h4">{{ lightLevel }} lux</div>
              <v-progress-linear
                :model-value="lightLevel / 20"
                color="warning"
                height="8"
              ></v-progress-linear>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  
  const temperature = ref(25)
  const humidity = ref(60)
  const soilMoisture = ref(45)
  const lightLevel = ref(1200)
  
  // Simulate real-time updates
  onMounted(() => {
    setInterval(() => {
      temperature.value = Math.random() * (30 - 20) + 20
      humidity.value = Math.random() * (80 - 40) + 40
      soilMoisture.value = Math.random() * (100 - 20) + 20
      lightLevel.value = Math.random() * (2000 - 100) + 100
    }, 5000)
  })
  </script>