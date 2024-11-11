<script setup>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

onMounted(() => {
    const user = localStorage.getItem("user");
    if (!user) {
        router.push({ name: 'Login' });
    }
});
</script>

<template>
  <div id="dashboard">
    <nav class="navbar">
      <div class="logo">Greenhouse</div>
      <ul class="nav-links">
        <li><router-link to="/overview">Overview</router-link></li>
        <li><router-link to="/settings">Settings</router-link></li>
        <li><router-link to="/logs">Logs</router-link></li>
      </ul>
    </nav>

    <main>
      <header>
        <h1>Dashboard</h1>
        <p>Real-time Monitoring of Greenhouse Conditions</p>
      </header>

      <section class="metrics">
        <div class="card temperature-card">
          <div class="card-icon">
            <i class="fas fa-thermometer-half"></i>
          </div>
          <h2>Temperature</h2>
          <p>24°C</p>
        </div>
        <div class="card humidity-card">
          <div class="card-icon">
            <i class="fas fa-tint"></i>
          </div>
          <h2>Humidity</h2>
          <p>65%</p>
        </div>
        <div class="card moisture-card">
          <div class="card-icon">
            <i class="fas fa-water"></i>
          </div>
          <h2>Soil Moisture</h2>
          <p>45%</p>
        </div>
        <div class="card light-card">
          <div class="card-icon">
            <i class="fas fa-sun"></i>
          </div>
          <h2>Light Level</h2>
          <p>300 lux</p>
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
  color: #34495e;
  margin-bottom: 10px;
}

header p {
  font-size: 1.1rem;
  color: #7f8c8d;
  font-weight: 300;
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
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  text-align: center;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
}

.card-icon {
  font-size: 2.5rem;
  color: #3498db;
  margin-bottom: 15px;
}

.card h2 {
  font-size: 1.5rem;
  margin-bottom: 10px;
}

.card p {
  font-size: 2rem;
  font-weight: 600;
}

.temperature-card {
  border-left: 5px solid #e74c3c;
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
