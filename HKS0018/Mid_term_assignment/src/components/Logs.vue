<template>
    <div class="logs">
      <h2>Activity Logs</h2>
      <p>View recent activities and alerts in your greenhouse system.</p>
      
      <div v-if="logs.length">
        <table class="logs-table">
          <thead>
            <tr>
              <th>Date</th>
              <th>Time</th>
              <th>Event</th>
              <th>Details</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="log in logs" :key="log.id">
              <td>{{ log.date }}</td>
              <td>{{ log.time }}</td>
              <td>{{ log.event }}</td>
              <td>{{ log.details }}</td>
            </tr>
          </tbody>
        </table>
      </div>
  
      <p v-else>No logs available at the moment.</p>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        logs: []
      };
    },
    mounted() {
      this.fetchLogs();
    },
    methods: {
      fetchLogs() {
        // Mock data for logs
        this.logs = [
          { id: 1, date: '2024-11-12', time: '10:00', event: 'Temperature Alert', details: 'Temperature exceeded 30°C' },
          { id: 2, date: '2024-11-12', time: '09:45', event: 'Humidity Change', details: 'Humidity dropped below 40%' },
          { id: 3, date: '2024-11-12', time: '09:30', event: 'Soil Moisture Level', details: 'Moisture level fell to 15%' },
          { id: 4, date: '2024-11-12', time: '09:00', event: 'Light Adjustment', details: 'Light intensity increased to 500 lux' }
        ];
      }
    }
  };
  </script>
  
  <style scoped>
  .logs {
    padding: 2rem;
    text-align: center;
  }
  
  .logs h2 {
    font-size: 2rem;
    margin-bottom: 1rem;
    color: #333;
  }
  
  .logs-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 1rem;
  }
  
  .logs-table th, .logs-table td {
    padding: 0.75rem;
    border: 1px solid #ddd;
    text-align: left;
  }
  
  .logs-table th {
    background-color: #f4f4f4;
    font-weight: bold;
  }
  
  .logs-table tr:nth-child(even) {
    background-color: #f9f9f9;
  }
  </style>
  