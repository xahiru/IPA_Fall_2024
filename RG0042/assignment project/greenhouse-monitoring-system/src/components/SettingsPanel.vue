<template>
  <div class="settings-panel-wrapper">
    <div class="settings-panel">
      <h2>Configure Alert Settings</h2>
      <form @submit.prevent="saveSettings">

        <div class="setting">
          <label for="temperature">Temperature (°C)</label>
          <input
            id="temperature"
            type="number"
            v-model="localThresholds.temperature"
            :disabled="!thresholdsEnabled"
            @input="onFieldChange('temperature')"
          />
        </div>

        <div class="setting">
          <label for="humidity">Humidity (%)</label>
          <input
            id="humidity"
            type="number"
            v-model="localThresholds.humidity"
            :disabled="!thresholdsEnabled"
            @input="onFieldChange('humidity')"
          />
        </div>


        <div class="setting">
          <label for="soil-moisture">Soil Moisture (%)</label>
          <input
            id="soil-moisture"
            type="number"
            v-model="localThresholds.soilMoisture"
            :disabled="!thresholdsEnabled"
            @input="onFieldChange('soilMoisture')"
          />
        </div>


        <div class="setting">
          <label for="light-level">Light Level (lux)</label>
          <input
            id="light-level"
            type="number"
            v-model="localThresholds.lightLevel"
            :disabled="!thresholdsEnabled"
            @input="onFieldChange('lightLevel')"
          />
        </div>

        <div class="checkbox-group">
          <label>
            <input
              type="checkbox"
              v-model="thresholdsEnabled"
              @change="toggleThresholds"
            />
            Enable All Thresholds
          </label>
        </div>

        <button type="submit" class="save-btn">Save</button>
        <button type="button" class="cancel-btn" @click="cancelSettings">
          Reset
        </button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "SettingsPanel",
  props: {
    thresholds: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      localThresholds: { ...this.thresholds },
      thresholdsEnabled: true,
    };
  },
  methods: {
    saveSettings() {
      alert("Settings saved!");
      console.log("Updated thresholds:", this.localThresholds);
    },
    cancelSettings() {
      alert("Settings reset to defaults.");
      this.localThresholds = { ...this.thresholds };
      this.thresholdsEnabled = true;
    },
    toggleThresholds() {
      console.log("Thresholds enabled:", this.thresholdsEnabled);
    },
    onFieldChange(field) {
      console.log(`Updated field: ${field}, Value: ${this.localThresholds[field]}`);
    },
  },
};
</script>

<style scoped>
.settings-panel-wrapper {
  display: grid;
  place-items: center;
  min-height: 100vh;
  background-color: #f4f5f7;
  background-image: url("src/assets/setting-background.jpg");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.settings-panel {
  padding: 2rem;
  background-color: #ffffff;
  border-radius: 10px;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
  width: 90%;
  max-width: 400px;
  animation: fadeIn 0.5s ease-in-out;
}

h2 {
  text-align: center;
  font-size: 1.5rem;
  color: #333333;
  margin-bottom: 1rem;
}

form {
  display: grid;
  gap: 1rem;
}

.setting {
  display: grid;
  gap: 0.5rem;
}

label {
  font-size: 0.9rem;
  font-weight: 600;
  color: #555555;
}

input[type="number"] {
  padding: 0.5rem;
  border: 1px solid #cccccc;
  border-radius: 6px;
  font-size: 0.9rem;
  transition: border-color 0.3s;
}

input[type="number"]:hover,
input[type="number"]:focus {
  border-color: #007bff;
  outline: none;
}

.checkbox-group label {
  font-size: 0.9rem;
  font-weight: 600;
  color: #555555;
  display: flex;
  align-items: center;
}

input[type="checkbox"] {
  margin-right: 0.5rem;
}

.button-group {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.5rem;
}

button {
  padding: 0.75rem;
  font-size: 1rem;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: transform 0.3s, background-color 0.3s;
}

.save-btn {
  background-color: #007bff;
  color: white;
}

.save-btn:hover {
  background-color: #0056b3;
  transform: scale(1.05);
}

.cancel-btn {
  background-color: #dc3545;
  color: white;
}

.cancel-btn:hover {
  background-color: #c82333;
  transform: scale(1.05);
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>