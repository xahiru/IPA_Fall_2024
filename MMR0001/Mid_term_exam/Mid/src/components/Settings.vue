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

        
        if (type === 'temperature') {
            console.log(`Temperature: ${value}, Threshold: ${settings.temperatureThreshold}`);
        }

        
        if (settings.alertsEnabled[type] && value > settings[`${type}Threshold`]) {
            settings.activeAlert = `⚠️ ${type.toUpperCase()} exceeded! Value: ${value.toFixed(
                1
            )}, Threshold: ${settings[`${type}Threshold`]}`;
        }
    });

    
    if (!simulatedMetrics.some(
        (metric) => settings.alertsEnabled[metric.type] && metric.value > settings[`${metric.type}Threshold`]
    )) {
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
            <li><router-link to="/dashboard">Dashboard</router-link></li>
            <li><router-link to="/over-view">Overview</router-link></li>
        </ul>
      </nav>
    <Navbar />
    <h1 class="title">Settings</h1>
    <p class="subtitle">Set thresholds and control alerts dynamically.</p>

    <form class="settings-form" @submit.prevent="saveSettings">

      
      <div class="form-group">
        <label for="temperature">Temperature Threshold (°C):</label>
        <input type="number" id="temperature" v-model="settings.temperatureThreshold" min="0" class="input-field" />
        <div class="toggle">
          <input type="checkbox" id="temperature-alert" v-model="settings.alertsEnabled.temperature" />
          <label for="temperature-alert">Enable Temperature Alerts</label>
        </div>
      </div>

      
      <div class="form-group">
        <label for="humidity">Humidity Threshold (%):</label>
        <input type="number" id="humidity" v-model="settings.humidityThreshold" min="0" class="input-field" />
        <div class="toggle">
          <input type="checkbox" id="humidity-alert" v-model="settings.alertsEnabled.humidity" />
          <label for="humidity-alert">Enable Humidity Alerts</label>
        </div>
      </div>

      
      <div class="form-group">
        <label for="light">Light Threshold (lux):</label>
        <input type="number" id="light" v-model="settings.lightThreshold" min="0" class="input-field" />
        <div class="toggle">
          <input type="checkbox" id="light-alert" v-model="settings.alertsEnabled.light" />
          <label for="light-alert">Enable Light Alerts</label>
        </div>
      </div>

      
      <div class="form-group">
        <label for="moisture">Moisture Threshold (%):</label>
        <input type="number" id="moisture" v-model="settings.moistureThreshold" min="0" class="input-field" />
        <div class="toggle">
          <input type="checkbox" id="moisture-alert" v-model="settings.alertsEnabled.moisture" />
          <label for="moisture-alert">Enable Moisture Alerts</label>
        </div>
      </div>

      
      <div class="form-group">
        <label for="frequency">Simulation Frequency (ms):</label>
        <input type="number" id="frequency" v-model="settings.simulationFrequency" min="1000" class="input-field" />
      </div>

      <button type="submit" class="button save-button">Save Settings</button>
    </form>

    
    <div v-if="settings.activeAlert" class="active-alert">
      {{ settings.activeAlert }}
    </div>
  </div>
</template>

<style scoped>

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background-color: #f9f9f9;
    color: #333;
}

h1.title {
    text-align: center;
    font-size: 2rem;
    margin-top: 20px;
    color: #2e7d32; 
}

p.subtitle {
    text-align: center;
    font-size: 1rem;
    margin-bottom: 20px;
    color: #555;
}

.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #2e7d32;
    padding: 10px 20px;
    color: white;
}

.navbar .logo {
    font-size: 1.5rem;
    font-weight: bold;
}

.navbar .nav-links {
    display: flex;
    list-style: none;
    gap: 20px;
}

.navbar .nav-links li a {
    color: white;
    text-decoration: none;
    font-weight: bold;
    padding: 5px 10px;
    border-radius: 5px;
    transition: background-color 0.3s ease;
}

.navbar .nav-links li a:hover {
    background-color: #1b5e20;
}

.settings-form {
    max-width: 600px;
    margin: 0 auto;
    background: white;
    border: 1px solid #ddd;
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.form-group {
    margin-bottom: 20px;
}

.form-group label {
    display: block;
    font-weight: bold;
    margin-bottom: 5px;
    color: #2e7d32;
}

.input-field {
    width: 100%;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
}

.toggle {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-top: 10px;
}

.toggle label {
    font-size: 0.9rem;
    color: #555;
}

.button.save-button {
    background-color: #2e7d32;
    color: white;
    border: none;
    padding: 10px 15px;
    font-size: 1rem;
    border-radius: 5px;
    cursor: pointer;
    width: 100%;
}

.button.save-button:hover {
    background-color: #1b5e20;
}

.active-alert {
    max-width: 600px;
    margin: 20px auto;
    padding: 15px;
    background-color: #ffcccb;
    color: #b71c1c;
    border: 1px solid #b71c1c;
    border-radius: 5px;
    font-weight: bold;
    text-align: center;
}

@media (max-width: 768px) {
    .navbar .nav-links {
        flex-direction: column;
        gap: 10px;
    }

    .settings-form {
        padding: 15px;
    }
}

</style>
