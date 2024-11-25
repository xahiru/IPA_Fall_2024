<script setup>

</script>

<template>
  <main id="login-page">
    <section class="login-container">
      <header class="login-header">
        <h1 class="login-title">Welcome Back to EcoGrow</h1>
        <p class="login-subtitle">Log in to manage your greenhouse</p>
      </header>
      
      <form class="login-form">
        <label for="email" class="input-label">Email</label>
        <input type="email" id="email" class="input-field" placeholder="Enter your email" required>
        
        <label for="password" class="input-label">Password</label>
        <input type="password" id="password" class="input-field" placeholder="Enter your password" required>
        
        <button type="submit" class="login-btn">Log In</button>
      </form>
      
      <footer class="login-footer">
        <p class="signup-link">
          Don’t have an account? 
          <router-link to="/sign-up" class="signup-link-text">Sign up here</router-link>
        </p>
      </footer>
    </section>
  </main>
</template>

<style scoped>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

#login-page {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: #e0f7f4;
  font-family: 'Arial', sans-serif;
  padding: 2rem;
}

.login-container {
  background-color: #ffffff;
  padding: 2rem;
  width: 100%;
  max-width: 400px;
  border-radius: 12px;
  box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.login-header {
  margin-bottom: 2rem;
}

.login-title {
  font-size: 2rem;
  color: #2c3e50;
}

.login-subtitle {
  font-size: 1rem;
  color: #7f8c8d;
}

.login-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.input-label {
  text-align: left;
  font-size: 0.9rem;
  color: #555555;
}

.input-field {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-size: 1rem;
}

.input-field:focus {
  outline: none;
  border-color: #3498db;
  box-shadow: 0 0 8px rgba(52, 152, 219, 0.2);
}

.login-btn {
  background-color: #3498db;
  color: white;
  padding: 0.75rem;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.login-btn:hover {
  background-color: #2980b9;
}

.login-footer {
  margin-top: 1.5rem;
}

.signup-link {
  font-size: 0.9rem;
  color: #7f8c8d;
}

.signup-link-text {
  color: #3498db;
  text-decoration: none;
  font-weight: bold;
}

.signup-link-text:hover {
  text-decoration: underline;
}
</style>
