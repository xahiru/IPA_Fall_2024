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
  height: auto;
  background-color: #f4f6f9;
}

.dashboard-content {
  flex-grow: 1;
  display: flex;
  justify-content: center;
  align-items: flex-start; /* Align content to the top of the screen */
  padding: 0.2rem;
  gap: 2rem;
  width: 100%; /* Ensure the content area is full width */
  height: auto;
}
  
@media (max-width: 768px) {
  .dashboard-content {
    padding: 1rem; /* Less padding on phones */
    gap: 1.2rem; /* Reduce gap between content items */
  }
  
  .dashboard {
    padding: 1rem; /* Reduce padding around the dashboard for small screens */
  }
}

/* Small Phones (up to 480px) */
@media (max-width: 480px) {
  .dashboard-content {
    padding: 0.1rem; /* Even smaller padding for very small screens */
    gap: 1rem;
  }
}  
</style>  