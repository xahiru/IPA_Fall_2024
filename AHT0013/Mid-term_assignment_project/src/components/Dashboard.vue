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
          <div class="card-icon" :style="{ backgroundColor: metric.color + '20' }">
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

.metrics {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  margin-top: 30px;
}

.card {
  display: flex;
  align-items: center;
  padding: 1.5rem;
  border-radius: 16px;
  background: linear-gradient(135deg, #ffffff, #f7f9fc);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.05);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.15);
}

.card-icon {
  width: 60px;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  margin-right: 1.2rem;
}

.card-content h2 {
  font-size: 1.2rem;
  color: #34495e;
  margin-bottom: 6px;
}

.metric-value {
  font-size: 2rem;
  font-weight: 600;
  color: #2c3e50;
}

.metric-label {
  font-size: 0.85rem;
  color: #95a5a6;
  margin-top: 6px;
}

@media (max-width: 100px) {
  .metrics {
    grid-template-columns: 1fr;
  }

  main {
    padding: 1.5rem;
  }

  .navbar {
    padding: 1.2rem 1.5rem;
  }
}

@media (max-width: 100px) {
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

  .metrics {
    margin-top: 20px;
  }

  .card {
    padding: 1rem;
  }

  .card-content h2 {
    font-size: 1rem;
  }

  .metric-value {
    font-size: 1.5rem;
  }
}
</style>