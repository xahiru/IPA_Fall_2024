<template>
  <div class="greenhouse-dashboard dashboard-container">
    <!-- Sidebar Navigation -->
    <div class="sidebar">
      <div class="sidebar-header">
        <h3 class="sidebar-title">Greenhouse Monitoring</h3>
      </div>
      <ul class="sidebar-menu">
        <li class="menu-item">
          <span>Login Time: {{ loginTime }}</span>
        </li>
        <li class="menu-item">
          <span>Username: {{ username }}</span>
        </li>
        <li class="menu-item" @click="toggleSettingsPage">
          <span>Settings</span>
        </li>
        <li class="menu-item">
          <span>Location</span>
          <select v-model="selectedLocation" @change="fetchMetrics">
            <option v-for="location in locations" :key="location" :value="location">{{ location }}</option>
          </select>
        </li>
      </ul>
      <button v-if="!showSettingsPage" class="logout-btn" @click="logout">Logout</button>
    </div>

    <!-- Greenhouse Monitoring Content -->
    <div class="content">
      <div v-if="!showSettingsPage" class="greenhouse-content">
        <h2>Greenhouse Metrics</h2>
        <h3>{{ selectedLocation }}</h3>
        
        <!-- Metrics Card -->
        <div class="metrics-card">
          <div class="metric" v-for="(value, label) in greenhouseMetrics" :key="label">
            <p class="metric-label">{{ label }}</p>
            <p class="metric-value">{{ value }}</p>
          </div>
        </div>

        <!-- Chart Display -->
        <div class="chart-container">
          <canvas id="metricsChart" width="200" height="70"></canvas>
        </div>
      </div>

      <!-- Settings Page =-->
      <div v-if="showSettingsPage" class="settings-page">
        <h2>Settings</h2>
        <div class="settings-option">
          <label for="unit">Temperature Unit:</label>
          <select id="unit" v-model="unit" @change="updateUnit">
            <option value="metric">Celsius</option>
            <option value="imperial">Fahrenheit</option>
          </select>
        </div>
        <div class="settings-option">
          <label for="theme">Theme:</label>
          <select id="theme" v-model="theme" @change="updateTheme">
            <option value="light">Light</option>
            <option value="dark">Dark</option>
          </select>
        </div>
        <div class="settings-option">
          <label for="refresh">Auto-Refresh Interval (minutes):</label>
          <input
            id="refresh"
            type="number"
            v-model.number="refreshInterval"
            @change="updateRefreshInterval"
            min="1"
          />
        </div>
        <button class="close-settings" @click="toggleSettingsPage">Close Settings</button>
      </div>
    </div>
  </div>
</template>

<script>
import Chart from "chart.js/auto"; // Import only Chart.js

