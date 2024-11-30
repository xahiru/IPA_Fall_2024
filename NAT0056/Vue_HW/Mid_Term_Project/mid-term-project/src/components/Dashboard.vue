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
    window.location.href = '/login';
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
      <div class="logo">Greenhouse</div>
      <ul class="nav-links">
        <li><router-link to="/dashboard">Home</router-link></li>
        <li><router-link to="/over-view">Overview</router-link></li>
        <li><router-link to="/settings">Settings</router-link></li>
        <li><router-link to="/logs">Logs</router-link></li>
        <li> <a @click="logout">Logout</a> </li>
      </ul>
    </nav>

    <main>
      <header>
        <h1>Greenhouse</h1>
        <h3>Real-time Monitoring of Greenhouse Conditions</h3>
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
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Roboto', sans-serif;
  background: linear-gradient(135deg, #070532d3, #1769e4);
  color: #9e1f1f;
  padding-top: 68px;
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
  background: #2d3e50;
  color: white;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  z-index: 100;
  overflow-x: auto;
}
a:hover{
  cursor: pointer;
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

main {
  padding: 2rem 3rem;
}

header h3 {
  font-size: 1.1rem;
  color: #051752;
  font-weight: 300;
  padding-top: 10px;
}

.metrics {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 30px;
  margin-top: 30px;
}

.card {
  padding: 1.8rem;
  border-radius: 10px;
  box-shadow: 0 4px 15px rgba(51, 20, 20, 0.1);
  text-align: center;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
}

.card h2 {
  font-size: 1.6rem;
  margin-bottom: 10px;
}

.card p {
  font-size: 1.9rem;
  font-weight: 600;
}

.temperature-card {
  border-left: 5px solid #247c22;
}

.humidity-card {
  border-left: 5px solid #16a085;
}

.moisture-card {
  border-left: 5px solid #f39c12;
}

.light-card {
  border-left: 5px solid #3498db;
}

@media (max-width: 1024px) {
  .metrics {
    grid-template-columns: repeat(2, 1fr);
  }

  .navbar {
    padding: 1.2rem 1.5rem;
  }

  .nav-links li a {
    font-size: 1rem;
  }
}

@media (max-width: 768px) {
  .metrics {
    grid-template-columns: 1fr;
  }
  .navbar li{
    margin-left: 20px;
  }
  header h1 {
    font-size: 2rem;
  }
  header h1 {
    margin-top: 30px;
  }
  header p {
    font-size: 1rem;
  }

  .card {
    padding: 1.5rem;
  }

  .card h2 {
    font-size: 1.3rem;
  }

  .card p {
    font-size: 1.8rem;
  }
}

@media (max-width: 480px) {
  .navbar {
    flex-direction: column;
    align-items: flex-start;
    padding: 1.2rem;
  }

  .navbar li{
    margin-left: 20px;
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

  .metrics {
    margin-top: 20px;
  }

  .card {
    padding: 1rem;
  }

  .card-icon {
    font-size: 2rem;
  }

  .card h2 {
    font-size: 1.2rem;
  }

  .card p {
    font-size: 1.5rem;
  }
}
</style>
