<script setup>
import { reactive, onMounted, watch, onUnmounted } from 'vue';

const settings = reactive({
    temperatureThreshold: 30,
    humidityThreshold: 60,
    lightThreshold: 200,
    moistureThreshold: 50,
    alertsEnabled: {
        temperature: true,
        humidity: true,
        light: true,
        moisture: true,
    },
    activeAlert: null,
    simulationFrequency: 5000,
});

const saveSettings = () => {
    localStorage.setItem('alertSettings', JSON.stringify(settings));
    alert("Settings saved successfully!");
};

onMounted(() => {
    const savedSettings = localStorage.getItem('alertSettings');
    if (savedSettings) {
        Object.assign(settings, JSON.parse(savedSettings));
    }
});

const simulateData = () => {
    const simulatedMetrics = [
        { type: 'temperature', value: Math.random() * 50 },
        { type: 'humidity', value: Math.random() * 100 },
        { type: 'light', value: Math.random() * 300 },
        { type: 'moisture', value: Math.random() * 100 },
    ];

    simulatedMetrics.forEach((metric) => {
        const { type, value } = metric;

        if (settings.alertsEnabled[type] && value > settings[`${type}Threshold`]) {
            settings.activeAlert = `⚠️ ${type.toUpperCase()} exceeded! Value: ${value.toFixed(
                1
            )}, Threshold: ${settings[`${type}Threshold`]}`;
        }
    });

    if (
        !simulatedMetrics.some(
            (metric) => settings.alertsEnabled[metric.type] && metric.value > settings[`${metric.type}Threshold`]
        )
    ) {
        settings.activeAlert = null;
    }
};

let simulationInterval = null;
const startSimulation = () => {
    stopSimulation();
    simulationInterval = setInterval(simulateData, settings.simulationFrequency);
};

const stopSimulation = () => {
    if (simulationInterval) {
        clearInterval(simulationInterval);
        simulationInterval = null;
    }
};

onMounted(startSimulation);
onUnmounted(stopSimulation);

watch(
    () => settings.simulationFrequency,
    () => {
        startSimulation();
    }
);
</script>

<template>
  <div id="settings">
    <div class="abstract-background"></div>

    <nav class="navbar">
      <div class="logo">Greenhouse Dashboard</div>
      <ul class="nav-links">
        <li><router-link to="/dashboard">Home</router-link></li>
        <li><router-link to="/over-view">Overview</router-link></li>
        <li><router-link to="/settings">Settings</router-link></li>
        <li><router-link to="/historical-data-chart">Logs</router-link></li>
        <li><a @click="logout">Logout</a></li>
      </ul>
    </nav>

    <main>
      <header>
        <h1>Settings</h1>
        <p>Configure alert thresholds and monitoring preferences for your greenhouse.</p>
      </header>

      <form class="settings-form" @submit.prevent="saveSettings">
        <div
          class="form-group"
          v-for="(enabled, key) in settings.alertsEnabled"
          :key="key"
        >
          <div class="input-group">
            <label :for="key">{{ key.charAt(0).toUpperCase() + key.slice(1) }} Threshold:</label>
            <input
              type="number"
              :id="key"
              v-model="settings[`${key}Threshold`]"
              min="0"
              class="input-field"
            />
          </div>
          <div class="toggle">
            <input
              type="checkbox"
              :id="`${key}-alert`"
              v-model="settings.alertsEnabled[key]"
            />
            <label :for="`${key}-alert`">Enable Alerts</label>
          </div>
        </div>

        <div class="form-group">
          <div class="input-group">
            <label for="frequency">Simulation Frequency (ms):</label>
            <input
              type="number"
              id="frequency"
              v-model="settings.simulationFrequency"
              min="1000"
              class="input-field"
            />
          </div>
        </div>

        <button type="submit" class="button save-button">
          Save Settings
        </button>
      </form>

      <div v-if="settings.activeAlert" class="active-alert">
        {{ settings.activeAlert }}
      </div>
    </main>
  </div>
</template>

<style scoped>
/* General Styling */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Roboto', sans-serif;
  background: #f4f7fa;
  color: #333;
}

/* Abstract Background */
.abstract-background {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #ff8a00, #e52e71, #8921aa);
  z-index: -1;
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
  background: rgba(255, 255, 255, 0.9);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.nav-links li a {
  font-size: 1rem;
  color: #333;
  text-decoration: none;
  transition: color 0.3s;
}

.nav-links li a:hover {
  color: #e52e71;
}

main {
  padding: 2rem;
  margin-top: 80px;
}

header h1 {
  font-size: 2.5rem;
  color: #ffffff;
}

header p {
  font-size: 1rem;
  color: rgba(255, 255, 255, 0.7);
}

.settings-form {
  max-width: 700px;
  margin: 2rem auto;
  background: #ffffff;
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15);
}

.form-group {
  margin-bottom: 1.5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.input-group label {
  font-size: 1rem;
  color: #34495e;
}

.input-field {
  width: 100px;
  padding: 0.4rem;
  border: 1px solid #e0e0e0;
  border-radius: 5px;
}

.toggle input {
  margin-right: 10px;
}

.button {
  display: inline-block;
  background-color: #2ecc71;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 0.8rem 1.2rem;
  cursor: pointer;
  transition: background 0.3s;
}

.button:hover {
  background-color: #27ae60;
}

.active-alert {
  margin-top: 1rem;
  padding: 1rem;
  background: #e74c3c;
  color: #fff;
  border-radius: 8px;
  font-size: 1rem;
  text-align: center;
}
</style>