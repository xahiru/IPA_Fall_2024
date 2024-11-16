<script setup>
import { ref, onMounted, watch } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

const temperatureThreshold = ref(25);
const humidityThreshold = ref(50);
const soilMoistureThreshold = ref(40);
const lightLevelThreshold = ref(500);

const loadSettingsFromFile = async () => {
    try {
        const response = await fetch('/data.json');
        const data = await response.json();
        temperatureThreshold.value = data.temperatureThreshold;
        humidityThreshold.value = data.humidityThreshold;
        soilMoistureThreshold.value = data.soilMoistureThreshold;
        lightLevelThreshold.value = data.lightLevelThreshold;
    } catch (error) {
        console.error('Error loading settings from JSON:', error);
    }
};

const saveSettings = () => {
    const settings = {
        temperatureThreshold: temperatureThreshold.value,
        humidityThreshold: humidityThreshold.value,
        soilMoistureThreshold: soilMoistureThreshold.value,
        lightLevelThreshold: lightLevelThreshold.value,
    };
    localStorage.setItem('alertSettings', JSON.stringify(settings));
};

watch(
    [temperatureThreshold, humidityThreshold, soilMoistureThreshold, lightLevelThreshold],
    saveSettings
);

onMounted(() => {
    loadSettingsFromFile();
});

const logout = async () => {
    localStorage.removeItem("user");
    router.push({ name: 'Login' });
};
</script>

<template>
  <div id="settings">
    <nav class="navbar">
      <div class="logo">Greenhouse Settings</div>
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
        <p>Adjust alert thresholds for greenhouse metrics</p>
      </header>

      <section class="settings-form">
        <form @submit.prevent="saveSettings">
          <div class="form-item">
            <label for="temperatureThreshold">Temperature Threshold (°C):</label>
            <input type="number" v-model="temperatureThreshold" id="temperatureThreshold" min="0" max="50" />
          </div>

          <div class="form-item">
            <label for="humidityThreshold">Humidity Threshold (%):</label>
            <input type="number" v-model="humidityThreshold" id="humidityThreshold" min="0" max="100" />
          </div>

          <div class="form-item">
            <label for="soilMoistureThreshold">Soil Moisture Threshold (%):</label>
            <input type="number" v-model="soilMoistureThreshold" id="soilMoistureThreshold" min="0" max="100" />
          </div>

          <div class="form-item">
            <label for="lightLevelThreshold">Light Level Threshold (lux):</label>
            <input type="number" v-model="lightLevelThreshold" id="lightLevelThreshold" min="0" max="2000" />
          </div>

          <button type="button" @click="saveSettings" class="save-btn">Save Settings</button>
        </form>
      </section>
    </main>
  </div>
</template>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Arial', sans-serif;
  background: #f4f7fa;
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
  background: #ffffff;
  color: #333;
  border-bottom: 1px solid #e0e0e0;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
  z-index: 100;
}

a:hover {
  cursor: pointer;
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
  color: #2c3e50;
}

.nav-links {
  list-style: none;
  display: flex;
  gap: 20px;
}

.nav-links li a {
  text-decoration: none;
  color: #2c3e50;
  font-size: 1rem;
  transition: color 0.3s ease;
}

.nav-links li a:hover {
  color: #8e44ad;
}

main {
  padding: 2rem 3rem;
}

header h1 {
  font-size: 2.2rem;
  font-weight: 700;
  color: #2c3e50;
  margin-bottom: 5px;
}

header p {
  font-size: 1rem;
  color: #d7d7d7;
  font-weight: 300;
}

.settings-form {
  margin-top: 30px;
}

.form-item {
  margin-bottom: 1rem;
}

label {
  display: block;
  font-size: 1rem;
  color: #34495e;
  margin-bottom: 5px;
}

input[type="number"] {
  width: 100%;
  padding: 8px;
  font-size: 1rem;
  border: 1px solid #ddd;
  border-radius: 8px;
  outline: none;
  transition: border 0.3s ease;
}

input[type="number"]:focus {
  border-color: #392085;
}

.save-btn {
  padding: 0.8rem 1.5rem;
  font-size: 1rem;
  color: #ffffff;
  background-color: #227b6c;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.save-btn:hover {
  background-color: #382589;
}

@media (max-width: 768px) {
  .settings-form {
    grid-template-columns: 1fr;
  }

  main {
    padding: 1.5rem;
  }

  .navbar {
    padding: 1.2rem 1.5rem;
  }
}

@media (max-width: 500px) {
  .navbar {
    flex-direction: column;
    align-items: flex-start;
  }

  .nav-links {
    gap: 10px;
    overflow-x: auto;
    max-width: 100%;
  }

  header h1 {
    font-size: 1.8rem;
  }

  header p {
    font-size: 0.9rem;
  }

  .settings-form {
    margin-top: 20px;
  }

  .form-item {
    padding: 1rem;
  }

  .form-item label {
    font-size: 0.9rem;
  }

  .save-btn {
    font-size: 0.9rem;
  }
}
</style>