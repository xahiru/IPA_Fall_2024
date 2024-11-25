<template>
    <div id="dashboard">
      <!-- Navbar -->
      <nav class="navbar">
        <div class="logo">Greenhouse</div>
        <ul class="nav-links">
          <li><router-link to="/">Home</router-link></li>
          <li><router-link to="/dashboard">Dashboard</router-link></li>
          <li><router-link to="/overview">Overview</router-link></li>
          <li><router-link to="/settings">Settings</router-link></li>
          <li><a @click="logout">Logout</a></li>
        </ul>
      </nav>
  
      <!-- Settings Panel -->
      <div class="content">
        <h1 class="title">Settings Panel</h1>
        <p class="subtitle">Set thresholds and control alerts dynamically.</p>
  
        <form class="settings-form">
          <div class="form-group">
            <label for="temperature">Temperature Threshold (°C):</label>
            <input type="number" id="temperature" class="input-field" />
            <div class="toggle">
              <input type="checkbox" id="temperature-alert" />
              <label for="temperature-alert">Enable Temperature Alerts</label>
            </div>
          </div>
  
          <div class="form-group">
            <label for="humidity">Humidity Threshold (%):</label>
            <input type="number" id="humidity" class="input-field" />
            <div class="toggle">
              <input type="checkbox" id="humidity-alert" />
              <label for="humidity-alert">Enable Humidity Alerts</label>
            </div>
          </div>
  
          <div class="form-group">
            <label for="light">Light Threshold (lux):</label>
            <input type="number" id="light" class="input-field" />
            <div class="toggle">
              <input type="checkbox" id="light-alert" />
              <label for="light-alert">Enable Light Alerts</label>
            </div>
          </div>
  
          <div class="form-group">
            <label for="moisture">Moisture Threshold (%):</label>
            <input type="number" id="moisture" class="input-field" />
            <div class="toggle">
              <input type="checkbox" id="moisture-alert" />
              <label for="moisture-alert">Enable Moisture Alerts</label>
            </div>
          </div>
  
          <button type="button" class="button save-button">
            Save Settings
          </button>
        </form>
      </div>
    </div>
  </template>
  
  <script setup>
  const logout = async () => {
    localStorage.removeItem("user");
    window.location.href = "/login";
  };
  

  </script>
  
  <style scoped>
  /* Reset styles */
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
  
  /* Page and layout styles */
  #dashboard {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
    background: #f4f6f9;
    color: #333;
  }
  
  .content {
    padding: 2rem;
    margin: 80px auto 0; /* Adjust for navbar height */
    max-width: 600px;
    background: white;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  }
  
  /* Navbar styles */
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
  
  .nav-links a {
    color: #ffffff;
    text-decoration: none;
    font-size: 1.1rem;
    font-weight: 500;
  }
  
  .nav-links a:hover {
    color: #00aaff;
  }
  
  /* Typography and form styles */
  .title {
    font-size: 1.8rem;
    font-weight: bold;
    color: #2d3e50;
    margin-bottom: 1rem;
    text-align: center;
  }
  
  .subtitle {
    font-size: 1rem;
    color: #7f8c8d;
    margin-bottom: 2rem;
    text-align: center;
  }
  
  .settings-form {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
  }
  
  .form-group {
    display: flex;
    flex-direction: column;
  }
  
  label {
    font-size: 1rem;
    margin-bottom: 0.5rem;
    color: #2d3e50;
  }
  
  .input-field {
    padding: 0.8rem;
    font-size: 1rem;
    border: 1px solid #ccc;
    border-radius: 5px;
    outline: none;
  }
  
  .input-field:focus {
    border-color: #00aaff;
    box-shadow: 0 0 5px rgba(0, 170, 255, 0.5);
  }
  
  .toggle {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-top: 0.5rem;
  }
  
  .toggle label {
    font-size: 0.9rem;
    color: #34495e;
  }
  
  /* Buttons */
  .button {
    padding: 0.8rem;
    font-size: 1rem;
    font-weight: bold;
    color: white;
    background-color: #2d3e50;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  .button:hover {
    background-color: #1a2736;
  }
  </style>
  