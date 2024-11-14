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
        <!-- Temperature Card -->
        <v-col cols="12" sm="6" md="4">
          <v-card class="metric-card">
            <v-card-text class="d-flex flex-column align-center">
              <v-icon size="48" color="error" class="mb-2">mdi-thermometer</v-icon>
              <div class="text-h4 mb-2">25°C</div>
              <div class="text-subtitle-1">Temperature</div>
            </v-card-text>
          </v-card>
        </v-col>
        <!-- Humidity Card -->
      <v-col cols="12" sm="6" md="4">
        <v-card class="metric-card">
          <v-card-text class="d-flex flex-column align-center">
            <v-icon size="48" color="blue" class="mb-2">mdi-water</v-icon>
            <div class="text-h4 mb-2">60%</div>
            <div class="text-subtitle-1">Humidity</div>
          </v-card-text>
        </v-card>
      </v-col>
     <!-- Soil Moisture Card -->
     <v-col cols="12" sm="6" md="4">
        <v-card class="metric-card">
          <v-card-text class="d-flex flex-column align-center">
            <v-icon size="48" color="brown" class="mb-2">mdi-water-percent</v-icon>
            <div class="text-h4 mb-2">45%</div>
            <div class="text-subtitle-1">Soil Moisture</div>
          </v-card-text>
        </v-card>
      </v-col>
      <!-- Light Level Card -->
<v-col cols="12" sm="6" md="4">
  <v-card class="metric-card">
    <v-card-text class="d-flex flex-column align-center">
      <v-icon size="48" color="orange" class="mb-2">mdi-white-balance-sunny</v-icon>
      <div class="text-h4 mb-2">1200 lux</div>
      <div class="text-subtitle-1">Light Level</div>
    </v-card-text>
  </v-card>
</v-col>
<!-- CO2 Level Card -->
<v-col cols="12" sm="6" md="4">
  <v-card class="metric-card">
    <v-card-text class="d-flex flex-column align-center">
      <v-icon size="48" color="grey-darken-1" class="mb-2">mdi-molecule-co2</v-icon>
      <div class="text-h4 mb-2">450 ppm</div>
      <div class="text-subtitle-1">CO2 Level</div>
    </v-card-text>
  </v-card>
</v-col>
<!-- Nutrient Level Card -->
<v-col cols="12" sm="6" md="4">
  <v-card class="metric-card">
    <v-card-text class="d-flex flex-column align-center">
      <v-icon size="48" color="green" class="mb-2">mdi-leaf</v-icon>
      <div class="text-h4 mb-2">75%</div>
      <div class="text-subtitle-1">Nutrient Level</div>
    </v-card-text>
   </v-card>
    </v-col>
      </v-row>
        </v-container>
          </template>

<style scoped>
.metric-card {
  transition: all 0.3s ease;
}

.metric-card:hover {
  transform: translateY(-5px);
}
</style>