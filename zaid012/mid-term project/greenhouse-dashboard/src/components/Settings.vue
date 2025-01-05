<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

const settings = ref({
  temperatureThreshold: 30,
  humidityThreshold: 60,
  moistureThreshold: 40,
  lightThreshold: 70,
});

const saveSettings = () => {
  localStorage.setItem('settings', JSON.stringify(settings.value));
  alert('Settings saved successfully!');
};

const loadSettings = () => {
  const savedSettings = localStorage.getItem('settings');
  if (savedSettings) {
    settings.value = JSON.parse(savedSettings);
  }
};

onMounted(loadSettings);

const logout = () => {
  localStorage.removeItem('user');
  window.location.href = '/login';
};
</script>

<template>
  <div id="settings">
    <nav class="navbar">
      <div class="logo">Greenhouse</div>
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
        <p>Adjust alert thresholds for greenhouse monitoring.</p>
      </header>

      <form @submit.prevent="saveSettings" class="settings-form">
        <div class="form-group">
          <label for="temperature">Temperature Threshold (°C)</label>
          <input
            id="temperature"
            type="number"
            v-model="settings.temperatureThreshold"
          />
        </div>

        <div class="form-group">
          <label for="humidity">Humidity Threshold (%)</label>
          <input
            id="humidity"
            type="number"
            v-model="settings.humidityThreshold"
          />
        </div>

        <div class="form-group">
          <label for="moisture">Moisture Threshold (%)</label>
          <input
            id="moisture"
            type="number"
            v-model="settings.moistureThreshold"
          />
        </div>

        <div class="form-group">
          <label for="light">Light Threshold (lx)</label>
          <input
            id="light"
            type="number"
            v-model="settings.lightThreshold"
          />
        </div>

        <button type="submit" class="btn-save">Save Settings</button>
      </form>
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
  font-family: 'Roboto', sans-serif;
  background: #f4f6f9;
  color: #090f36;
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
  background: #003268;
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

a:hover {
  cursor: pointer;
}

main {
  padding: 2rem 3rem;
}

header h1 {
  font-size: 2.5rem;
  font-weight: 700;
  color: #48006a;
  margin-bottom: 10px;
}

header p {
  font-size: 1.1rem;
  color: #252525;
  font-weight: 300;
}

.settings-form {
  display: grid;
  grid-template-columns: 1fr;
  gap: 20px;
  margin-top: 30px;
}

.form-group {
  display: flex;
  flex-direction: column;
}

.form-group label {
  font-size: 1rem;
  font-weight: 500;
  margin-bottom: 5px;
}

.form-group input {
  padding: 0.8rem;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.form-group input:focus {
  outline: none;
  border-color: #db34b1;
  box-shadow: 0 0 5px rgba(52, 152, 219, 0.5);
}

.btn-save {
  background: #0033ff;
  color: white;
  padding: 0.8rem 1.5rem;
  font-size: 1rem;
  font-weight: 500;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background 0.3s ease;
}

.btn-save:hover {
  background: #274dae;
}

@media (max-width: 1024px) {
  .settings-form {
    grid-template-columns: 1fr;
  }

  .navbar {
    padding: 1.2rem 1.5rem;
  }

  .nav-links li a {
    font-size: 1rem;
  }
}

@media (max-width: 768px) {
  .navbar {
    flex-wrap: wrap;
  }

  .navbar li {
    margin-left: 20px;
  }

  header h1 {
    margin-top: 30px;
  }

  header p {
    font-size: 1rem;
  }

  .form-group input {
    font-size: 0.9rem;
  }

  .btn-save {
    padding: 0.6rem 1.2rem;
    font-size: 0.9rem;
  }
}

@media (max-width: 480px) {
  .navbar {
    flex-direction: column;
    align-items: flex-start;
    padding: 1.2rem;
  }

  .nav-links {
    display: flex;
    flex-direction: row;
    gap: 10px;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    max-width: 100%;
    white-space: nowrap;
  }

  header h1 {
    margin-top: 30px;
  }

  .nav-links li {
    flex-shrink: 0;
  }

  .logo {
    font-size: 1.6rem;
    margin-bottom: 10px;
  }
}
</style>