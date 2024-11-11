<script setup>
import { ref } from 'vue';

const temperatureThreshold = ref(30);
const humidityThreshold = ref(70);
const moistureThreshold = ref(50);
const lightThreshold = ref(400);


const saveSettings = () => {
  console.log("Settings saved:");
  console.log({
    temperatureThreshold: temperatureThreshold.value,
    humidityThreshold: humidityThreshold.value,
    moistureThreshold: moistureThreshold.value,
    lightThreshold: lightThreshold.value
  });
};
</script>

<template>
  <div id="settings">
    <nav class="navbar">
      <div class="logo">Greenhouse</div>
      <ul class="nav-links">
        <li><router-link to="/over-view">Overview</router-link></li>
        <li><router-link to="/dashboard">Dashboard</router-link></li>
        <li><a @click="logout">Logout</a></li>
      </ul>
    </nav>

    <main>
      <header>
        <h1>Settings</h1>
        <p>Set Alert Thresholds for Greenhouse Monitoring</p>
      </header>

      <section class="settings-panel">
        <form @submit.prevent="saveSettings">
          <div class="form-group">
            <label for="temperature">Temperature Threshold (°C)</label>
            <input
              type="number"
              id="temperature"
              v-model="temperatureThreshold"
              min="0"
              step="0.1"
              class="form-input"
            />
          </div>

          <div class="form-group">
            <label for="humidity">Humidity Threshold (%)</label>
            <input
              type="number"
              id="humidity"
              v-model="humidityThreshold"
              min="0"
              max="100"
              class="form-input"
            />
          </div>

          <div class="form-group">
            <label for="moisture">Soil Moisture Threshold (%)</label>
            <input
              type="number"
              id="moisture"
              v-model="moistureThreshold"
              min="0"
              max="100"
              class="form-input"
            />
          </div>

          <div class="form-group">
            <label for="light">Light Level Threshold (lux)</label>
            <input
              type="number"
              id="light"
              v-model="lightThreshold"
              min="0"
              step="1"
              class="form-input"
            />
          </div>

          <button type="submit" class="save-button">Save Settings</button>
        </form>
      </section>
    </main>
  </div>
</template>

<style scoped>
/* Basic styling for settings panel */
body {
  font-family: 'Roboto', sans-serif;
  background: #f4f6f9;
  color: #333;
}

.navbar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.2rem 2rem;
  background: #2d3e50;
  color: white;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  z-index: 100;
}

.logo {
  font-size: 1.8rem;
  font-weight: bold;
  letter-spacing: 1px;
}

.nav-links {
  list-style: none;
  display: flex;
  gap: 30px;
}

.nav-links li a {
  text-decoration: none;
  color: white;
  font-size: 1.1rem;
  font-weight: 500;
  transition: color 0.3s ease;
}

.nav-links li a:hover {
  color: #3498db;
}

main {
  padding: 2rem 3rem;
}

header h1 {
  font-size: 2.5rem;
  font-weight: 700;
  color: #34495e;
  margin-bottom: 10px;
}

header p {
  font-size: 1.1rem;
  color: #7f8c8d;
  font-weight: 300;
}

.settings-panel {
  background: white;
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  margin-top: 30px;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  font-size: 1.2rem;
  display: block;
  margin-bottom: 10px;
}

.form-input {
  width: 100%;
  padding: 10px;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-top: 5px;
}

.save-button {
  padding: 12px 20px;
  background: #3498db;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 1.2rem;
  cursor: pointer;
}

.save-button:hover {
  background: #2980b9;
}

@media (max-width: 768px) {
  .settings-panel {
    padding: 1.5rem;
  }

  .form-group label {
    font-size: 1rem;
  }

  .form-input {
    padding: 8px;
    font-size: 0.9rem;
  }

  .save-button {
    padding: 10px 18px;
    font-size: 1rem;
  }
}
</style>
