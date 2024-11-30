<template>
    <div class="home">
      <section class="hero">
        <h1>Welcome to the Greenhouse Monitoring Dashboard</h1>
        <p>Track and manage your greenhouse environment in real-time.</p>
        <router-link to="/dashboard" class="btn">Go to Dashboard</router-link>
      </section>
  
      <section class="features">
        <h2>Features</h2>
        <div class="feature-grid">
          <div class="feature">
            <h3>Real-Time Data</h3>
            <p>Monitor temperature, humidity, soil moisture, and light levels instantly.</p>
          </div>
          <div class="feature">
            <h3>Custom Alerts</h3>
            <p>Set alerts for specific environmental conditions.</p>
          </div>
          <div class="feature">
            <h3>Interactive Charts</h3>
            <p>Analyze trends with interactive visualizations.</p>
          </div>
        </div>
      </section>
    </div>
  </template>
  
  <script>
  export default {
    name: "Home",
  };
  </script>
  
  <style scoped>
  .hero {
    text-align: center;
    padding: 50px 20px;
    background-color: #f4f9f9;
  }
  
  .hero h1 {
    font-size: 2.5rem;
    color: #2a9d8f;
  }
  
  .hero p {
    font-size: 1.2rem;
    color: #264653;
    margin: 10px 0 20px;
  }
  
  .hero .btn {
    display: inline-block;
    padding: 10px 20px;
    font-size: 1rem;
    color: white;
    background-color: #2a9d8f;
    border-radius: 5px;
    text-decoration: none;
  }
  
  .hero .btn:hover {
    background-color: #21867a;
  }
  
  .features {
    padding: 40px 20px;
  }
  
  .features h2 {
    text-align: center;
    margin-bottom: 30px;
    font-size: 2rem;
    color: #264653;
  }
  
  .feature-grid {
    display: flex;
    gap: 20px;
    flex-wrap: wrap;
    justify-content: center;
  }
  
  .feature {
    flex: 1 1 300px;
    padding: 20px;
    border: 1px solid #e1e1e1;
    border-radius: 10px;
    text-align: center;
    background-color: #fff;
  }
  
  .feature h3 {
    font-size: 1.5rem;
    color: #2a9d8f;
  }
  
  .feature p {
    font-size: 1rem;
    color: #606c76;
  }
  </style>
  