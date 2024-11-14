<template>
    <v-container fluid>
      <v-row>
        <v-col cols="12" md="8" lg="6">
          <v-card>
            <v-card-title class="text-h4 d-flex align-center">
              <v-icon size="36" color="primary" class="mr-2">mdi-cog</v-icon>
              Alert Thresholds
            </v-card-title>
  
            <v-card-text>
              <v-form v-model="valid" @submit.prevent="saveSettings">
                <v-slider
                  v-model="settings.temperature"
                  label="Temperature Alert (°C)"
                  min="15"
                  max="35"
                  thumb-label
                  class="mb-4"
                ></v-slider>
  
                <v-slider
                  v-model="settings.humidity"
                  label="Humidity Alert (%)"
                  min="30"
                  max="90"
                  thumb-label
                  class="mb-4"
                ></v-slider>
  
                <v-slider
                  v-model="settings.soilMoisture"
                  label="Soil Moisture Alert (%)"
                  min="20"
                  max="80"
                  thumb-label
                  class="mb-4"
                ></v-slider>
  
                <v-btn
                  type="submit"
                  color="primary"
                  block
                  :loading="saving"
                >
                  Save Settings
                </v-btn>
              </v-form>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  
  const valid = ref(true)
  const saving = ref(false)
  
  const settings = ref({
    temperature: 25,
    humidity: 60,
    soilMoisture: 45
  })
  
  const saveSettings = () => {
    saving.value = true
    setTimeout(() => {
      saving.value = false
    }, 1000)
  }
  </script>