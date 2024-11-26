
<script setup>
  import { ref } from 'vue';
  
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

.articles {
    max-width: 900px;
    margin: 20px auto;
    padding: 0 15px;
}

.articles article {
    background-color: white;
    border: 1px solid #ddd;
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.articles article h2 {
    color: #2e7d32;
    margin-bottom: 10px;
    font-size: 1.5rem;
}

.articles article p {
    margin-bottom: 0;
    font-size: 1rem;
    color: #555;
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

    .articles article {
        padding: 15px;
    }
}

</style>
