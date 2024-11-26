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
    font-family: Arial, sans-serif;
    background-color: #f9f9f9;
    color: #333;
}

h1 {
    text-align: center;
    font-size: 2rem;
    margin-top: 20px;
    color: #2e7d32; 
}

p {
    color: #555;
    line-height: 1.6;
    margin-bottom: 20px;
}

.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #2e7d32;
    padding: 10px 20px;
    color: white;
}

.navbar .logo {
    font-size: 1.5rem;
    font-weight: bold;
}

.navbar .nav-links {
    display: flex;
    list-style: none;
    gap: 20px;
}

.navbar .nav-links li a {
    color: white;
    text-decoration: none;
    font-weight: bold;
    padding: 5px 10px;
    border-radius: 5px;
    transition: background-color 0.3s ease;
}

.navbar .nav-links li a:hover {
    background-color: #1b5e20;
}

header {
    max-width: 800px;
    margin: 0 auto;
    text-align: center;
    padding: 20px 10px;
}

header p {
    font-size: 1rem;
    color: #555;
}

.metrics {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
    max-width: 1200px;
    margin: 20px auto;
    padding: 0 15px;
}

.card {
    background-color: white;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    padding: 20px;
    transition: transform 0.2s ease;
    position: relative;
}

.card:hover {
    transform: scale(1.02);
}

.card h2 {
    color: #2e7d32;
    font-size: 1.5rem;
    margin-bottom: 10px;
}

.card p {
    font-size: 1.2rem;
    font-weight: bold;
    color: #333;
}

button,
a {
    background-color: #2e7d32;
    color: white;
    border: none;
    padding: 10px 15px;
    font-size: 1rem;
    border-radius: 5px;
    cursor: pointer;
    text-decoration: none;
}

button:hover,
a:hover {
    background-color: #1b5e20;
}

@media (max-width: 768px) {
    .navbar .nav-links {
        flex-direction: column;
        gap: 10px;
    }

    .metrics {
        grid-template-columns: 1fr;
    }
}

</style>
