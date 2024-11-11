<script setup>
</script>

<template>
    <div id="bdy">
        <div class="login-page">
            <header class="header">
              <h1 class="title">Greenhouse Farming System</h1>
              <p class="subtitle">Login to access your dashboard</p>
            </header>
          
            <form class="login-form">
              <input type="email" id="email" class="input-field" placeholder="Enter your email" required>
          
              <input type="password" id="password" class="input-field" placeholder="Enter your password" required>
          
              <button type="submit" class="button login-button">Login</button>
              
              <p class="signup-prompt">Don't have an account? <a href="/signup" class="signup-link">Sign up here</a></p>
            </form>
          </div>
          
    </div>
</template>


<style>
#bdy{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }
  
  body {
    font-family: 'Roboto', sans-serif;
    background: linear-gradient(135deg, #18a0e9, #0d2495);
    color: #333;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
    margin: 0;
    color: #ffffff;
  }
  
  .login-page {
    text-align: center;
    max-width: 400px;
    width: 100%;
  }
  
  .header {
    margin-bottom: 30px;
  }
  
  .title {
    font-size: 2.5rem;
    font-weight: 700;
    color: #ffffff;
    text-shadow: 2px 2px 8px rgba(66, 65, 65, 0.3);
  }
  
  .subtitle {
    font-size: 1rem;
    color: #e0ffe6;
    margin-top: 10px;
    text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.2);
  }
  
  .login-form {
    display: flex;
    flex-direction: column;
    gap: 15px;
    background: rgba(255, 255, 255, 0.15);
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  }
  
  .input-field {
    padding: 10px 15px;
    font-size: 1rem;
    border: none;
    border-radius: 5px;
    outline: none;
    background: rgba(255, 255, 255, 0.474);
  }
  
  .input-field:focus {
    background: #ffffff;
  }
  
  .button {
    padding: 12px 20px;
    font-size: 1rem;
    font-weight: 600;
    color: white;
    background-color: #3498db;
    border: none;
    cursor: pointer;
    border-radius: 8px;
    transition: background 0.3s ease;
  }
  
  .button:hover {
    background-color: #2980b9;
  }
  
  .signup-prompt {
    margin-top: 20px;
    font-size: 0.9rem;
    color: #e0ffe6;
  }
  
  .signup-link {
    color: #ffffff;
    font-weight: 500;
    text-decoration: underline;
  }
  
  .signup-link:hover {
    color: #b0d8b0;
  }
  
</style>