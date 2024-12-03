<template>
  <div id="dashboard">
    <!-- Navbar -->
    <nav class="navbar">
      <div class="logo">Greenhouse</div>
     
      <!-- Hamburger Icon for mobile -->
      <div class="hamburger" @click="toggleMenu">
        <span class="bar"></span>
        <span class="bar"></span>
        <span class="bar"></span>
      </div>
     
      <!-- Navbar Links -->
      <ul class="nav-links" :class="{'active': menuActive}">
        <li><router-link to="/">Home</router-link></li>
        <li><router-link to="/dashboard">Dashboard</router-link></li>
        <li><router-link to="/overview">Overview</router-link></li>
        <li><router-link to="/settings">Settings</router-link></li>
        <li><router-link to="/charts">Charts</router-link></li>
        <li><a @click="logout">Logout</a></li>
      </ul>
    </nav>

    <!-- Settings Panel -->
    <div class="content">
      <h1 class="title">Settings Panel</h1>
      <p class="subtitle">Set thresholds and control alerts dynamically.</p>

      <form class="settings-form" @submit.prevent="saveSettings">
        <div class="form-group">
          <label for="temperature">Temperature Threshold (°C):</label>
          <input type="number" id="temperature" v-model="settings.temperatureThreshold" class="input-field" />
          <div class="toggle">
            <input type="checkbox" id="temperature-alert" v-model="settings.alertsEnabled.temperature" />
            <label for="temperature-alert">Enable Temperature Alerts</label>
          </div>
        </div>

        <div class="form-group">
          <label for="humidity">Humidity Threshold (%):</label>
          <input type="number" id="humidity" v-model="settings.humidityThreshold" class="input-field" />
          <div class="toggle">
            <input type="checkbox" id="humidity-alert" v-model="settings.alertsEnabled.humidity" />
            <label for="humidity-alert">Enable Humidity Alerts</label>
          </div>
        </div>

        <div class="form-group">
          <label for="light">Light Threshold (lux):</label>
          <input type="number" id="light" v-model="settings.lightThreshold" class="input-field" />
          <div class="toggle">
            <input type="checkbox" id="light-alert" v-model="settings.alertsEnabled.light" />
            <label for="light-alert">Enable Light Alerts</label>
          </div>
        </div>

        <div class="form-group">
          <label for="moisture">Moisture Threshold (%):</label>
          <input type="number" id="moisture" v-model="settings.moistureThreshold" class="input-field" />
          <div class="toggle">
            <input type="checkbox" id="moisture-alert" v-model="settings.alertsEnabled.moisture" />
            <label for="moisture-alert">Enable Moisture Alerts</label>
          </div>
        </div>

        <button type="submit" class="button save-button">
          Save Settings
        </button>
      </form>

      <!-- Active Alerts -->
      <div v-if="settings.activeAlerts.length > 0" class="active-alerts">
        <ul>
          <li v-for="alert in settings.activeAlerts" :key="alert">{{ alert }}</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
import {ref, reactive, onMounted, watch, onUnmounted } from 'vue';

const menuActive = ref(false);
  
  const toggleMenu = () => {
    menuActive.value = !menuActive.value;
  };
  
  
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
  activeAlerts: [],
  simulationFrequency: 5000,
});

const saveSettings = () => {
  localStorage.setItem('alertSettings', JSON.stringify(settings));
  alert("Settings saved successfully!");
};

// Function to simulate metric data
const simulateData = () => {
  const simulatedMetrics = [
    { type: 'temperature', value: Math.random() * 50 },
    { type: 'humidity', value: Math.random() * 100 },
    { type: 'light', value: Math.random() * 300 },
    { type: 'moisture', value: Math.random() * 100 },
  ];

  // Clear previous alerts
  settings.activeAlerts = [];

  // Check each metric and trigger alerts if necessary
  simulatedMetrics.forEach((metric) => {
    const { type, value } = metric;
    const thresholdKey = `${type}Threshold`;

    if (settings.alertsEnabled[type] && value > settings[thresholdKey]) {
      settings.activeAlerts.push(
        `⚠️ ${type.toUpperCase()} exceeded! Value: ${value.toFixed(1)}, Threshold: ${settings[thresholdKey]}`
      );
    }
  });

  // If no alerts are triggered, show a "safe" message
  if (settings.activeAlerts.length === 0) {
    settings.activeAlerts.push('All metrics are within the normal range.');
  }
};

