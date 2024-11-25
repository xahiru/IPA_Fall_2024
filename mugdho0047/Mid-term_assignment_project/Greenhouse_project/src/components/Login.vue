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
        <input type="email" id="email" class="input-field" placeholder="Enter your email" required />
        <input type="password" id="password" class="input-field" placeholder="Enter your password" required />
        <button type="submit" class="button login-button">Login</button>
        <p class="signup-prompt">Don't have an account? <a href="/signup" class="signup-link">Sign up here</a></p>
      </form>
    </div>
  </div>
</template>

<style scoped>
#bdy {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: 'Nunito', sans-serif;
  background: linear-gradient(135deg, #af30d6, #a375ff, #d1b6ff);
  color: #178304;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  margin: 0;
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
  font-size: 2.8rem;
  font-weight: 800;
  color: #ffffff;
  text-shadow: 3px 3px 10px rgba(0, 0, 0, 0.3);
}

.subtitle {
  font-size: 1.2rem;
  color: #d1f7e1;
  margin-top: 10px;
  text-shadow: 1px 1px 6px rgba(0, 0, 0, 0.3);
}

.login-form {
  display: flex;
  flex-direction: column;
  gap: 15px;
  background: rgba(255, 255, 255, 0.25);
  padding: 35px;
  border-radius: 12px;
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.2);
}

.input-field {
  padding: 12px 18px;
  font-size: 1.1rem;
  border: none;
  border-radius: 8px;
  outline: none;
  background: rgba(255, 255, 255, 0.5);
  transition: background 0.2s ease, box-shadow 0.2s ease;
}

.input-field:focus {
  background: #ffffff;
  box-shadow: 0 0 8px rgba(34, 139, 230, 0.4);
}

.button {
  padding: 14px 22px;
  font-size: 1.1rem;
  font-weight: 700;
  color: #ffffff;
  background-color: #021e2b;
  border: none;
  cursor: pointer;
  border-radius: 10px;
  transition: background 0.3s ease, transform 0.2s ease;
}

.button:hover {
  background-color: #227093;
  transform: translateY(-2px);
}

.signup-prompt {
  margin-top: 20px;
  font-size: 1rem;
  color: #d1f7e1;
}

.signup-link {
  color: #ffffff;
  font-weight: 600;
  text-decoration: underline;
  transition: color 0.3s ease;
}

.signup-link:hover {
  color: #98d4aa;
}
</style>
