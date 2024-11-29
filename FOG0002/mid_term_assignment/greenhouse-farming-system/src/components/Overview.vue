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
      <Navbar />
  
      <main>
        <header>
          <h1>Overview</h1>
          <p>Explore the benefits, challenges, and real-time data of greenhouse monitoring.</p>
        </header>
  
        <section class="articles">
          <article>
            <h2>Benefits of Greenhouse Farming</h2>
            <p>
              Greenhouse farming offers numerous advantages, such as increased control over environmental factors, extended growing seasons, and protection from extreme weather. With the right monitoring tools, farmers can optimize conditions for plant growth, leading to higher yields and better-quality produce.
            </p>
          </article>
          <article>
            <h2>Challenges in Greenhouse Farming</h2>
            <p>
              Despite its benefits, greenhouse farming can also present challenges. High initial costs, energy consumption, and the need for constant monitoring of temperature, humidity, and other factors are some of the key challenges faced by greenhouse operators. However, advancements in automation and technology are helping to address these issues.
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
  
  .overview-metrics {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 30px;
    margin-top: 30px;
  }
  
  .overview-card {
    padding: 1.8rem;
    border-radius: 10px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    text-align: center;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }
  
  .overview-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
  }
  
  .overview-card h2 {
    font-size: 1.5rem;
    margin-bottom: 10px;
  }
  
  .overview-card p {
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
  
  .articles {
    margin-top: 40px;
  }
  
  .articles article {
    margin-bottom: 30px;
    padding: 20px;
    background: #fff;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  }
  
  .articles h2 {
    font-size: 1.8rem;
    color: #34495e;
    margin-bottom: 15px;
  }
  
  .articles p {
    font-size: 1.1rem;
    color: #7f8c8d;
    line-height: 1.6;
  }
  
  @media (max-width: 1024px) {
    main{
    margin-top: 30%;
  }
    .overview-metrics {
      grid-template-columns: repeat(2, 1fr);
    }
  
  }
  
  @media (max-width: 768px) {
    main{
      margin-top: 30%;
    }
    .overview-metrics {
      grid-template-columns: 1fr;
    }
    header h1 {
      font-size: 2rem;
    }
  
    header p {
      font-size: 1rem;
    }
  
    .overview-card {
      padding: 1.5rem;
    }
  
    .overview-card h2 {
      font-size: 1.3rem;
    }
  
    .overview-card p {
      font-size: 1.8rem;
    }
  
    .articles h2 {
      font-size: 1.5rem;
    }
  
    .articles p {
      font-size: 1rem;
    }
  }
  
  @media (max-width: 600px) {
    main{
      margin-top: 800px;
    }
  }
  @media (max-width: 480px) {
    main{
      margin-top: 800px;
    }
  
    .overview-metrics {
      margin-top: 20px;
    }
  
    .overview-card {
      padding: 1rem;
    }
  
    .overview-card h2 {
      font-size: 1.2rem;
    }
  
    .overview-card p {
      font-size: 1.5rem;
    }
  }
  </style>
  