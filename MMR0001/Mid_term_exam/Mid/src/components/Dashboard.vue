<template>
    <div class="dashboard-container">
      <header class="dashboard-header">
    
        <h1>Greenhouse Farming Dashboard</h1>
        <button @click="logout">Logout</button>
      </header>
      <nav class="dashboard-nav">
        <button @click="selectTab('overview')" :class="{ active: activeTab === 'overview' }">Overview</button>
        <button @click="selectTab('settings')" :class="{ active: activeTab === 'settings' }">Settings</button>
        <button @click="selectTab('logs')" :class="{ active: activeTab === 'logs' }">Logs</button>
      </nav>
      <section class="dashboard-content">
        <div v-if="activeTab === 'overview'" class="overview-section">
          <h2>Overview of Greenhouse Farming with Technology</h2>
          <p>
            Greenhouse farming with technology allows farmers to monitor and control essential factors 
            such as temperature, humidity, and light levels. This approach increases crop yield, conserves 
            resources, and reduces dependency on external weather conditions. With advanced sensors and 
            monitoring tools, growers can achieve optimized growth for a variety of crops in a controlled 
            environment.
          </p>
        </div>
  
        <div v-if="activeTab === 'settings'">
          <h2>Settings</h2>
          <p>Configure alert thresholds and customize your dashboard here.</p>
        </div>
  
        <div v-if="activeTab === 'logs'">
          <h2>Logs</h2>
          <p>View system logs and historical data for analysis.</p>
        </div>
      </section>
    </div>
  </template>
  <script>
  export default {
    name: "Dashboard",
    data() {
      return {
        activeTab: "overview",
      };
    },
    methods: {
     logout() {
        localStorage.removeItem('authenticated');
        this.$router.push('/login');
      },
    },
  };
  </script>
  
  <style scoped>
  .dashboard-container {
    padding: 2em;
    text-align: center;
    font-family: Arial, sans-serif;
    color: #333;
  }
  
  .logo {
    width: 60px;
    height: 60px;
    margin-bottom: 0.5em;
  }
  .dashboard-header h1 {
    margin-top: 0;
    color: #4CAF50;
  }
  .dashboard-nav {
    display: flex;
    justify-content: center;
    margin: 1em 0;
    gap: 1em;
  }
  
  .dashboard-nav button {
    padding: 0.5em 1em;
    border: none;
    border-radius: 5px;
    background-color: #4CAF50;
    color: white;
    cursor: pointer;
    font-size: 1em;
    transition: background-color 0.3s ease;
  }
  
  .dashboard-nav button:hover {
    background-color: #45a049;
  }
  
  .dashboard-nav .active {
    background-color: #388E3C;
  }
  .dashboard-content {
    margin-top: 1.5em;
    text-align: left;
    padding: 1em 2em;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    background-color: #f9f9f9;
  }
  h2 {
    color: #4CAF50;
  }
  
  p {
    font-size: 1.1em;
    line-height: 1.6;
  }
  </style>
  