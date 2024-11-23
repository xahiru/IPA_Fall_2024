<script setup>
import Navbar from './Navbar.vue';
</script>

<template>
  <div id="settings">
    <Navbar />
    <h1 class="title">Settings Panel</h1>
    <p class="subtitle">Set thresholds and control alerts dynamically.</p>

    <form class="settings-form">
      
      <div class="form-group">
        <label for="temperature">Temperature Threshold (°C):</label>
        <input type="number" id="temperature" class="input-field" />
        <div class="toggle">
          <input type="checkbox" id="temperature-alert"/>
          <label for="temperature-alert">Enable Temperature Alerts</label>
        </div>
      </div>

      
      <div class="form-group">
        <label for="humidity">Humidity Threshold (%):</label>
        <input type="number" id="humidity" class="input-field" />
        <div class="toggle">
          <input type="checkbox" id="humidity-alert"/>
          <label for="humidity-alert">Enable Humidity Alerts</label>
        </div>
      </div>

      
      <div class="form-group">
        <label for="light">Light Threshold (lux):</label>
        <input type="number" id="light" class="input-field" />
        <div class="toggle">
          <input type="checkbox" id="light-alert"/>
          <label for="light-alert">Enable Light Alerts</label>
        </div>
      </div>

      
      <div class="form-group">
        <label for="moisture">Moisture Threshold (%):</label>
        <input type="number" id="moisture" class="input-field" />
        <div class="toggle">
          <input type="checkbox"/>
          <label for="moisture-alert">Enable Moisture Alerts</label>
        </div>
      </div>

      <button type="submit" class="button save-button">Save Settings</button>
    </form>


  </div>
</template>

<style scoped>
#settings {
  font-family: 'Roboto', sans-serif;
  max-width: 600px;
  margin: 2rem auto;
  padding: 2rem;
  background: white;
  border-radius: 10px;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
}


.title {
  font-size: 2rem;
  color: #34495e;
  margin-bottom: 0.5rem;
  text-align: center;
}

.subtitle {
  font-size: 1rem;
  color: #7f8c8d;
  margin-bottom: 2rem;
  text-align: center;
}


.settings-form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.form-group {
  display: flex;
  flex-direction: column;
}

label {
  font-size: 1rem;
  margin-bottom: 0.5rem;
  color: #2c3e50;
}

.input-field {
  padding: 10px;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
  outline: none;
}

.input-field:focus {
  border-color: #3498db;
  box-shadow: 0 0 5px rgba(52, 152, 219, 0.5);
}


.active-alert {
  margin-top: 1.5rem;
  padding: 1rem;
  font-size: 1.2rem;
  color: #ffffff;
  background-color: #e74c3c;
  border-radius: 5px;
  text-align: center;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}


.button {
  padding: 12px;
  font-size: 1rem;
  font-weight: 600;
  color: white;
  background-color: #3498db;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.button:hover {
  background-color: #2980b9;
}
</style>
