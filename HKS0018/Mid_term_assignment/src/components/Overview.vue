<template>
  <div class="overview-layout">
    <Navbar />

    <main class="overview">
      <header>
        <h1>Overview</h1>
      </header>
      <section class="features">
        <p>
  Our app is designed to provide real-time insights and powerful tools that help you maintain an optimal environment for plant growth.<br>
  By continuously monitoring key factors like temperature, humidity, soil moisture, and light levels, it ensures your greenhouse is always in ideal conditions.<br>
  This helps prevent common environmental stressors, boosts plant health, and maximizes crop yield.<br>
  With easy-to-use features, you can make data-driven decisions to optimize plant care, increase productivity, and ensure your greenhouse operates efficiently.
</p>

      </section>



      <section class="features">
        <h2>Key Features</h2>
<ul>
  <li><strong>Temperature Control:</strong> Automatically monitor and adjust the temperature to stay within the ideal range for different crops, ensuring healthy growth and preventing stress caused by temperature fluctuations.</li>
  <li><strong>Humidity Management:</strong> Keep track of humidity levels to prevent conditions that could cause mold or dehydration, promoting a stable environment for plant growth.</li>
  <li><strong>Soil Moisture Monitoring:</strong> Prevent overwatering or dehydration by tracking soil moisture levels, making it easier to maintain the right balance of water for healthy plants.</li>
  <li><strong>Light Level Optimization:</strong> Ensure plants receive the right amount of sunlight by monitoring light intensity, supporting efficient photosynthesis and promoting robust, healthy growth.</li>
</ul>

      </section>

      <section class="metrics-section">
        <div class="metric-card" v-for="(metric, index) in metrics" :key="index">
          <h3>{{ metric.icon }} {{ metric.name }}</h3>
          <p>{{ metric.description }}</p>
          <div class="metric-value">{{ metric.value }}</div>
          <div class="status" :class="getStatusClass(metric.value, metric.type, metric.min, metric.max)">
            {{ getStatus(metric.value, metric.type, metric.min, metric.max) }}
          </div>
        </div>
      </section>

      <div class="update-info">Last Updated: {{ lastUpdated }}</div>
    </main>
  </div>
</template>

<script>
import Navbar from '../components/Navbar.vue';
export default {
  components: { Navbar },
  data() {
    return {
      metrics: [],
      lastUpdated: ''
    };
  },
  methods: {
    getStatus(value, type, min, max) {
      if (value < min) return 'Low';
      if (value > max) return 'High';
      return 'Normal';
    },
    getStatusClass(value, type, min, max) {
      const status = this.getStatus(value, type, min, max);
      return `status-${status.toLowerCase()}`;
    },
    logout() {
      localStorage.clear();
      this.$router.push('/login');
    },
    async fetchMetrics() {
      try {
        const response = await fetch('../../db/data.json');
        const data = await response.json();
        this.metrics = data;
      } catch (error) {
        console.error('Error loading metrics:', error);
      }
    }
  },
  mounted() {
    this.fetchMetrics();
    this.lastUpdated = new Date().toLocaleTimeString();
  }
};
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  background-color: #121212;
  color: #e0e0e0;
  font-family: 'Arial', sans-serif;
}

.overview-layout {
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
  font-size: 1.1rem;
  transition: color 0.3s ease;
}

.link:hover {
  color: #00e676;
}

.overview {
  margin-top: 80px;
  padding: 2rem;
  flex: 1;
}

header h1 {
  font-size: 2rem;
  margin-bottom: 10px;
}

header p {
  font-size: 1rem;
  color: #b0bec5;
}

.features {
  margin-top: 40px;
  background: #d7d7ec;
  padding: 1.5rem;
  border-radius: 10px;
}

.features h2 {
  font-size: 1.5rem;
  margin-bottom: 1rem;
}

.features ul {
  list-style: none;
  padding-left: 1.2rem;
}

.features li {
  margin-bottom: 10px;
}

.metrics-section {
  margin-top: 40px;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
}

.metric-card {
  background: #2e2e48;
  color: #fff;
  padding: 1rem;
  border-radius: 10px;
  text-align: center;
  transition: transform 0.2s ease;
}

.metric-card:hover {
  transform: scale(1.05);
}

.metric-value {
  font-size: 1.5em;
  font-weight: bold;
  margin-top: 5px;
}

.status {
  margin-top: 10px;
  padding: 5px 10px;
  border-radius: 5px;
  font-size: 0.9rem;
}

.status-low {
  background: #f39c12;
}

.status-high {
  background: #e74c3c;
}

.status-normal {
  background: #27ae60;
}

.update-info {
  margin-top: 20px;
  color: #b0bec5;
  text-align: center;
}
</style>
