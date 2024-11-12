<template>
    <div class="settings">
      <h3>Settings</h3>
      <form @submit.prevent="saveSettings">
        <div class="form-group">
          <label for="temperature">Temperature Threshold (°C)</label>
          <input
            type="number"
            id="temperature"
            v-model="settings.temperature"
            min="0"
            step="0.1"
            required
          />
        </div>
  
        <div class="form-group">
          <label for="humidity">Humidity Threshold (%)</label>
          <input
            type="number"
            id="humidity"
            v-model="settings.humidity"
            min="0"
            max="100"
            step="1"
            required
          />
        </div>
  
        <div class="form-group">
          <label for="soilMoisture">Soil Moisture Threshold (%)</label>
          <input
            type="number"
            id="soilMoisture"
            v-model="settings.soilMoisture"
            min="0"
            max="100"
            step="1"
            required
          />
        </div>
  
        <div class="form-group">
          <label for="lightLevel">Light Level Threshold (Lux)</label>
          <input
            type="number"
            id="lightLevel"
            v-model="settings.lightLevel"
            min="0"
            step="10"
            required
          />
        </div>
  
        <button type="submit" class="save-button">Save Settings</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: "Settings",
    data() {
      return {
        // these values can be loaded dynamically from a server if needed
        settings: {
          temperature: 25.0,
          humidity: 60,
          soilMoisture: 30,
          lightLevel: 500,
        },
      };
    },
    methods: {
      saveSettings() {
        // Here you would handle saving the settings, e.g., making an API call or storing in local storage
        console.log('Settings saved:', this.settings);
        alert('Settings have been saved!');
      },
    },
  };
  </script>
  
  <style scoped>
  .settings {
    background-color: #fff;
    padding: 30px;
    border-radius: 8px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    max-width: 600px;
    margin: 0 auto;
  }
  
  h3 {
    text-align: center;
    margin-bottom: 20px;
  }
  
  .form-group {
    margin-bottom: 20px;
  }
  
  label {
    display: block;
    font-size: 16px;
    margin-bottom: 5px;
  }
  
  input {
    width: 100%;
    padding: 10px;
    font-size: 14px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  button.save-button {
    display: block;
    width: 100%;
    padding: 10px;
    background-color: #4CAF50;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
  }
  
  button.save-button:hover {
    background-color: #45a049;
  }
  </style>
  