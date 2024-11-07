<template>
  <v-container fluid class="animate-fade-in">
    <v-row>
      <v-col cols="12">
        <h1 class="text-h4 mb-6 text-primary font-weight-bold d-flex align-center">
          <v-icon size="36" color="primary" class="mr-2">mdi-cog-outline</v-icon>
          Greenhouse Controls
        </h1>
      </v-col>
    </v-row>

    <v-card class="mx-auto pa-6" elevation="8">
      <v-form @submit.prevent="saveSettings">
        <v-row>
          <v-col cols="12" md="6">
            <v-card class="setting-card" elevation="2">
              <v-slider
                v-model="settings.temperatureThreshold"
                color="red"
                label="Temperature Threshold"
                :min="15"
                :max="35"
                thumb-label="always"
                :thumb-size="24"
                show-ticks
              >
                <template v-slot:prepend>
                  <v-icon color="red">mdi-thermometer</v-icon>
                </template>
                <template v-slot:append>
                  {{ settings.temperatureThreshold }}°C
                </template>
              </v-slider>
            </v-card>
          </v-col>

          <v-col cols="12" md="6">
            <v-card class="setting-card" elevation="2">
              <v-slider
                v-model="settings.humidityThreshold"
                color="blue"
                label="Humidity Threshold"
                :min="30"
                :max="90"
                thumb-label="always"
                :thumb-size="24"
                show-ticks
              >
                <template v-slot:prepend>
                  <v-icon color="blue">mdi-water</v-icon>
                </template>
                <template v-slot:append>
                  {{ settings.humidityThreshold }}%
                </template>
              </v-slider>
            </v-card>
          </v-col>

          <v-col cols="12" md="6">
            <v-card class="setting-card" elevation="2">
              <v-slider
                v-model="settings.soilMoistureThreshold"
                color="brown"
                label="Soil Moisture Threshold"
                :min="20"
                :max="80"
                thumb-label="always"
                :thumb-size="24"
                show-ticks
              >
                <template v-slot:prepend>
                  <v-icon color="brown">mdi-water-percent</v-icon>
                </template>
                <template v-slot:append>
                  {{ settings.soilMoistureThreshold }}%
                </template>
              </v-slider>
            </v-card>
          </v-col>

          <v-col cols="12" md="6">
            <v-card class="setting-card" elevation="2">
              <v-slider
                v-model="settings.lightLevelThreshold"
                color="orange"
                label="Light Level Threshold"
                :min="500"
                :max="2000"
                step="100"
                thumb-label="always"
                :thumb-size="24"
                show-ticks
              >
                <template v-slot:prepend>
                  <v-icon color="orange">mdi-white-balance-sunny</v-icon>
                </template>
                <template v-slot:append>
                  {{ settings.lightLevelThreshold }} lux
                </template>
              </v-slider>
            </v-card>
          </v-col>
        </v-row>

        <v-card-actions class="justify-center mt-6">
          <v-btn
            color="primary"
            type="submit"
            size="x-large"
            :loading="saving"
            class="px-8"
          >
            <v-icon start>mdi-content-save</v-icon>
            Save Settings
          </v-btn>
        </v-card-actions>
      </v-form>
    </v-card>

    <v-snackbar
      v-model="showSnackbar"
      color="success"
      timeout="3000"
    >
      Settings saved successfully!
    </v-snackbar>
  </v-container>
</template>

<script setup>
import { ref } from 'vue'

const saving = ref(false)
const showSnackbar = ref(false)
const settings = ref({
  temperatureThreshold: 25,
  humidityThreshold: 60,
  soilMoistureThreshold: 45,
  lightLevelThreshold: 1000
})

const saveSettings = async () => {
  saving.value = true
  await new Promise(resolve => setTimeout(resolve, 1000))
  localStorage.setItem('greenhouseSettings', JSON.stringify(settings.value))
  saving.value = false
  showSnackbar.value = true
}
</script>

<style scoped>
.setting-card {
  padding: 16px;
  transition: all 0.3s ease;
}

.setting-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.animate-fade-in {
  animation: fadeIn 0.5s ease-in;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>