<script setup>
import { reactive, onMounted, watch, onUnmounted } from 'vue';
import Navbar from './Navbar.vue';
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
  font-family: 'Arial', sans-serif;
  background-color: #f7fafc; 
  color: #333; 
}

#settings {
  padding: 20px;
  max-width: 800px;
  margin: 0 auto;
}

.navbar {
  background-color: #2b580c; 
  padding: 10px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: white;
}

.navbar .logo {
  font-size: 1.5rem;
  font-weight: bold;
}

.navbar ul {
  list-style: none;
  display: flex;
  gap: 15px;
  margin: 0;
  padding: 0;
}

.navbar ul li a {
  text-decoration: none;
  color: white;
  transition: color 0.3s;
}

.navbar ul li a:hover {
  color: #a3d9a5; 
}

h1.title {
  font-size: 2rem;
  margin-bottom: 10px;
  text-align: center;
  color: #2b580c; 
}

p.subtitle {
  font-size: 1.2rem;
  text-align: center;
  color: #555;
  margin-bottom: 20px;
}

.settings-form {
  background-color: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  font-weight: bold;
  margin-bottom: 5px;
  color: #333;
}

.input-field {
  width: 100%;
  padding: 10px;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.input-field:focus {
  outline: none;
  border-color: #2b580c; 
}

.toggle {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-top: 10px;
}

.toggle input[type='checkbox'] {
  width: 20px;
  height: 20px;
}

.save-button {
  width: 100%;
  padding: 10px 15px;
  background-color: #2b580c;
  color: white;
  font-size: 1.2rem;
  font-weight: bold;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.save-button:hover {
  background-color: #367c15; 
}

.active-alert {
  margin-top: 20px;
  padding: 10px 15px;
  background-color: #ffe5e5; 
  color: #b22222; 
  border-left: 5px solid #b22222; 
  border-radius: 5px;
  font-size: 1rem;
}

@media (max-width: 600px) {
  .settings-form {
    padding: 15px;
  }

  h1.title {
    font-size: 1.5rem;
  }

  p.subtitle {
    font-size: 1rem;
  }

  .input-field, .save-button {
    font-size: 1rem;
  }

  .active-alert {
    font-size: 0.9rem;
  }
}
</style>
