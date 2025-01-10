<template>
    <div class="not-found-container">
      <div class="content">
        <h1 class="error-code">404</h1>
        <h2 class="error-title">Oops! Page Not Found</h2>
        <p class="error-message">The page you're looking for has vanished into thin air.</p >
        <router-link to="/" class="home-button">Back to Home</router-link>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'NotFound'
  }
  </script>
  
  <style scoped>
  .not-found-container {
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #859398;
  }
  
  .content {
    text-align: center;
    padding: 2rem;
  }
  
  .error-code {
    font-size: 120px;
    color: #2c3e50;
    margin: 0;
    font-weight: bold;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
  }
  
  .error-title {
    font-size: 32px;
    color: #2c3e50;
    margin: 20px 0;
  }
  
  .error-message {
    font-size: 18px;
    color: #666;
    margin-bottom: 30px;
  }
  
  .home-button {
    display: inline-block;
    padding: 12px 30px;
    background-color: #3498db;
    color: white;
    text-decoration: none;
    border-radius: 25px;
    font-weight: bold;
    transition: background-color 0.3s ease;
  }
  
  .home-button:hover {
    background-color: #2980b9;
    transform: translateY(-2px);
  }
  
  @media (max-width: 768px) {
    .error-code {
      font-size: 80px;
    }
    
    .error-title {
      font-size: 24px;
    }
    
    .error-message {
      font-size: 16px;
    }
  }
  </style>