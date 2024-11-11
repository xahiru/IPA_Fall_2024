<template>
  <div :class="['dashboard', theme]">
    <aside class="sidebar">
      <h2>Dashboard</h2>
      <ul class="nav-links">
        <li :class="{ active: currentSection === 'Overview' }" @click="navigateTo('Overview')">Overview</li>
        <li :class="{ active: currentSection === 'Settings' }" @click="navigateTo('Settings')">Settings</li>
        <li :class="{ active: currentSection === 'Logs' }" @click="navigateTo('Logs')">Logs</li>
      </ul>
    </aside>

    <main class="main-content">
      <div v-if="currentSection === 'Overview'" class="section">
        <h3>Overview</h3>
        <p>Welcome to the Overview section.</p>
      </div>
      <div v-if="currentSection === 'Settings'" class="section">
        <h3>Settings</h3>
        <label class="theme-toggle">
          <input type="checkbox" v-model="isDarkMode" @change="toggleTheme" />
          Dark Mode
        </label>
        <p>Adjust your settings here.</p>
        <button @click="logout" class="logout-button">Logout</button>
      </div>
      <div v-if="currentSection === 'Logs'" class="section">
        <h3>Logs</h3>
        <p>View your activity logs here.</p>
      </div>
    </main>
  </div>
</template>

<script>
export default {
  name: "Dashboard",
  data() {
    return {
      currentSection: "Overview",
      isDarkMode: false,
    };
  },
  computed: {
    theme() {
      return this.isDarkMode ? 'dark-mode' : 'light-mode';
    },
  },
  methods: {
    navigateTo(section) {
      this.currentSection = section;
    },
    toggleTheme() {
      this.isDarkMode = !this.isDarkMode;
    },
    logout() {
      // Redirect to Home page when logging out
      this.$router.push({ name: 'Home' });
    },
  },
};
</script>



<style scoped>
.light-mode {
  --bg-color: #f4f4f4;
  --text-color: #333;
  --sidebar-bg: #333;
  --sidebar-text: #fff;
  --content-bg: #fff;
}

.dark-mode {
  --bg-color: #2c2c2c;
  --text-color: #f4f4f4;
  --sidebar-bg: #444;
  --sidebar-text: #ddd;
  --content-bg: #333;
}

.dashboard {
  display: flex;
  height: 100vh;
  font-family: Arial, sans-serif;
  background-color: var(--bg-color);
  color: var(--text-color);
}


.sidebar {
  width: 220px;
  background-color: var(--sidebar-bg);
  color: var(--sidebar-text);
  padding: 20px;
  display: flex;
  flex-direction: column;
}

.sidebar h2 {
  margin-bottom: 30px;
  font-size: 24px;
  color: var(--sidebar-text);
}

.nav-links {
  list-style: none;
  padding: 0;
}

.nav-links li {
  padding: 10px 0;
  cursor: pointer;
  color: var(--sidebar-text);
  transition: background 0.3s;
}

.nav-links li:hover,
.nav-links li.active {
  background-color: #555;
  border-radius: 4px;
  color: #fff;
  padding-left: 10px;
}

.main-content {
  flex: 1;
  padding: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: var(--content-bg);
}

.section {
  background: var(--bg-color);
  padding: 30px;
  border-radius: 8px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  max-width: 800px;
  width: 100%;
  text-align: center;
}

.theme-toggle {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-top: 15px;
}

.logout-button {
  margin-top: 20px;
  padding: 10px 20px;
  background-color: #d9534f;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background 0.3s;
}

.logout-button:hover {
  background-color: #c9302c;
}

@media (max-width: 768px) {
  .dashboard {
    flex-direction: column;
  }

  .sidebar {
    width: 100%;
    text-align: center;
  }

  .main-content {
    padding: 10px;
  }

  .section {
    width: 90%;
  }
}
</style>