export default {
  data() {
    return {
      locations: ["Greenhouse 1", "Greenhouse 2", "Greenhouse 3"],
      selectedLocation: "Greenhouse 1",
      greenhouseMetrics: {
        Temperature: "Loading...",
        Humidity: "Loading...",
        "Light Intensity": "Loading...",
      },
      unit: "metric",
      theme: "light",
      refreshInterval: 10,
      showSettingsPage: false,
      loginTime: new Date().toLocaleString(), // Show login time dynamically
      username: "John Doe", // Dynamic username, could be replaced by user authentication data
      refreshIntervalId: null,
      metricsChart: null, // Store the chart instance
    };
  },
  methods: {
    // Simulate fetching greenhouse metrics from an API
    async fetchMetrics() {
      const locationMetrics = {
        "Greenhouse 1": { temperature: 25, humidity: 70, lightIntensity: 800 },
        "Greenhouse 2": { temperature: 30, humidity: 60, lightIntensity: 1200 },
        "Greenhouse 3": { temperature: 22, humidity: 75, lightIntensity: 600 },
      };

      const metrics = locationMetrics[this.selectedLocation];

      this.greenhouseMetrics = {
        Temperature: `${metrics.temperature}°${this.unit === "metric" ? "C" : "F"}`,
        Humidity: `${metrics.humidity}%`,
        "Light Intensity": `${metrics.lightIntensity} lux`,
      };

      // Update the chart with the new metrics data
      this.updateChart(metrics);
    },

    // Update chart with new data
    updateChart(metrics) {
      if (this.metricsChart) {
        this.metricsChart.destroy();
      }

      const ctx = document.getElementById("metricsChart").getContext("2d");
      this.metricsChart = new Chart(ctx, {
        type: "bar",
        data: {
          labels: ["Temperature", "Humidity", "Light Intensity"],
          datasets: [
            {
              label: this.selectedLocation,
              data: [
                metrics.temperature,
                metrics.humidity,
                metrics.lightIntensity,
              ],
              backgroundColor: ["#FF5733", "#33FF57", "#3357FF"],
              borderColor: ["#C70039", "#28B463", "#1F77B4"],
              borderWidth: 1,
            },
          ],
        },
        options: {
          responsive: true,
          plugins: {
            legend: {
              position: "top",
            },
          },
        },
      });
    },

    toggleSettingsPage() {
      this.showSettingsPage = !this.showSettingsPage;
    },

    updateUnit() {
      this.fetchMetrics(); // Refresh metrics based on the new unit
    },

    updateTheme() {
      document.body.setAttribute("data-theme", this.theme);
    },

    updateRefreshInterval() {
      clearInterval(this.refreshIntervalId);
      this.refreshIntervalId = setInterval(this.fetchMetrics, this.refreshInterval * 60 * 1000);
    },

    logout() {
      alert("Logging out...");
      this.$router.push({ name: "Home" }); // Redirect to Home page or login
    },
  },
  mounted() {
    this.fetchMetrics();
    this.refreshIntervalId = setInterval(this.fetchMetrics, this.refreshInterval * 60 * 1000);
  },

  beforeUnmount() {
    clearInterval(this.refreshIntervalId);
  },
};
</script>


<style scoped>
/* Dashboard Styling */
.dashboard-container {
  display: flex;
  min-height: 100vh;
  font-family: "Roboto", sans-serif;
}

/* Sidebar Styling */
.sidebar {
  width: 250px;
  background-color: #2c3e50;
  color: white;
  padding: 20px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  box-shadow: 4px 0 10px rgba(0, 0, 0, 0.2);
}

.sidebar-header {
  text-align: center;
  font-size: 1.5rem;
  margin-bottom: 20px;
}

.sidebar-title {
  font-weight: bold;
}

.sidebar-menu {
  list-style-type: none;
  padding-left: 0;
}

.menu-item {
  padding: 10px 0;
  cursor: pointer;
  border-bottom: 1px solid #34495e;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.menu-item:hover {
  background-color: #34495e;
}

/* Hover effect for Logout button */
.logout-btn {
  background-color: #e74c3c;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 30px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.logout-btn:hover {
  background-color: #c0392b;
}

/* Content Area */
.content {
  flex: 1;
  padding: 20px;
  background-color: #ecf0f1;
}

/* Greenhouse Dashboard Styling */
.greenhouse-content {
  text-align: center;
}

h2 {
  font-size: 2rem;
  color: #2980b9;
}

.metrics-card {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  max-width: 800px;
  margin: auto;
}

.metric {
  background-color: #ffffff;
  padding: 15px;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.metric-label {
  font-weight: 600;
}

.metric-value {
  font-size: 1.5rem;
  font-weight: 700;
  color: #4caf50;
}

/* Chart Styling */
.chart-container {
  margin-top: 30px;
  max-width: 900px;
  margin: auto;
}

/* Settings Page */
.settings-page {
  background-color: #fff;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.settings-option {
  margin-bottom: 20px;
}

.settings-option label {
  font-weight: 600;
}

.close-settings {
  background-color: #2980b9;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.close-settings:hover {
  background-color: #1f6f9b;
}
</style>
