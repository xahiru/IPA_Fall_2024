<template>
  <div>
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

    <div class="settings">
      <h2>Alert Thresholds</h2>
      <form class="settings-form" @submit.prevent="saveSettings">
        <div class="form-group">
          <label>Temperature Alert Range (°C)</label>
          <div class="range-inputs">
            <input 
              type="number" 
              v-model.number="settings.temp.min" 
              placeholder="Min"
              required
            >
            <span>to</span>
            <input 
              type="number" 
              v-model.number="settings.temp.max" 
              placeholder="Max"
              required
            >
          </div>
          <div class="current-value">
            Current Range: {{ settings.temp.min }}°C - {{ settings.temp.max }}°C
          </div>
        </div>
  
        <div class="form-group">
          <label>Humidity Alert Range (%)</label>
          <div class="range-inputs">
            <input 
              type="number" 
              v-model.number="settings.humidity.min" 
              placeholder="Min"
              required
            >
            <span>to</span>
            <input 
              type="number" 
              v-model.number="settings.humidity.max" 
              placeholder="Max"
              required
            >
          </div>
          <div class="current-value">
            Current Range: {{ settings.humidity.min }}% - {{ settings.humidity.max }}%
          </div>
        </div>
  
        <button type="submit">Save Settings</button>
      </form>
    </div>
  </div>
</template>
  
<script>
export default {
  name: 'SettingsView',
  data() {
    return {
      settings: {
        temp: {
          min: 18,
          max: 28
        },
        humidity: {
          min: 40,
          max: 80
        }
      }
    }
  },
  mounted() {
    const saved = localStorage.getItem('alertSettings')
    if (saved) {
      this.settings = JSON.parse(saved)
    }
  },
  methods: {
    saveSettings() {
      if (this.settings.temp.min >= this.settings.temp.max ||
          this.settings.humidity.min >= this.settings.humidity.max) {
        alert('Maximum value must be greater than minimum value')
        return
      }

      localStorage.setItem('alertSettings', JSON.stringify(this.settings))
      alert('Settings saved successfully!')
    },
    logout() {
      alert('You have been logged out')
    }
  }
}
</script>

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

.settings {
  max-width: 400px;
  margin: 20px auto;
  padding: 20px;
}
h2 {
  color: #ffffff;
  text-align: center;
  margin-bottom: 20px;
}
.settings-form {
  background-color: #f8f9fada;
  padding: 20px;
  border-radius: 8px;
}
.form-group {
  margin-bottom: 20px;
}
label {
  display: block;
  margin-bottom: 10px;
  color: #2c3e50;
  font-weight: bold;
}
.range-inputs {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 5px;
}
input {
  width: 100px;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}
.current-value {
  font-size: 0.9em;
  color: #666;
  margin-top: 5px;
}
button {
  width: 100%;
  padding: 10px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-top: 20px;
}
button:hover {
  background-color: #45a049;
}
</style>