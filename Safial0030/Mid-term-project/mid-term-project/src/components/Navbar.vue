<!-- eslint-disable vue/multi-word-component-names -->
<template>
    <nav :style="{ backgroundColor: bgColor }" class="navbar navbar-expand-lg fixed-top">
      <div class="container">
        <a class="navbar-brand text-white" href="#">Safial's Greenhouse Monitoring (SGM)</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <router-link to="/dashboard" class="nav-link box">Dashboard</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/temperature-chart" class="nav-link box">Temperature Chart</router-link>
            </li>
            
            <li class="nav-item">
              <router-link to="/settings" class="nav-link box">Settings</router-link>
            </li>
            <li class="nav-item">
              <a class="nav-link box" href="#" @click.prevent="logout">Logout</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </template>
  
  <script>
  export default {
    props: {
      bgColor: {
        type: String,
        default: '#007bff',
      },
    },
    methods: {
      logout() {
        localStorage.removeItem('token');
        this.$router.push('/');
      },
    },
  };
  </script>
  
  <style scoped>
  .navbar {
    margin-bottom: 20px;
    padding: 1rem;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .nav-link {
    transition: color 0.3s ease;
  }
  
  .nav-link:hover {
    color: #ffc107;
  }
  
  .box {
    display: inline-block;
    padding: 10px 15px;
    margin: 5px;
    background-color: rgba(255, 255, 255, 0.1);
    border-radius: 5px;
    border: 1px solid transparent;
    color: white;
    text-decoration: none;
  }
  
  .box:hover {
    background-color: rgba(255, 255, 255, 0.2);
    border-color: rgba(255, 255, 255, 0.5);
  }
  </style>                         
  
  
  