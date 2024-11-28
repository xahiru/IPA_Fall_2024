<template>
    <div class="logs-layout">
      <Navbar />
      <main class="logs-content">
        <header>
          <h1>System Logs</h1>
          <p>View the latest system activity and alerts</p>
        </header>
  
        <div class="logs-table">
          <table>
            <thead>
              <tr>
                <th>Timestamp</th>
                <th>Event</th>
                <th>Details</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="log in logs" :key="log.id">
                <td>{{ log.timestamp }}</td>
                <td>{{ log.event }}</td>
                <td>{{ log.details }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </main>
    </div>
  </template>
  
  <script>
import Navbar from '../components/Navbar.vue';
import logs from '../../db/logs.json';

export default {
  components: { Navbar },
  data() {
    return {
      logs
    };
  }
};
</script>
  
  <style scoped>
  .logs-layout {
    display: flex;
    flex-direction: column;
  }
  
  .logs-content {
    margin-top: 80px;
    padding: 2rem;
  }
  
  header {
    text-align: center;
    margin-bottom: 2rem;
  }
  
  .logs-table {
    overflow-x: auto;
    margin: 0 auto;
    max-width: 1000px;
  }
  
  table {
    width: 100%;
    border-collapse: collapse;
    background-color: #2e2e48;
    color: #fff;
  }
  
  th, td {
    padding: 1rem;
    text-align: left;
    border-bottom: 1px solid #444;
  }
  
  th {
    background-color: #1c1c2d;
  }
  
  tbody tr:hover {
    background-color: #383850;
  }
  </style>
  