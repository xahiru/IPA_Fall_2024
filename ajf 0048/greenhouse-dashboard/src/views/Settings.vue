<template>
    <v-container>
      <h2 class="text-h4 mb-4">Greenhouse Settings</h2>
      <v-card class="mx-auto" max-width="800">
        <v-card-text>
          <v-form @submit.prevent="saveSettings">
            <v-row>
              <v-col cols="12" md="6">
                <v-text-field
                  v-model="settings.temperatureThreshold"
                  label="Temperature Threshold (°C)"
                  type="number"
                  hint="Alert when temperature exceeds this value"
                ></v-text-field>
              </v-col>
  
              <v-col cols="12" md="6">
                <v-text-field
                  v-model="settings.humidityThreshold"
                  label="Humidity Threshold (%)"
                  type="number"
                  hint="Alert when humidity exceeds this value"
                ></v-text-field>
              </v-col>
  
              <v-col cols="12" md="6">
                <v-text-field
                  v-model="settings.soilMoistureThreshold"
                  label="Soil Moisture Threshold (%)"
                  type="number"
                  hint="Alert when soil moisture falls below this value"
                ></v-text-field>
              </v-col>
  
              <v-col cols="12" md="6">
                <v-text-field
                  v-model="settings.lightLevelThreshold"
                  label="Light Level Threshold (lux)"
                  type="number"
                  hint="Alert when light level falls below this value"
                ></v-text-field>
              </v-col>
            </v-row>
  
            <v-btn
              color="primary"
              type="submit"
              block
              class="mt-4"
            >
              Save Settings
            </v-btn>
          </v-form>
        </v-card-text>
      </v-card>
    </v-container>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  
  const settings = ref({
    temperatureThreshold: 30,
    humidityThreshold: 70,
    soilMoistureThreshold: 40,
    lightLevelThreshold: 1000
  })
  
  const saveSettings = () => {
    // Save settings to localStorage
    localStorage.setItem('greenhouseSettings', JSON.stringify(settings.value))
    // Show success message
    alert('Settings saved successfully!')
  }
  </script>