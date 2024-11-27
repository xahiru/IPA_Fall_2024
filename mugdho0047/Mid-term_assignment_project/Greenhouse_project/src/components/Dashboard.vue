<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const metrics = ref([]);

onMounted(() => {
    const user = localStorage.getItem("user");
    if (!user) {
        router.push({ name: 'Login' });
    }
});

const logout = async () => {
    localStorage.removeItem("user");
    router.push({ name: 'Login' });
};

const fetchData = async () => {
    try {
        const response = await fetch('../../DB/data.json');
        metrics.value = await response.json();
    } catch (error) {
        console.error('Error fetching data:', error);
    }
};

onMounted(fetchData);
</script>

<template>
  <div id="dashboard">
    <div class="abstract-background"></div>
    <nav class="navbar">
      <div class="logo">Greenhouse Dashboard</div>
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
        <h1>Dashboard</h1>
        <p>Real-time Monitoring of Greenhouse Conditions</p>
      </header>

      <section class="metrics">
        <div
          v-for="(metric, index) in metrics"
          :key="index"
          class="card"
        >
          <div
            class="card-icon"
            :style="{ backgroundColor: metric.color + '20' }"
          >
            <span :style="{ color: metric.color }">📈</span>
          </div>
          <div class="card-content">
            <h2>{{ metric.title }}</h2>
            <p class="metric-value">{{ metric.value }}</p>
            <p class="metric-label">Current Value</p>
          </div>
        </div>
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
  font-family: 'Roboto', sans-serif;
  margin: 0;
}

#dashboard {
  position: relative;
  width: 100%;
  min-height: 100vh;
  overflow-x: hidden;
}

.abstract-background {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #ff8a00, #e52e71, #8921aa);
  z-index: -1;
}

.abstract-background::before,
.abstract-background::after {
  content: '';
  position: absolute;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 50%;
  pointer-events: none;
}

.abstract-background::before {
  width: 400px;
  height: 400px;
  top: -50px;
  left: -100px;
}

.abstract-background::after {
  width: 300px;
  height: 300px;
  bottom: -50px;
  right: -100px;
}

.navbar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background: rgba(255, 255, 255, 0.9);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  z-index: 100;
}

.nav-links {
  list-style: none;
  display: flex;
  gap: 1.5rem;
}

.nav-links li a {
  text-decoration: none;
  font-size: 1rem;
  color: #333;
  transition: color 0.3s ease;
}

.nav-links li a:hover {
  color: #e52e71;
}

main {
  padding: 2rem 3rem;
  margin-top: 80px;
  color: #fff;
}

header h1 {
  font-size: 2.5rem;
  font-weight: bold;
  color: #ffffff;
}

header p {
  font-size: 1rem;
  font-weight: 300;
  color: rgba(255, 255, 255, 0.7);
}

.metrics {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
  margin-top: 30px;
}

.card {
  background: linear-gradient(135deg, #ffffff, #f9f9fb);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15);
  border-radius: 15px;
  display: flex;
  align-items: center;
  padding: 1.5rem;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
  transform: translateY(-10px);
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.2);
}

.card-icon {
  width: 70px;
  height: 70px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  margin-right: 1.5rem;
}

.card-content h2 {
  font-size: 1.5rem;
  color: #333;
}

.metric-value {
  font-size: 2rem;
  font-weight: 700;
  color: #2c3e50;
}

.metric-label {
  font-size: 0.9rem;
  color: #95a5a6;
}
</style>