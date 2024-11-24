<template>
    <div id="dashboard">
      <!-- Navbar -->
      <nav class="navbar">
        <div class="logo">Greenhouse</div>
        <ul class="nav-links">
          <li><router-link to="/">Home</router-link></li>
          <li><router-link to="/dashboard">Dashboard</router-link></li>
          <li><router-link to="/overview">Overview</router-link></li>
          <li><router-link to="/settings">Settings</router-link></li>
          <li><a @click="logout">Logout</a></li>
        </ul>
      </nav>

    </div>
</template>

<script setup>

const logout = async () => {
    localStorage.removeItem("user");
    window.location.href = '/login';
};

</script>


<style scoped>

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Roboto', sans-serif;
  background: #f4f6f9;
  color: #333;
  padding-top: 70px;
}

a:hover {
  cursor: pointer;
}

#dashboard {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.navbar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.2rem 2rem;
  background: #2d3e50;
  color: white;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  z-index: 100;
  overflow-x: auto;
}

.logo {
  font-size: 1.8rem;
  font-weight: bold;
  letter-spacing: 1px;
}

.nav-links {
  list-style: none;
  display: flex;
  gap: 30px;
}

.nav-links a {
  color: #ffffff;
  text-decoration: none;
  font-size: 1.1rem;
  font-weight: 500;
}

.nav-links a:hover {
  color: #00aaff;
}


</style>
