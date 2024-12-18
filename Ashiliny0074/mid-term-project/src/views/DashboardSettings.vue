<template>
  <div class="p-6">
    <div class="md:flex md:items-center md:justify-between mb-6">
      <h2 class="text-2xl font-bold leading-7 text-gray-900 sm:text-3xl">Settings</h2>
      <div class="mt-4 flex md:mt-0 md:ml-4">
        <button
          type="button"
          @click="saveSettings"
          :disabled="loading"
          class="inline-flex items-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
        >
          {{ loading ? 'Saving...' : 'Save Changes' }}
        </button>
      </div>
    </div>

    <!-- Success/Error Messages -->
    <div v-if="message" :class="`mb-4 p-4 rounded-md ${message.type === 'success' ? 'bg-green-50 text-green-700' : 'bg-red-50 text-red-700'}`">
      {{ message.text }}
    </div>

    <!-- Settings Form -->
    <div class="bg-white shadow rounded-lg">
      <div class="px-4 py-5 sm:p-6">
        <div class="grid grid-cols-1 gap-6">
          <!-- Temperature Settings -->
          <div class="space-y-6">
            <h3 class="text-lg font-medium leading-6 text-gray-900">Temperature Thresholds (°C)</h3>
            <div class="grid grid-cols-1 gap-4 sm:grid-cols-2">
              <div>
                <label class="block text-sm font-medium text-gray-700">Minimum Temperature</label>
                <div class="mt-1 relative rounded-md shadow-sm">
                  <input
                    type="number"
                    v-model="settings.temperature.min"
                    step="0.1"
                    class="focus:ring-blue-500 focus:border-blue-500 block w-full pl-3 pr-12 sm:text-sm border-gray-300 rounded-md"
                  />
                  <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                    <span class="text-gray-500 sm:text-sm">°C</span>
                  </div>
                </div>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Maximum Temperature</label>
                <div class="mt-1 relative rounded-md shadow-sm">
                  <input
                    type="number"
                    v-model="settings.temperature.max"
                    step="0.1"
                    class="focus:ring-blue-500 focus:border-blue-500 block w-full pl-3 pr-12 sm:text-sm border-gray-300 rounded-md"
                  />
                  <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                    <span class="text-gray-500 sm:text-sm">°C</span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Humidity Settings -->
          <div class="space-y-6">
            <h3 class="text-lg font-medium leading-6 text-gray-900">Humidity Thresholds (%)</h3>
            <div class="grid grid-cols-1 gap-4 sm:grid-cols-2">
              <div>
                <label class="block text-sm font-medium text-gray-700">Minimum Humidity</label>
                <div class="mt-1 relative rounded-md shadow-sm">
                  <input
                    type="number"
                    v-model="settings.humidity.min"
                    min="0"
                    max="100"
                    class="focus:ring-blue-500 focus:border-blue-500 block w-full pl-3 pr-12 sm:text-sm border-gray-300 rounded-md"
                  />
                  <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                    <span class="text-gray-500 sm:text-sm">%</span>
                  </div>
                </div>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Maximum Humidity</label>
                <div class="mt-1 relative rounded-md shadow-sm">
                  <input
                    type="number"
                    v-model="settings.humidity.max"
                    min="0"
                    max="100"
                    class="focus:ring-blue-500 focus:border-blue-500 block w-full pl-3 pr-12 sm:text-sm border-gray-300 rounded-md"
                  />
                  <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                    <span class="text-gray-500 sm:text-sm">%</span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Soil Moisture Settings -->
          <div class="space-y-6">
            <h3 class="text-lg font-medium leading-6 text-gray-900">Soil Moisture Thresholds (%)</h3>
            <div class="grid grid-cols-1 gap-4 sm:grid-cols-2">
              <div>
                <label class="block text-sm font-medium text-gray-700">Minimum Soil Moisture</label>
                <div class="mt-1 relative rounded-md shadow-sm">
                  <input
                    type="number"
                    v-model="settings.soilMoisture.min"
                    min="0"
                    max="100"
                    class="focus:ring-blue-500 focus:border-blue-500 block w-full pl-3 pr-12 sm:text-sm border-gray-300 rounded-md"
                  />
                  <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                    <span class="text-gray-500 sm:text-sm">%</span>
                  </div>
                </div>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Maximum Soil Moisture</label>
                <div class="mt-1 relative rounded-md shadow-sm">
                  <input
                    type="number"
                    v-model="settings.soilMoisture.max"
                    min="0"
                    max="100"
                    class="focus:ring-blue-500 focus:border-blue-500 block w-full pl-3 pr-12 sm:text-sm border-gray-300 rounded-md"
                  />
                  <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                    <span class="text-gray-500 sm:text-sm">%</span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Light Level Settings -->
          <div class="space-y-6">
            <h3 class="text-lg font-medium leading-6 text-gray-900">Light Level Thresholds (lux)</h3>
            <div class="grid grid-cols-1 gap-4 sm:grid-cols-2">
              <div>
                <label class="block text-sm font-medium text-gray-700">Minimum Light Level</label>
                <div class="mt-1 relative rounded-md shadow-sm">
                  <input
                    type="number"
                    v-model="settings.lightLevel.min"
                    min="0"
                    class="focus:ring-blue-500 focus:border-blue-500 block w-full pl-3 pr-12 sm:text-sm border-gray-300 rounded-md"
                  />
                  <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                    <span class="text-gray-500 sm:text-sm">lux</span>
                  </div>
                </div>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Maximum Light Level</label>
                <div class="mt-1 relative rounded-md shadow-sm">
                  <input
                    type="number"
                    v-model="settings.lightLevel.max"
                    min="0"
                    class="focus:ring-blue-500 focus:border-blue-500 block w-full pl-3 pr-12 sm:text-sm border-gray-300 rounded-md"
                  />
                  <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                    <span class="text-gray-500 sm:text-sm">lux</span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Notification Settings -->
          <div class="space-y-6">
            <h3 class="text-lg font-medium leading-6 text-gray-900">Notification Settings</h3>
            <div class="space-y-4">
              <div class="flex items-start">
                <div class="flex items-center h-5">
                  <input
                    id="alerts"
                    v-model="settings.notifications.alerts"
                    type="checkbox"
                    class="focus:ring-blue-500 h-4 w-4 text-blue-600 border-gray-300 rounded"
                  />
                </div>
                <div class="ml-3 text-sm">
                  <label for="alerts" class="font-medium text-gray-700">Enable Alert Notifications</label>
                  <p class="text-gray-500">Receive notifications when values exceed thresholds</p>
                </div>
              </div>
              <div class="flex items-start">
                <div class="flex items-center h-5">
                  <input
                    id="dailyReport"
                    v-model="settings.notifications.dailyReport"
                    type="checkbox"
                    class="focus:ring-blue-500 h-4 w-4 text-blue-600 border-gray-300 rounded"
                  />
                </div>
                <div class="ml-3 text-sm">
                  <label for="dailyReport" class="font-medium text-gray-700">Daily Report</label>
                  <p class="text-gray-500">Receive daily summary reports</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';

