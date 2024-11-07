<template>
    <v-container fluid>
      <h1 class="text-h4 mb-6 text primary font-weight-bold">
        <v-icon large color="primary" class="mr-2">mdi-view-dashboard</v-icon>
        Greenhouse Metrics
      </h1>

      <v-row>
        <v-col cols="12" sm="6" md="3">
          <v-hover v-slot="{ isHovering, props }">
          <v-card
            v-bind="props"
            :elevation="isHovering ? 12 : 2"
             :class="['metric-card', {'pulse': isUpdating}]"
          ></v-card>
          <v-card elevation="2">
            <v-card-title class="text-subtitle-1">
              <v-icon color="error" class="mr-2">mdi-thermometer</v-icon> 
              Temperature
            </v-card-title>
            <v-card-text>
              <div class="text-h4 mb-2">{{ temperature.toFixed(1) }}°C</div>
              <v-progress-linear
                :model-value="temperature"
                :color="getTemperatureColor > 30 ? 'error' : 'success'"
                height="8"
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
            :elevation="isHovering ? 12 : 2"
            class="transition-swing"
          ></v-card>
          <v-card elevation="2">
            <v-card-title class="text-subtitle-1"><v-icon color="blue" class="mr-2">mdi-water</v-icon>
              Humidity
            </v-card-title>
            <v-card-text>
              <div class="text-h4 mb-2">{{ humidity.toFixed(1) }}%</div>
              <v-progress-linear
                :model-value="humidity"
                color="blue"
                height="8"
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
            :elevation="isHovering ? 12 : 2"
            class="transition-swing"
          ></v-card>
          <v-card elevation="2">
            <v-card-title class="text-subtitle-1">
              <v-icon color="brown" class="mr-2">mdi-water-percent</v-icon>
              Soil Moisture
            </v-card-title>
            <v-card-text>
              <div class="text-h4 mb-2">{{ soilMoisture.toFixed(1) }}%</div>
              <v-progress-linear
                :model-value="soilMoisture"
                color="brown"
                height="8"
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
            :elevation="isHovering ? 12 : 2"
            class="transition-swing"
          ></v-card>
          <v-card elevation="2">
            <v-card-title class="text-subtitle-1">
              <v-icon color="orange" class="mr-2">mdi-white-balance-sunny</v-icon>
              Light Level
            </v-card-title>
            <v-card-text>
              <div class="text-h4 mb-2">{{ lightLevel.toFixed(0) }} lux</div>
              <v-progress-linear
                :model-value="lightLevel / 20"
                color="orange"
                height="8"
              ></v-progress-linear>
            </v-card-text>
          </v-card>
        </v-hover>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script setup>
  import { ref, computed, onMounted } from 'vue'
  
  const temperature = ref(25)
  const humidity = ref(60)
  const soilMoisture = ref(45)
  const lightLevel = ref(1200)

  const isUpdating = ref(false)

  const getTemperatureColor = computed(()=>{
    return temperature.value > 30 ? 'error' : 'success'
  })
  
  // Simulate real-time updates
  onMounted(() => {
    setInterval(() => {
      isUpdating.value = true
      temperature.value = Math.random() * (30 - 20) + 20
      humidity.value = Math.random() * (80 - 40) + 40
      soilMoisture.value = Math.random() * (100 - 20) + 20
      lightLevel.value = Math.random() * (2000 - 100) + 100
    }, 5000)
    setTimeout(() => {
      isUpdating.value = false
    }, (500)
    , 3000)
})
  </script>

  <style scoped>
.transition-swing{
  transition: 0.3s cubic-bezier(0.25,0.8,0.5,1);
}
.animate-fade-in {
  animation: fadeIn 0.5s ease-in;
}

.metric-card {
  transition: all 0.3s ease;
}

.pulse {
  animation: pulse 0.5s ease-in-out;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes pulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.02); }
  100% { transform: scale(1); }
}
</style>