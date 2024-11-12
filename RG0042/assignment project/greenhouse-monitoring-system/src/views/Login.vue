<template>
    <div class="login-page">
      <div class="content-page">
        <h1>Login to Greenhouse Dashboard</h1>
        <form @submit.prevent="login">
          <div class="auth-buttons">
          <input type="text" v-model="username" placeholder="Username" />
          <br><br>
          <input type="password" v-model="password" placeholder="Password" />
          <br><br>
          <button type="submit">Login</button>
          <br>
          </div>
        </form>
  
          <p class="signup-prompt">Don't have an account? <a href="/signup" class="signup-link">Sign up here</a></p>
      </div>
    </div>  
  </template>
    
    
  <script>
    export default {
      data() {
        return { username: '', password: '' };
      },
      methods: {
        login() {
          // Mock login, store user in localStorage
          localStorage.setItem('auth', true);
          this.$router.push('/dashboard');
        },
      },
    };
  </script>
    
  
  <style scoped>
  .login-page {
      background-size: cover;
      background-position: center;
      background-repeat: no-repeat;
      height: 100vh;
      
      display: flex;
      flex-direction: column;
      text-align: center;
      align-items: center;
  }
  .content-page {
      background: rgba(222, 230, 224, 0.156);
      padding: 2rem;
      border-radius: 12px;
      max-width: 285px;
      width: 90%;
      text-align: center;
  }
  h1 {
      font-size: 2em;
      margin-bottom: 30px;
      color: white;
  }
  p {
      font-size: 1.2em;
      margin-bottom: 30px;
  }
  
  .auth-buttons{
    margin-top: 1.5rem;
    size: 8px;
  }
  
  button {
      margin: 0.5rem;
      padding: 0.75rem 1.5rem;
      font-size: 1rem;
      cursor: pointer;
      background-color: #3b82f6;
      color: aliceblue;
  }
  </style>