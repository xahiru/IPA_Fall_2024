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
    window.location.href = '/login';
};

const fetchOverviewData = async () => {
    try {
        const response = await fetch('../../DB/overview.json'); // Adjust path as needed
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
      <div class="logo">Greenhouse</div>
      <ul class="nav-links">
        <li><router-link to="/dashboard">Home</router-link></li>
        <li><router-link to="/over-view">Overview</router-link></li>
        <li><router-link to="/settings">Settings</router-link></li>
        <li><router-link to="/historical-data-chart">Logs</router-link></li>
        <li> <a @click="logout">Logout</a> </li>
      </ul>
    </nav>

    <main>
      <header>
        <h1>Greenhouse Overview</h1>
        <p>A greenhouse is a structure designed to create a controlled environment for growing plants. It typically features transparent walls and roofs, often made of glass or plastic, to allow sunlight in while trapping heat. This warmth helps maintain a stable temperature, promoting plant growth even in cold or unfavorable weather conditions.

Greenhouses are used for various purposes, such as growing flowers, vegetables, fruits, and ornamental plants, especially in regions where the natural climate isn't ideal for year-round cultivation. They can range from small backyard setups to large commercial operations. Key features often include ventilation systems, heating, cooling, irrigation, and automated climate controls to optimize growing conditions.

By creating a microclimate, greenhouses allow for extended growing seasons, protection from pests, and improved crop yields..</p>
      </header>

      <section class="overview-details">
        <div 
          v-for="(item, index) in overviewData" 
          :key="index" 
          class="card" 
          :style="{ borderLeft: `5px solid ${item.color}` }"
        >
          <h2>{{ item.title }}</h2>
          <p>{{ item.description }}</p>
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
  background: #f4f6f9;
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
  background: #2d3e50;
  color: white;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  z-index: 100;
  overflow-x: auto;
}

a:hover {
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

header h1 {
  font-size: 2.5rem;
  font-weight: 700;
  color: #ffffff;
  margin-top: 100px;
}

header p {
  font-size: 1.1rem;
  color: #ffffff;
  font-weight: 300;
}

.overview-details {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 30px;
  margin-top: 30px;
}

.card {
  padding: 1.8rem;
  border-radius: 10px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  text-align: center;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
}

.card h2 {
  font-size: 1.5rem;
  margin-bottom: 10px;
}

.card p {
  font-size: 1rem;
  font-weight: 400;
}

@media (max-width: 1024px) {
  .overview-details {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .overview-details {
    grid-template-columns: 1fr;
  }

  header h1 {
    font-size: 2rem;
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
    font-size: 1rem;
  }
}

@media (max-width: 480px) {
  .navbar {
    flex-direction: column;
    align-items: flex-start;
    padding: 1.2rem;
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

  .overview-details {
    margin-top: 20px;
  }

  .card {
    padding: 1rem;
  }

  .card h2 {
    font-size: 1.2rem;
  }

  .card p {
    font-size: 0.9rem;
  }
}
</style>