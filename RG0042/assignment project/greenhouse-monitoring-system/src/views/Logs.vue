<template>
    <div id="logs" class="logs-container">
      <Navbar />
      <h1 class="logs-title">System Logs</h1>
      <table class="logs-table">
        <thead>
          <tr>
            <th>Timestamp</th>
            <th>User</th>
            <th>Level</th>
            <th>Action</th>
            <th>Message</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(log, index) in logs" :key="index">
            <td>{{ log.timestamp }}</td>
            <td>{{ log.user }}</td>
            <td>
              <span :class="`log-level ${log.level}`">{{ log.level }}</span>
            </td>
            <td>{{ log.action }}</td>
            <td>{{ log.message }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
<script setup>
  import { ref, onMounted } from 'vue';
  import Navbar from '../components/Navbar.vue'; // Import Navbar component
  
  const logs = ref([]);
  
  const fetchLogs = async () => {
    try {
      const response = await fetch('/logs.json'); // Fetch from public folder
      logs.value = await response.json();
    } catch (error) {
      console.error('Error fetching logs:', error);
    }
  };
  
  onMounted(fetchLogs);
</script>
  
<style scoped>
  .logs-container {
    padding: 2rem;
    background-color: #f9f9f9;
    border-radius: 8px;
  }
  
  .logs-title {
    font-size: 2rem;
    font-weight: 700;
    color: #2c3e50;
    margin-bottom: 1.5rem;
  }
  
  .logs-table {
    width: 100%;
    border-collapse: collapse;
    background-color: #fff;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    border-radius: 8px;
    overflow: hidden;
  }
  
  .logs-table th,
  .logs-table td {
    padding: 1rem;
    text-align: left;
    border-bottom: 1px solid #ddd;
  }
  
  .logs-table th {
    background-color: #34495e;
    color: white;
  }
  
  .logs-table tr:last-child td {
    border-bottom: none;
  }
  
  .log-level {
    padding: 0.2rem 0.5rem;
    border-radius: 5px;
    color: white;
    font-weight: bold;
  }
  
  .log-level.info {
    background-color: #2d87f0;
  }
  
  .log-level.warning {
    background-color: #f1c40f;
  }
  
  .log-level.error {
    background-color: #e74c3c;
  }
  
  .log-level.success {
    background-color: #2ecc71;
  }
</style>  