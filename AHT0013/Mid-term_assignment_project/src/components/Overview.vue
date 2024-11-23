<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const overviewData = ref([]);

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

const fetchOverviewData = async () => {
    try {
        const response = await fetch('../../DB/Data.json');
        overviewData.value = await response.json();
    } catch (error) {
        console.error('Error fetching overview data:', error);
    }
};

onMounted(fetchOverviewData);
</script>

<template>
  <div id="overview">
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
        <h1>Overview</h1>
        <p>Summary of Greenhouse Performance</p>
      </header>

      <section class="parameters-description">
        <p>
          Our dashboard provides an intuitive, real-time summary of greenhouse conditions. By monitoring key metrics like temperature, humidity, soil moisture, and light levels, we empower farmers and greenhouse managers to effectively manage the environment for optimal crop growth. Below is an overview of each parameter and its significance:
        </p>
        <ul>
          <li><strong>Temperature:</strong> Essential for optimal plant growth, temperature is displayed in real time, allowing users to maintain ideal levels and adjust as needed.</li>
          <li><strong>Humidity:</strong> Appropriate humidity levels support plant health and productivity. Our system continuously tracks changes, alerting users to any fluctuations that may impact crop quality.</li>
          <li><strong>Soil Moisture:</strong> A key factor for plant hydration and nutrient absorption, soil moisture monitoring helps users ensure adequate watering without overwatering.</li>
          <li><strong>Light Level:</strong> As plants rely on light for photosynthesis, our dashboard tracks light exposure, helping users adjust artificial lighting for maximum yield and efficiency.</li>
        </ul>
      </section>

      <section class="overview-metrics">
        <div 
          v-for="(data, index) in overviewData" 
          :key="index" 
          class="card"
        >
          <div class="card-icon" :style="{ backgroundColor: data.color + '20' }">
            <span :style="{ color: data.color }">📊</span>
          </div>
          <div class="card-content">
            <h2>{{ data.title }}</h2>
            <p class="overview-value">{{ data.value }}</p>
            <p class="overview-label">{{ data.description }}</p>
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

.parameters-description {
  font-size: 1rem;
  color: #2d2c2c;
  line-height: 1.6;
  background-color: #fff;
  padding: 1.5rem;
  border-radius: 8px;
  margin-top: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
}

.parameters-description ul {
  margin-top: 0px;
  padding-left: 1.2rem;
}

.parameters-description li {
  margin-bottom: 0rem;
}

.overview-metrics {
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

.overview-value {
  font-size: 2rem;
  font-weight: 600;
  color: #2c3e50;
}

.overview-label {
  font-size: 0.85rem;
  color: #95a5a6;
  margin-top: 6px;
}

@media (max-width: 768px) {
  .overview-metrics {
    grid-template-columns: 1fr;
  }

  main {
    padding: 1.5rem;
  }

  .navbar {
    padding: 1.2rem 1.5rem;
  }

  header h1 {
    font-size: 1.8rem;
  }

  header p,
  .parameters-description p,
  .parameters-description ul li {
    font-size: 0.9rem;
  }

  .overview-value {
    font-size: 1.7rem;
  }

  .card-content h2 {
    font-size: 1.1rem;
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
    font-size: 1.6rem;
  }

  header p,
  .parameters-description p,
  .parameters-description ul li {
    font-size: 0.85rem;
  }

  .overview-metrics {
    margin-top: 20px;
  }

  .card {
    padding: 1rem;
  }

  .card-content h2 {
    font-size: 1rem;
  }

  .overview-value {
    font-size: 1.4rem;
  }
}
</style>