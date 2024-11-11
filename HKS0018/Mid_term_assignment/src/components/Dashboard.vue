<template>
    <div class="dashboard">
      <!-- Navigation Bar -->
      <nav class="navbar">
        <h2>Dashboard</h2>
        <ul class="nav-links">
          <li @click="navigateTo('Overview')">Overview</li>
          <li @click="navigateTo('Settings')">Settings</li>
          <li @click="navigateTo('Logs')">Logs</li>
        </ul>
      </nav>
  
      <!-- Main Content -->
      <div class="content">
        <div v-if="currentSection === 'Overview'" class="section">
          <h3>Overview</h3>
          <p>Welcome to the Overview section.</p>
        </div>
        <div v-if="currentSection === 'Settings'" class="section">
          <h3>Settings</h3>
          <p>Adjust your settings here.</p>
        </div>
        <div v-if="currentSection === 'Logs'" class="section">
          <h3>Logs</h3>
          <p>View your activity logs here.</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "Dashboard",
    data() {
      return {
        currentSection: "Overview",
      };
    },
    methods: {
      navigateTo(section) {
        this.currentSection = section;
      },
    },
  };
  </script>
  
  <style scoped>
  /* Overall Layout */
  .dashboard {
    display: flex;
    flex-direction: column;
    height: 100vh;
    font-family: Arial, sans-serif;
  }
  
  /* Navigation Bar */
  .navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px;
    background-color: #333;
    color: white;
  }
  
  .navbar h2 {
    margin: 0;
  }
  
  .nav-links {
    list-style: none;
    display: flex;
    gap: 20px;
  }
  
  .nav-links li {
    cursor: pointer;
    color: white;
  }
  
  .nav-links li:hover {
    text-decoration: underline;
  }
  
  /* Main Content Area */
  .content {
    flex: 1;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px;
    background-color: #f4f4f4;
  }
  
  /* Section Styles */
  .section {
    background: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    max-width: 600px;
    width: 100%;
  }
  
  /* Responsive Adjustments */
  @media (max-width: 600px) {
    .navbar {
      flex-direction: column;
      gap: 10px;
      text-align: center;
    }
  
    .nav-links {
      flex-direction: column;
    }
  
    .section {
      width: 90%;
    }
  }
  </style>
  