interface ThresholdSettings {
  min: number;
  max: number;
}

interface Settings {
  temperature: ThresholdSettings;
  humidity: ThresholdSettings;
  soilMoisture: ThresholdSettings;
  lightLevel: ThresholdSettings;
  notifications: {
    alerts: boolean;
    dailyReport: boolean;
  };
}

interface Message {
  type: 'success' | 'error';
  text: string;
}

const loading = ref(false);
const message = ref<Message | null>(null);

// Initialize settings with default values
const settings = ref<Settings>({
  temperature: { min: 18, max: 28 },
  humidity: { min: 40, max: 70 },
  soilMoisture: { min: 50, max: 80 },
  lightLevel: { min: 2000, max: 8000 },
  notifications: {
    alerts: true,
    dailyReport: false
  }
});

// Load saved settings on component mount
onMounted(() => {
  const savedSettings = localStorage.getItem('greenhouseSettings');
  if (savedSettings) {
    settings.value = JSON.parse(savedSettings);
  }
});

// Save settings
const saveSettings = async () => {
  loading.value = true;
  message.value = null;

  try {
    // Validate settings
    if (settings.value.temperature.min >= settings.value.temperature.max) {
      throw new Error('Temperature: Minimum must be less than maximum');
    }
    if (settings.value.humidity.min >= settings.value.humidity.max) {
      throw new Error('Humidity: Minimum must be less than maximum');
    }
    if (settings.value.soilMoisture.min >= settings.value.soilMoisture.max) {
      throw new Error('Soil Moisture: Minimum must be less than maximum');
    }
    if (settings.value.lightLevel.min >= settings.value.lightLevel.max) {
      throw new Error('Light Level: Minimum must be less than maximum');
    }

    // Save settings to localStorage
    localStorage.setItem('greenhouseSettings', JSON.stringify(settings.value));

    message.value = {
      type: 'success',
      text: 'Settings saved successfully'
    };
  } catch (err: any) {
    message.value = {
      type: 'error',
      text: err.message || 'Failed to save settings'
    };
  } finally {
    loading.value = false;
    
    // Clear success message after 3 seconds
    if (message.value?.type === 'success') {
      setTimeout(() => {
        message.value = null;
      }, 3000);
    }
  }
};
</script>