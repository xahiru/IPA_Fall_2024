<template>
    <div class="settings-panel">
      <h2>Settings Panel</h2>
      <form @submit.prevent="saveSettings">

        <div class="setting">
          <label for="temperature-threshold">Temperature Alert Threshold (°C):</label>
          <input
            id="temperature-threshold"
            type="number"
            v-model="thresholds.temperature"
          />
        </div>

        <div class="setting">
          <label for="humidity-threshold">Humidity Alert Threshold (%):</label>
          <input
            id="humidity-threshold"
            type="number"
            v-model="thresholds.humidity"
          />
        </div>

        <div class="setting">
          <label for="soil-moisture-threshold">Soil Moisture Alert Threshold (%):</label>
          <input
            id="soil-moisture-threshold"
            type="number"
            v-model="thresholds.soilMoisture"
          />
        </div>

        <div class="setting">
          <label for="light-level-threshold">Light Level Alert Threshold (lux):</label>
          <input
            id="light-level-threshold"
            type="number"
            v-model="thresholds.lightLevel"
          />
        </div>
  
        <button type="submit">Save Settings</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: "SettingsPanel",
    data() {
      return {
        thresholds: {
          temperature: 28,
          humidity: 65,
          soilMoisture: 40,
          lightLevel: 300,
        },
      };
    },
    methods: {
      saveSettings() {
        alert("Settings saved!");
        console.log("Updated thresholds:", this.thresholds);
      },
    },
  };
  </script>
  
  <style scoped>
  .settings-panel {
    padding: 1.5rem;
    background-color: #f9f9f9;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    max-width: 500px;
    margin: auto;
  }
  
  h2 {
    margin-bottom: 1.5rem;
    color: #333;
  }
  
  form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }
  
  .setting {
    display: flex;
    flex-direction: column;
  }
  
  label {
    margin-bottom: 0.5rem;
    font-weight: bold;
    color: #555;
  }
  
  input {
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  button {
    padding: 0.75rem 1.5rem;
    background-color: #4caf50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  button:hover {
    background-color: #45a049;
  }
  </style>