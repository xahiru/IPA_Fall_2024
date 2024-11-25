<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import Navbar from './Navbar.vue';

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
        const response = await fetch('../../Data/data.json');
        metrics.value = await response.json();
    } catch (error) {
        console.error('Error fetching data:', error);
    }
};

const generateRandomValue = (min, max, unit = '') => {
    return `${(Math.random() * (max - min) + min).toFixed(1)}${unit}`;
};
const updateMetrics = () => {
    metrics.value = [
        {
            ...metrics.value[0],
            value: generateRandomValue(15, 16, '°C')
        },
        {
            ...metrics.value[1],
            value: generateRandomValue(67, 68, '%')
        },
        {
            ...metrics.value[2],
            value: generateRandomValue(45, 45.5, '%')
        },
        {
            ...metrics.value[3],
            value: generateRandomValue(300, 312, ' lux')
        }
    ];
};

onMounted(async () => {
    await fetchData();
    const intervalId = setInterval(updateMetrics, 3000);
    onUnmounted(() => {
        clearInterval(intervalId);
    });
});
</script>


<template>
  <div id="dashboard">
    <nav class="navbar">
      <div class="logo">Greenhouse</div>
      <ul class="nav-links">
        <li><router-link to="/dashboard">Home</router-link></li>
        <li><router-link to="/over-view">Overview</router-link></li>
        <li><router-link to="/settings">Settings</router-link></li>
        <li><router-link to="/data-chart">Logs</router-link></li>
        <li> <a @click="logout">Logout</a> </li>
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
          :style="{ borderLeft: `5px solid ${metric.color}` }"
        >
          <h2>{{ metric.title }}</h2>
          <p>{{ metric.value }}</p>
        </div>
      </section>
    </main>
  </div>
</template>

<style scoped>
body {
  margin: 0;
  font-family: 'Arial', sans-serif;
  background-color: #f4f7f6; 
  color: #333; 
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #2b580c; 
  color: white;
  padding: 10px 20px;
}

.navbar .logo {
  font-size: 1.5rem;
  font-weight: bold;
}

.nav-links {
  list-style: none;
  display: flex;
  gap: 15px;
  margin: 0;
  padding: 0;
}

.nav-links li {
  font-size: 1rem;
}

.nav-links a {
  color: white;
  text-decoration: none;
  transition: color 0.3s;
}

.nav-links a:hover {
  color: #a3d9a5; 
}

main {
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
}

header h1 {
  font-size: 2rem;
  margin-bottom: 10px;
}

header p {
  font-size: 1.2rem;
  color: #666;
}

.metrics {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin-top: 20px;
}

.card {
  background-color: white;
  border-radius: 10px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
  text-align: center;
  position: relative;
}

.card h2 {
  font-size: 1.5rem;
  margin-bottom: 10px;
  color: #2b580c;
}

.card p {
  font-size: 1.2rem;
  color: #555;
}

.card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 5px;
  height: 100%;
  background-color: var(--color, #2b580c); /* Default color */
  border-radius: 10px 0 0 10px;
}

@media (max-width: 600px) {
  .navbar .logo {
    font-size: 1.2rem;
  }

  .nav-links li {
    font-size: 0.9rem;
  }

  header h1 {
    font-size: 1.5rem;
  }

  header p {
    font-size: 1rem;
  }

  .card h2 {
    font-size: 1.2rem;
  }

  .card p {
    font-size: 1rem;
  }
}
</style>