let simulationInterval = null;

const startSimulation = () => {
  stopSimulation(); // Clear previous interval
  simulationInterval = setInterval(simulateData, settings.simulationFrequency);
};

const stopSimulation = () => {
  if (simulationInterval) {
    clearInterval(simulationInterval);
    simulationInterval = null;
  }
};

onMounted(() => {
  const savedSettings = localStorage.getItem('alertSettings');
  if (savedSettings) {
    Object.assign(settings, JSON.parse(savedSettings));
  }
  startSimulation();
});

onUnmounted(stopSimulation);

watch(
  () => settings.simulationFrequency,
  () => {
    startSimulation(); // Restart simulation when frequency changes
  }
);

const logout = async () => {
  localStorage.removeItem("user");
  window.location.href = "/login";
};
</script>

<style scoped>
/* Reset styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Page and layout styles */



.content {
  padding: 2rem;
  margin: 80px auto 0; /* Adjust for navbar height */
  max-width: 600px;
  background: white;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}  
#dashboard {
    font-family: 'Roboto', sans-serif;
    background: #f4f6f9;
    color: #333;
    padding-top: 70px;
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
    z-index: 100;
    transition: all 0.3s ease; /* Add smooth transition */
  }
  
  a:hover{
    cursor: pointer;
}

  .logo {
    font-size: 1.8rem;
    font-weight: bold;
  }
  
  .nav-links {
    list-style: none;
    display: flex;
    gap: 30px;
  }
  
  .nav-links a {
    color: #ffffff;
    text-decoration: none;
    font-size: 1.1rem;
  }
  
  .hamburger {
    display: none;
    flex-direction: column;
    gap: 5px;
    cursor: pointer;
  }
  
  .hamburger .bar {
    width: 25px;
    height: 4px;
    background-color: white;
    border-radius: 5px;
  }
  
  @media (max-width: 768px) {
    .nav-links {
      display: none;
      width: 100%;
      flex-direction: column;
      gap: 1rem;
      position: absolute;
      top: 70px;
      left: 0;
      background-color: #2d3e50;
      padding: 1rem 0;
      z-index: -1; /* Fix issue where links appear behind navbar */
    }
  
    .nav-links.active {
      display: flex;
      z-index: 9999; /* Ensure the links show above other elements */
    }
  
    .hamburger {
      display: flex;
    }
  
    .nav-links li {
      width: 100%;
    }
  
    .nav-links a {
      padding: 0.5rem 1rem;
      font-size: 1.2rem;
    }
  }
/* Typography and form styles */
.title {
  font-size: 1.8rem;
  font-weight: bold;
  color: #2d3e50;
  margin-bottom: 1rem;
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
  color: #2d3e50;
}

.input-field {
  padding: 0.8rem;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
  outline: none;
}

.input-field:focus {
  border-color: #00aaff;
  box-shadow: 0 0 5px rgba(0, 170, 255, 0.5);
}

.toggle {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-top: 0.5rem;
}

.toggle label {
  font-size: 0.9rem;
  color: #34495e;
}

/* Active Alerts */
.active-alerts {
  margin-top: 1.5rem;
  padding: 1rem;
  font-size: 1.2rem;
  color: #ffffff;
  background-color: #e74c3c;
  border-radius: 5px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  text-align: center;
  white-space: normal; /* Allow text to wrap */
  word-wrap: break-word; /* Break long words */
  overflow-wrap: break-word; /* Break word if necessary */
  word-break: break-word; /* Prevent long strings from breaking out of the box */
}

/* Buttons */
.button {
  padding: 0.8rem;
  font-size: 1rem;
  font-weight: bold;
  color: white;
  background-color: #2d3e50;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.button:hover {
  background-color: #1a2736;
}
</style>