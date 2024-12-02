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
    <nav class="navbar">
      <div class="logo">Greenhouse</div>
      <ul class="nav-links">
        <li><router-link to="/dashboard">Home</router-link></li>
        <li><router-link to="/over-view">Overview</router-link></li>
        <li><router-link to="/settings">Settings</router-link></li>
        <li><router-link to="/logs">Logs</router-link></li>
        <li><a @click="logout">Logout</a></li>
      </ul>
    </nav>

    <main>
      <header>

      </header>

      <form class="settings-form" @submit.prevent="saveSettings">
        <div class="form-group" v-for="(threshold, key) in settings.alertsEnabled" :key="key">
          <label :for="key">{{ key.charAt(0).toUpperCase() + key.slice(1) }}:</label>
          <input
            type="number"
            :id="key"
            v-model="settings[`${key}Threshold`]"
            min="0"
            class="input-field"
          />
          <div class="toggle">
            <input
              type="checkbox"
              :id="`${key}-alert`"
              v-model="settings.alertsEnabled[key]"
            />
            <label :for="`${key}-alert`">Enable {{ key.charAt(0).toUpperCase() + key.slice(1) }} Alerts</label>
          </div>
        </div>

        <div class="form-group">
          <label for="frequency">Simulation Frequency (ms):</label>
          <input
            type="number"
            id="frequency"
            v-model="settings.simulationFrequency"
            min="1000"
            class="input-field"
          />
        </div>

        <button type="submit" class="button save-button">Set thresholds and enable alerts for monitoring</button>
      </form>

      <div v-if="settings.activeAlert" class="active-alert">
        {{ settings.activeAlert }}
      </div>
    </main>
  </div>
</template>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.dashboard {
  position: relative;
  background-color: #f4f7fc;
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
}

.navbar {
  position: fixed;
  top: 0;
  left: 0;
  height: 10%;
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.2rem 2rem;
  background-color: #34495e;
  color: #ffffff;
  border-bottom: 1px solid #2c3e50;
  box-shadow: 0 3px 5px rgba(0, 0, 0, 0.1);
  z-index: 100;
}

.logo {
  font-size: 2rem;
  font-weight: bold;
  color: #ffffff;
}

.nav-links {
  list-style: none;
  display: flex;
  gap: 20px;
}

.nav-links li a {
  text-decoration: none;
  color: #ecf0f1;
  font-size: 1rem;
  transition: color 0.3s ease;
}

.nav-links li a:hover {
  color: #1abc9c;
}

main {
  padding: 2rem 3rem;
}

header h1 {
  font-size: 2rem;
  font-weight: bold;
  color: #2c3e50;
}

header p {
  font-size: 1.2rem;
  color: #000000;
}

.settings-form {
  display: flex;
  margin: 2rem auto;
  padding: 2rem;
  background: #ffffff;
  border-radius: 10px;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
  flex-direction: column;
  gap: 20px;
  max-width: 1000px;
  width: 100%;
  margin: 0px auto;
  margin-top: 70px;
}

.form-group {
  display: flex;
  flex-direction: initial;
  gap: 10px;
}

label {
  font-size: 1rem;
  color: #34495e;
}

.input-field {
  padding: 0.4rem;
  font-size: 1rem;
  border: 1px solid #e0e0e0;
  border-radius: 5px;
  outline: none;
  transition: border-color 0.3s ease;
}

.input-field:focus {
  border-color: #8e44ad;
}

.toggle {
  display: flex;
  align-items: center;
  gap: 10px;
}

.button {
  padding: 0.8rem 1.5rem;
  font-size: 1rem;
  font-weight: bold;
  color: #ffffff;
  background: #2ecc71;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.3s ease;
}

.button:hover {
  background: #27ae60;
}

.save-button {
  align-self: center;
}

.active-alert {
  margin-top: 5px;
  padding: 1rem;
  font-size: 1.2rem;
  color: #ffffff;
  background: #ff0000;
  border: 1px solid #ffffff;
  border-radius: 10px;
}
</style>