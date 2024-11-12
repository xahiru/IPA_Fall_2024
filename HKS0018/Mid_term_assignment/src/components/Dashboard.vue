<template>
  <div class="dashboard">
    <aside class="sidebar">
      <h2>Dashboard</h2>
      <ul class="nav-links">
        <li :class="{ active: currentSection === 'Overview' }" @click="navigateTo('Overview')">Overview</li>
        <li :class="{ active: currentSection === 'Data Display' }" @click="navigateTo('Data Display')">Data Display</li>
        <li :class="{ active: currentSection === 'Settings' }" @click="navigateTo('Settings')">Settings</li>
        <li :class="{ active: currentSection === 'Logs' }" @click="navigateTo('Logs')">Logs</li>
      </ul>
      <button class="logout-button" @click="logout">Logout</button>
    </aside>

    <main class="main-content">
      <div v-if="currentSection === 'Overview'" class="section">
        <h3>Overview</h3>
        <p>Welcome to the Overview section.</p>
      </div>

      <div v-if="currentSection === 'Data Display'" class="section">
        <DataDisplay />
      </div>

      <div v-if="currentSection === 'Settings'" class="section">
        <Settings />
      </div>

      <div v-if="currentSection === 'Logs'" class="section">
        <Logs/>
      </div>
    </main>
  </div>
</template>

<script>
import DataDisplay from './DataDisplay.vue';
import Settings from './Settings.vue';
import Logs from './Logs.vue';

export default {
  name: "Dashboard",
  components: {
    DataDisplay,
    Settings,
    Logs,
  },
  data() {
    return {
      currentSection: "Overview",
    };
  },
  methods: {
    navigateTo(section) {
      this.currentSection = section;
    },
    logout() {
      this.$router.push({ name: 'Home' });
    },
  },
};
</script>

<style scoped>
.dashboard {
  display: flex;
  height: 100vh;
  font-family: Arial, sans-serif;
  background-color: #f4f4f4;
  color: #333;
}

.sidebar {
  width: 220px;
  background-color: #333;
  color: #fff;
  padding: 20px;
  display: flex;
  flex-direction: column;
}

.sidebar h2 {
  margin-bottom: 30px;
  font-size: 24px;
  color: #fff;
}

.nav-links {
  list-style: none;
  padding: 0;
}

.nav-links li {
  padding: 10px 0;
  cursor: pointer;
  color: #fff;
  transition: background 0.3s;
}

.nav-links li:hover,
.nav-links li.active {
  background-color: #555;
  border-radius: 4px;
  color: #fff;
  padding-left: 10px;
}


.logout-button {
  margin-top: 30px;
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

.main-content {
  flex: 1;
  padding: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #fff;
}

.section {
  background: #f4f4f4;
  padding: 30px;
  border-radius: 8px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  max-width: 800px;
  width: 100%;
  text-align: center;
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
