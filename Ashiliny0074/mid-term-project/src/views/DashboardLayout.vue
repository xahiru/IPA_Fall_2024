<template>
    <div class="min-h-screen bg-gray-100">
      <DashboardNav />
      
      <div class="py-6">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="bg-white shadow rounded-lg">
            <!-- Current page content -->
            <router-view></router-view>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  import DashboardNav from '../components/DashboardNav.vue';
  </script>