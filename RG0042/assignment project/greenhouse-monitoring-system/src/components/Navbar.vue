<template>
  <nav class="navbar">
    <router-link to="/" class="logo">Greenhouse Dashboard</router-link>
    <button class="menu-toggle" @click="toggleMenu">
      <span :class="menuOpen ? 'open' : ''"></span>
    </button>
    <div class="nav-links" :class="{ 'show-menu': menuOpen }">
      <router-link to="/overview">Overview</router-link>
      <router-link to="/settingspanel">Settings</router-link>
      <router-link to="/logs">Logs</router-link>
      <router-link to="/login" @click.prevent="logout">Logout</router-link>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Navbar",
  data() {
    return {
      menuOpen: false,
    };
  },
  methods: {
    toggleMenu() {
      this.menuOpen = !this.menuOpen;
    },
    logout() {
      localStorage.removeItem('isAuthenticated');
      this.$router.push('/login');
    },
  },
};
</script>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background-color: #3b82f6;
  color: white;
  position: relative;
  width: auto;
  
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
  color: white;
  text-decoration: none;
}

.nav-links {
  display: flex;
  gap: 1rem;
  align-items: center;
}

.nav-links a {
  color: white;
  text-decoration: none;
}

.nav-links a:hover {
  text-decoration: underline;
}

.menu-toggle {
  display: none;
  background: none;
  border: none;
  cursor: pointer;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 30px;
  height: 30px;
}

.menu-toggle span,
.menu-toggle span::before,
.menu-toggle span::after {
  content: '';
  display: block;
  background-color: white;
  height: 2px;
  width: 100%;
  transition: transform 0.3s ease-in-out;
}

.menu-toggle span::before {
  transform: translateY(-8px);
}

.menu-toggle span::after {
  transform: translateY(8px);
}

.menu-toggle span.open {
  background-color: transparent;
}

.menu-toggle span.open::before {
  transform: rotate(45deg) translate(5px, 5px);
}

.menu-toggle span.open::after {
  transform: rotate(-45deg) translate(5px, -5px);
}

@media (max-width: 768px) {
  .nav-links {
    position: absolute;
    top: 100%;
    right: 0;
    flex-direction: column;
    background-color: #3b82f6;
    width: 100%;
    display: none;
    gap: 1rem;
  }

  .nav-links.show-menu {
    display: flex;
  }

  .nav-links a {
    text-align: center;
    width: 100%;
  }

  .menu-toggle {
    display: flex;
  }
}
</style>