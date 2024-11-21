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
  import DataCard from "@/components/DataCard.vue";
  import SettingsPanel from "@/components/SettingsPanel.vue";
  export default {
    name: "Dashboard",
    components: {
      Navbar,
      DashboardContent,
      DataCard,
      SettingsPanel,
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