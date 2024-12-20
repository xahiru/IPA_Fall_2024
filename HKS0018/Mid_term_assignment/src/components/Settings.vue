<template>
    <div class="settings-layour">
        <Navbar />
  
      <main class="settings">
        <header>
          <h1>Settings</h1>
          <p>Configure Thresholds for Monitoring</p>
        </header>
  
        <div class="settings-form">
          <div v-for="(setting, index) in settings" :key="index" class="setting-item">
            <h3>{{ setting.name }} ({{ setting.unit }})</h3>
            <div class="input-group">
              <label>
                Min: 
                <input 
                  type="number" 
                  v-model.number="setting.min" 
                  :min="setting.range[0]" 
                  :max="setting.range[1]" 
                />
              </label>
              <label>
                Max: 
                <input 
                  type="number" 
                  v-model.number="setting.max" 
                  :min="setting.range[0]" 
                  :max="setting.range[1]" 
                />
              </label>
            </div>
          </div>
  
          <button @click="saveSettings" class="save-button">Save Settings</button>
        </div>
      </main>
    </div>
  </template>
  
  <script>
  import Navbar from '../components/Navbar.vue';
  export default {
    components: { Navbar },
    data() {
      return {
        settings: [
          { name: 'Temperature', unit: '°C', min: 18, max: 28, range: [0, 50] },
          { name: 'Humidity', unit: '%', min: 40, max: 80, range: [0, 100] },
          { name: 'Soil Moisture', unit: '%', min: 60, max: 90, range: [0, 100] },
          { name: 'Light Level', unit: 'lux', min: 600, max: 1000, range: [0, 2000] }
        ]
      };
    },
    methods: {
      saveSettings() {
        localStorage.setItem('greenhouseSettings', JSON.stringify(this.settings));
        alert('Settings saved successfully!');
      },
      loadSettings() {
        const savedSettings = JSON.parse(localStorage.getItem('greenhouseSettings'));
        if (savedSettings) {
          this.settings = savedSettings;
        }
      },

    },
    mounted() {
      this.loadSettings();
    }
  };
  </script>
  
  <style scoped>
.dashboard-layout {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
  color: #00e676;
}

.link {
  text-decoration: none;
  color: #e0e0e0;
  font-size: 1rem;
  transition: color 0.3s ease;
}

.link:hover {
  color: #00e676;
}

.settings {
  margin-top: 80px;
  padding: 1.5rem 2rem;
  background: #1e1e2f;
  color: #e0e0e0;
  flex: 1;
}

h1 {
  font-size: 1.8rem;
  margin-bottom: 1rem;
  text-align: center;
}

p {
  margin-bottom: 1.5rem;
  text-align: center;
}

.settings-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  max-width: 600px;
  margin: 0 auto;
}

.setting-item {
  background: #2e2e48;
  padding: 1rem;
  border-radius: 8px;
}

.input-group {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
}

label {
  flex: 1;
  display: flex;
  flex-direction: column;
  color: #8c9ba5;
}

input {
  padding: 0.5rem;
  background: #1c1c2d;
  border: none;
  border-radius: 5px;
  color: #e0e0e0;
  width: 100%;
  max-width: 150px;
}

.save-button {
  padding: 0.7rem 2rem;
  background-color: #11ba68;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background 0.3s ease;
  max-width: 200px;
  margin: 0 auto;
}

.save-button:hover {
  background-color: #00c853;
}

@media (max-width: 768px) {
  .input-group {
    flex-direction: column;
    gap: 0.5rem;
  }

  .nav-links {
    flex-direction: column;
    gap: 0.5rem;
  }

  .link {
    font-size: 0.9rem;
  }

  h1 {
    font-size: 1.5rem;
  }
}
</style>

  