<template>
    <aside class="sidebar">
      <ul>
        <li><router-link to="/overview">Overview</router-link></li>
        <li><router-link to="/settings">Settings</router-link></li>
        <li><router-link to="/logs">Logs</router-link></li>
        
      </ul>
    </aside>
  </template>
  
  <script>
  export default {
    name: "Sidebar",
  };
  </script>
  
  <style scoped>
  .sidebar {
    background-color: #f3f4f6;
    padding: 1rem;
    width: 250px;
  }
  
  .sidebar ul {
    list-style: none;
    padding: 0;
  }
  
  .sidebar li {
    margin: 1rem 0;
  }
  
  .sidebar a {
    color: #3b82f6;
    text-decoration: none;
    font-weight: bold;
  }
  
  .sidebar a:hover {
    text-decoration: underline;
  }
  </style>