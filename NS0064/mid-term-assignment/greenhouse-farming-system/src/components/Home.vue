<script setup>

</script>

<template>
  <main id="agri-dashboard">
    
    <section class="intro-section">
      <div class="branding">
        <h1 class="app-title">EcoGrow Home Page </h1>
        <p class="app-subtitle">Innovative solutions for high-yield farming</p>
      </div>
    </section>
    
    <section class="feature-section">
      <div class="feature-intro">
        <p>EcoGrow provides a comprehensive greenhouse management system that allows you to:</p>
      </div>
      <div class="features-grid">
        <div class="feature-item">🌡️ Monitor temperature & humidity</div>
        <div class="feature-item">💧 Automated watering & lighting</div>
        <div class="feature-item">📊 Data insights for optimal growth</div>
      </div>
    </section>
    
    <section class="cta-section">
      <router-link to="/login" class="cta-btn login-btn">Log In</router-link>
      <router-link to="/sign-up" class="cta-btn signup-btn">Sign Up</router-link>
    </section>
    
  </main>
</template>

<script>
function goToLogin() {
  window.location.href = '/login';
}

function goToSignup() {
  window.location.href = '/signup';
}
</script>

<style scoped>
#agri-dashboard{
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

#agri-dashboard {
  font-family: 'Arial', sans-serif;
  background: #e0f7f4;
  color: #34495e;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem;
  gap: 2rem;
  min-height: 100vh;
}

.intro-section {
  background: #ffffff;
  padding: 1.5rem 2rem;
  text-align: center;
  border-radius: 12px;
  box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.1);
  max-width: 400px;
  width: 100%;
}

.branding .app-title {
  font-size: 2.2rem;
  color: #2c3e50;
  margin-bottom: 0.5rem;
}

.branding .app-subtitle {
  font-size: 1.1rem;
  color: #7f8c8d;
}

.feature-section {
  max-width: 500px;
  width: 100%;
}

.feature-intro {
  text-align: center;
  font-size: 1rem;
  color: #555;
  margin-bottom: 1.5rem;
}

.features-grid {
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
}

.feature-item {
  background: #dff0d8;
  color: #2e7d32;
  padding: 0.8rem;
  border-radius: 8px;
  text-align: center;
  font-size: 1rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.cta-section {
  display: flex;
  gap: 1rem;
}

.cta-btn {
  background-color: #3498db;
  color: white;
  padding: 0.8rem 1.5rem;
  border: none;
  border-radius: 6px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.cta-btn.signup-btn {
  background-color: #27ae60;
}

.cta-btn:hover {
  opacity: 0.9;
}
</style>
