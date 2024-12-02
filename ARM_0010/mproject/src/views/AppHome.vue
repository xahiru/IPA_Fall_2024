<template>
  <div class="home-container">
    <!-- Navbar -->
    <header class="navbar">
      <div class="navbar-container">
        <div class="logo">Greenhouse</div>
        <nav>
          <ul class="nav-links">
            <li><router-link to="/" class="nav-link">Home</router-link></li>
            <li><router-link to="/login" class="nav-link">Login</router-link></li>
            <li><router-link to="/register" class="nav-link">Register</router-link></li>
          </ul>
        </nav>
      </div>
    </header>

    <!-- Main Content Section -->
    <div class="content-wrapper">
      <div class="welcome-card">
        <h2>Welcome to the Greenhouse Monitoring System</h2>
        <p>Manage and monitor your greenhouse in real-time with our easy-to-use system.</p>
        <div class="action-buttons">
          <router-link to="/login" class="btn login-btn">Login</router-link>
          <router-link to="/register" class="btn register-btn">Register</router-link>
        </div>
      </div>
    </div>

    <!-- More Content Section -->
    <div class="more-content">
      <h3>Features of Greenhouse Monitoring</h3>
      <p>Our system helps you track temperature, humidity, soil moisture, and more with real-time alerts to optimize your greenhouse environment.</p>
      <ul>
        <li>Automated Climate Control</li>
        <li>Real-Time Data Analytics</li>
        <li>Customizable Alerts and Notifications</li>
      </ul>
    </div>

    <!-- Footer -->
    <footer class="footer">
      <p>&copy; 2024 Greenhouse Monitoring | All rights reserved</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'AppHome',
};
</script>

<style scoped>
/* General page styling */
.home-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
  font-family: 'Roboto', sans-serif;
  background: linear-gradient(135deg, #74ebd5, #9face6); /* Soft gradient background */
  color: #fff;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Navbar Styling */
.navbar {
  background-color: #333;
  padding: 10px 20px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.navbar-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  font-size: 1.8rem;
  font-weight: 600;
  color: #fff;
  text-transform: uppercase;
}

.nav-links {
  display: flex;
  list-style: none;
  gap: 20px;
}

.nav-link {
  color: #fff;
  text-decoration: none;
  font-size: 1.1rem;
  transition: color 0.3s ease;
}

.nav-link:hover {
  color: #74ebd5;
}

/* Main Content Styling */
.content-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-grow: 1;
  background: url('https://source.unsplash.com/1600x900/?greenhouse') no-repeat center center;
  background-size: cover;
  text-align: center;
  padding: 40px;
}

.welcome-card {
  background: rgba(0, 0, 0, 0.7); /* Dark overlay to make text more readable */
  padding: 40px;
  border-radius: 15px;
  max-width: 500px;
  width: 100%;
  box-shadow: 0 8px 15px rgba(0, 0, 0, 0.3);
}

h2 {
  font-size: 2.8rem;
  font-weight: 700;
  margin-bottom: 20px;
  text-shadow: 3px 3px 15px rgba(0, 0, 0, 0.5);
}

p {
  font-size: 1.2rem;
  margin-bottom: 30px;
  font-weight: 300;
  line-height: 1.5;
}

.action-buttons {
  display: flex;
  gap: 20px;
  justify-content: center;
}

.btn {
  text-decoration: none;
  padding: 15px 35px;
  font-size: 1.1rem;
  font-weight: 500;
  border-radius: 50px;
  transition: all 0.3s ease;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.login-btn {
  background-color: #4CAF50; /* Green */
  color: white;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.register-btn {
  background-color: #ff5733; /* Orange */
  color: white;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.btn:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2);
}

/* More Content Section */
.more-content {
  padding: 40px;
  background: rgba(0, 0, 0, 0.7); /* Dark overlay */
  text-align: center;
}

.more-content h3 {
  font-size: 2.5rem;
  font-weight: 600;
  margin-bottom: 20px;
}

.more-content ul {
  list-style-type: none;
  padding: 0;
}

.more-content li {
  font-size: 1.2rem;
  margin: 10px 0;
}

/* Footer Styling */
.footer {
  text-align: center;
  padding: 20px;
  background-color: rgba(0, 0, 0, 0.7);
  color: #ddd;
  font-size: 0.9rem;
}

/* Responsive Design */
@media (max-width: 768px) {
  .navbar-container {
    flex-direction: column;
    text-align: center;
  }

  .nav-links {
    flex-direction: column;
    gap: 10px;
  }

  .content-wrapper {
    flex-direction: column;
    padding: 30px;
  }

  h2 {
    font-size: 2.5rem;
  }

  p {
    font-size: 1rem;
  }

  .action-buttons {
    flex-direction: column;
    gap: 15px;
  }

  .more-content {
    padding: 20px;
  }
}
</style>
