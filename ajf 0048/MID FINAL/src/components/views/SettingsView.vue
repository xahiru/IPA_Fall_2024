<template>
    <v-container fluid class="settings-container">
      <v-row>
      <v-col cols="12">
        <h2 color="primary" class="mr-2">Settings</h2>
      </v-col>
    </v-row>
      <v-row>
        <v-col cols="12" md="8" lg="6">
          <v-card class="settings-card">
            <v-card-title class="text-h4 d-flex align-center">
              <v-icon size="36" color="primary" class="mr-2">mdi-cog</v-icon>
              Alert Thresholds
            </v-card-title>

        
          <v-tabs v-model="activeTab">
            <v-tab value="thresholds">Sensor Thresholds</v-tab>
            <v-tab value="alerts">Alert Settings</v-tab>
            <v-tab value="schedule">Watering Schedule</v-tab>
          </v-tabs>
         
              
      <v-card-text>
        <v-window v-model="activeTab">
              <!-- Sensor Thresholds -->
              <v-window-item value="thresholds">
              <v-form v-model="valid" @submit.prevent="saveSettings">
                <v-slider
                  v-model="thresholds.temperature"
                  label="Temperature Alert (°C)"
                  min="15"
                  max="35"
                  thumb-label
                  class="mb-4"
                ></v-slider>
  
                <v-slider
                  v-model="thresholds.humidity"
                  label="Humidity Alert (%)"
                  min="30"
                  max="90"
                  thumb-label
                  class="mb-4"
                ></v-slider>
  
                <v-slider
                  v-model="thresholds.soilMoisture"
                  label="Soil Moisture Alert (%)"
                  min="20"
                  max="80"
                  thumb-label
                  class="mb-4"
                ></v-slider>
              </v-form>
            </v-window-item>

          <!-- Alert Settings -->
           <v-window-item value="alerts">
                <v-list>
                  <v-list-item>
                    <v-switch
                      v-model="alerts.email"
                      label="Email Alerts"
                    ></v-switch>
                  </v-list-item>
                  <v-list-item>
                    <v-switch
                      v-model="alerts.critical"
                      label="Critical Notifications"
                    ></v-switch>
                  </v-list-item>
                </v-list>
              </v-window-item>

              <!-- Watering Schedule -->
              <v-window-item value="schedule">
                <v-form class="mt-4">
                  <v-select
                    v-model="schedule.frequency"
                    :items="['Daily', 'Every 2 Days', 'Weekly']"
                    label="Watering Frequency"
                  ></v-select>
                  
                  <v-text-field
                    v-model="schedule.duration"
                    label="Duration (minutes)"
                    type="number"
                  ></v-text-field>
                </v-form>
              </v-window-item>
            </v-window>
          </v-card-text>

          <v-card-actions>
            <v-spacer></v-spacer>
                <v-btn
                  type="submit"
                  color="primary"
                  block
                  :loading="saving"
                  @click="saveSettings"
                >
                  Save Settings
                </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
  
  <script setup>
  import { ref } from 'vue'
  
  const activeTab = ref('profile')

  
  const thresholds = ref({
  temperature: 25,
  humidity: 60,
  soilMoisture: 70
})

const alerts = ref({
  email: true,
  critical: true
})

const schedule = ref({
  frequency: 'Daily',
  duration: 15
})

const saveSettings = () => {
  // Implementation for saving settings
}
</script>

<style scoped>
.settings-container {
  padding: 24px;
}

.settings-card {
  background: rgba(255, 255, 255, 0.15) !important;
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.gradient-text {
  background: linear-gradient(45deg, #FC466B, #3F5EFB);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  font-weight: bold;
}
</style>