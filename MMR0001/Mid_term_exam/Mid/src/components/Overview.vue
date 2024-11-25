
<script setup>
  import { ref } from 'vue';
  import Navbar from './Navbar.vue';
  
  const temperature = ref(24); 
  const humidity = ref(65); 
  const moisture = ref(45); 
  const lightLevel = ref(300); 
  </script>
  
  <template>
    <div id="overview">
      <nav class="navbar">
        <div class="logo">Greenhouse</div>
        <ul class="nav-links">
            <li><router-link to="/dashboard">Home</router-link></li>
            <li><router-link to="/dashboard">Dashboard</router-link></li>
            <li><router-link to="/settings">Settings</router-link></li>
            <li> <a @click="logout">Logout</a> </li>
        </ul>
      </nav>
  
      <main>
        <header>
          <h1>Overview</h1>
          <p>Explore the Controlled environment, challenges, and real-time data of greenhouse monitoring.</p>
        </header>
  
        <section class="articles">
          <article>
            <h2>Controlled Environment</h2>
            <p>
             Greenhouses provide a controlled environment for crops, allowing farmers to manage temperature, humidity, light, and water precisely. This control extends the growing season and allows for year-round production, even in unfavorable climates.
            </p>
          </article>
          <article>
            <h2>Reduced Environmental Impact</h2>
            <p>
             By optimizing resources like water, fertilizer, and energy, greenhouses can minimize the environmental footprint of agriculture. They also allow for climate-sensitive crops to be grown locally, reducing the need for long-distance transportation.
            </p>
          </article>
          <article>
            <h2>The Importance of Monitoring in Greenhouses</h2>
            <p>
              Monitoring the internal conditions of a greenhouse is critical for ensuring optimal growing conditions. Temperature, humidity, light levels, and soil moisture all directly impact plant growth. By using IoT sensors and smart systems, farmers can monitor and adjust these parameters in real time, improving both crop yield and resource efficiency.
            </p>
          </article>
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
  margin-bottom: 20px;
  line-height: 1.5;
}

.articles {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
}

article {
  background-color: white;
  border-radius: 10px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
  text-align: left;
  position: relative;
}

article h2 {
  font-size: 1.5rem;
  margin-bottom: 10px;
  color: #2b580c; 
}

article p {
  font-size: 1rem;
  color: #555;
  line-height: 1.6;
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

  article h2 {
    font-size: 1.2rem;
  }

  article p {
    font-size: 0.9rem;
  }
}
</style>
