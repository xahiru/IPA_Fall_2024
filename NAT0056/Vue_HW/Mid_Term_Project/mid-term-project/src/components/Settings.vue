<template>
  <div class="settings-panel">
    <h2>Greenhouse Alert Thresholds</h2>

    <!-- Temperature Alert Threshold -->
    <div class="setting-option">
      <label for="temperature-threshold">Temperature Alert Threshold (°C)</label>
      <div class="input-group">
        <input 
          type="number" 
          id="temperature-threshold" 
          v-model="temperatureThreshold" 
          min="-50" 
          max="100"
          :class="{'error-input': temperatureThreshold < -50 || temperatureThreshold > 100}" 
          placeholder="Temperature in °C" 
        />
        <span>°C</span>
      </div>
      <p class="info-text">Set the maximum and minimum temperature limits for alerts.</p>
      <p v-if="temperatureThreshold < -50 || temperatureThreshold > 100" class="error-text">Temperature must be between -50°C and 100°C.</p>
    </div>

    <!-- Humidity Alert Threshold -->
    <div class="setting-option">
      <label for="humidity-threshold">Humidity Alert Threshold (%)</label>
      <div class="input-group">
        <input 
          type="number" 
          id="humidity-threshold" 
          v-model="humidityThreshold" 
          min="0" 
          max="100"
          :class="{'error-input': humidityThreshold < 0 || humidityThreshold > 100}"
          placeholder="Humidity in %" 
        />
        <span>%</span>
      </div>
      <p class="info-text">Set the maximum and minimum humidity levels for alerts.</p>
      <p v-if="humidityThreshold < 0 || humidityThreshold > 100" class="error-text">Humidity must be between 0% and 100%.</p>
    </div>

    <!-- CO2 Level Alert Threshold -->
    <div class="setting-option">
      <label for="co2-threshold">CO2 Alert Threshold (ppm)</label>
      <div class="input-group">
        <input 
          type="number" 
          id="co2-threshold" 
          v-model="co2Threshold" 
          min="300" 
          max="2000"
          :class="{'error-input': co2Threshold < 300 || co2Threshold > 2000}"
          placeholder="CO2 in ppm" 
        />
        <span>ppm</span>
      </div>
      <p class="info-text">Set the CO2 level for alert thresholds (in parts per million).</p>
      <p v-if="co2Threshold < 300 || co2Threshold > 2000" class="error-text">CO2 level must be between 300ppm and 2000ppm.</p>
    </div>

    <!-- Save Button -->
    <div class="setting-option">
      <button @click="saveSettings" :disabled="isSaveDisabled" class="button">Save Settings</button>
    </div>

    <!-- Display Alert Settings (optional) -->
    <div class="alert-display">
      <h3>Current Alert Settings:</h3>
      <p><strong>Temperature Threshold:</strong> {{ temperatureThreshold }} °C</p>
      <p><strong>Humidity Threshold:</strong> {{ humidityThreshold }} %</p>
      <p><strong>CO2 Threshold:</strong> {{ co2Threshold }} ppm</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SettingsPanel',
  data() {
    return {
      temperatureThreshold: 30,
      humidityThreshold: 60,
      co2Threshold: 1000,
    };
  },
  computed: {
    isSaveDisabled() {
      return (
        this.temperatureThreshold < -50 || this.temperatureThreshold > 100 ||
        this.humidityThreshold < 0 || this.humidityThreshold > 100 ||
        this.co2Threshold < 300 || this.co2Threshold > 2000
      );
    }
  },
  methods: {
    saveSettings() {
      localStorage.setItem('temperatureThreshold', this.temperatureThreshold);
      localStorage.setItem('humidityThreshold', this.humidityThreshold);
      localStorage.setItem('co2Threshold', this.co2Threshold);

      alert('Settings saved!');
    },
  },
  mounted() {
    const savedTemperatureThreshold = localStorage.getItem('temperatureThreshold');
    const savedHumidityThreshold = localStorage.getItem('humidityThreshold');
    const savedCO2Threshold = localStorage.getItem('co2Threshold');

    if (savedTemperatureThreshold) {
      this.temperatureThreshold = savedTemperatureThreshold;
    }
    if (savedHumidityThreshold) {
      this.humidityThreshold = savedHumidityThreshold;
    }
    if (savedCO2Threshold) {
      this.co2Threshold = savedCO2Threshold;
    }
  },
};
</script>

<style scoped>
/* Full Page Gradient Background */
body {
  background: linear-gradient(#1f7439, #132c5f, #371156); /* Light gradient from top left to bottom right */
  margin: 0;
  padding: 0;
  font-family: 'Roboto', sans-serif;
  height: 90vh; /* Ensure full viewport height */
}

.settings-panel {
  padding: 30px;
  background-color: linear-gradient(#3c453fd6, #d5c389d5, #5316869a);
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(104, 21, 21, 0.795);
  width: 100%;
  max-width: 400px;
  margin: 20px auto;
}

h2 {
  text-align: center;
  color: #412e2e;
  margin-bottom: 20px;
}

.setting-option {
  margin-bottom: 25px;
}

label {
  font-weight: 600;
  color: #133c9a;
  margin-bottom: 8px;
  display: block;
}

.input-group {
  display: flex;
  align-items: center;
  border: 1px solid #ddd;
  border-radius: 5px;
  padding: 5px;
}

input {
  padding: 10px;
  border: none;
  outline: none;
  flex-grow: 1;
  font-size: 16px;
}

input.error-input {
  border: 1px solid rgb(139, 49, 49);
}

span {
  margin-left: 10px;
  font-size: 16px;
  color: #723d3d;
}

button {
  padding: 12px 20px;
  font-size: 1rem;
  font-weight: 600;
  color: rgb(230, 210, 210);
  background: linear-gradient(90deg, #6c63ff, #a084dc);
  border: none;
  cursor: pointer;
  border-radius: 8px;
  transition: transform 0.2s, background-color 0.3s;
}

button:hover {
  transform: scale(1.05);
  background: linear-gradient(90deg, #076322, #26a60d);
}

button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

.info-text {
  font-size: 14px;
  color: #666;
  background-color: #f1f1f1;
  padding: 8px;
  border-radius: 5px;
}

.error-text {
  font-size: 14px;
  color: rgb(238, 111, 111);
  margin-top: 5px;
  background-color: #867f7f;
  padding: 8px;
  border-radius: 5px;
}

.alert-display {
  margin-top: 30px;
  padding: 10px;
  background-color: #96c3c9;
  border-radius: 8px;
}
</style>
