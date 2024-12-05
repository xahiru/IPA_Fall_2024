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
  height: 100vh;
  background-color: #f4f6f9;
}

.dashboard-layout {
  display: flex;
  flex-grow: 1;
  gap: 2rem;
  padding: 2rem;
  overflow: hidden;
}

@media (max-width: 768px) {
  .dashboard-layout {
    flex-direction: column;
    padding: 1rem;
  }
}

@media (max-width: 480px) {
  .dashboard-layout {
    padding: 0.5rem;
  }
}
</style>