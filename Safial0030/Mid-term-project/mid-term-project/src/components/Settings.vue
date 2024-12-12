<!-- eslint-disable vue/multi-word-component-names -->
<template>
    <div class="background-image">
    <div class="container settings-content">
      <h1 class="text-center mb-4">Settings</h1>
      <div class="card shadow">
        <div class="card-body">
          <form @submit.prevent="saveSettings">
            <div class="mb-3">
              <label for="temperatureThreshold" class="form-label">Temperature Alert Threshold (°C)</label>
              <input
                type="number"
                id="temperatureThreshold"
                class="form-control"
                placeholder="Set temperature threshold"
                required
              />
            </div>
            <div class="mb-3">
              <label for="humidityThreshold" class="form-label">Humidity Alert Threshold (%)</label>
              <input
                type="number"
                id="humidityThreshold"
                class="form-control"
                placeholder="Set humidity threshold"
                required
              />
            </div>
            <button type="submit" class="btn btn-primary w-100">Save Settings</button>
          </form>
        </div>
      </div>
    </div>
  </div>
  </template>
  
  <script>
  export default {
    methods: {
      saveSettings() {
        alert('Settings saved successfully!'); // Show success alert
        this.$router.push('/dashboard'); // Navigate to the Dashboard page
      },
    },
  };
  </script>
  
  <style scoped>
  .settings-content {
    margin-top: 100px; /* Adjust this value according to the navbar height */
    width: 450px; /* Adjust the width to your desired value */
  }
  
  .card {
    border-radius: 10px;
    border-color: #007bff92;
    height: 300px;
  }
  
  .card-body {
    border-radius: 10px;
    background-color: #009220c5; /* background for card */
  }
  
  .btn-primary {
    background-color: #007bff;
    border-color: #007bff;
    transition: background-color 0.3s, border-color 0.3s;
  }
  
  .btn-primary:hover {
    background-color: #0056b3;
    border-color: #0056b3;
  }
  </style>
  <style scoped>
  .background-image {
    background-image: url('/src/assets/set.jpg');
    background-size: cover;
    background-position: right;
    min-height: 87vh; /* Sets the minimum height to fill the viewport */
    
  }
  </style>