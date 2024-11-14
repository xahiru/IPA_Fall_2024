<template>
    <div class="dashboard">
      <Navbar />
      <div class="dashboard-layout">
        <Sidebar />
        <DashboardContent />
      </div>
    </div>
  </template>
  
  <script>
  import Navbar from "@/components/Navbar.vue";
  import DashboardContent from "@/components/DashboardContent.vue";
  
  export default {
    name: "Dashboard",
    components: {
      Navbar,
      DashboardContent,
    },
  };
  </script>
  
  <style scoped>
  .dashboard {
    display: flex;
    flex-direction: column;
  }
  
  .dashboard-layout {
    display: flex;
    flex-grow: 1;
  }
  
  @media (max-width: 768px) {
    .dashboard-layout {
      flex-direction: column;
    }
  }
  </style>  