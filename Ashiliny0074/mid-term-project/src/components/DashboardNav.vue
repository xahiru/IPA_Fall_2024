<template>
  <nav class="bg-gradient-to-r from-blue-500 to-blue-700 shadow">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between h-16">
        <!-- Logo and Primary Nav -->
        <div class="flex">
          <div class="flex-shrink-0 flex items-center">
            <router-link to="/" class="text-xl font-bold text-white">
              GreenHouse Monitor
            </router-link>
          </div>
          <!-- Primary Nav Links -->
          <div class="hidden sm:ml-6 sm:flex sm:space-x-8">
            <router-link
              to="/dashboard"
              class="nav-link"
              :class="{ 'active-nav-link': currentRoute === 'dashboard' }"
            >
              Overview
            </router-link>
            <router-link
              to="/dashboard/metrics"
              class="nav-link"
              :class="{ 'active-nav-link': currentRoute === 'metrics' }"
            >
              Metrics
            </router-link>
            <router-link
              to="/dashboard/settings"
              class="nav-link"
              :class="{ 'active-nav-link': currentRoute === 'settings' }"
            >
              Settings
            </router-link>
            <router-link
              to="/dashboard/logs"
              class="nav-link"
              :class="{ 'active-nav-link': currentRoute === 'logs' }"
            >
              Logs
            </router-link>
          </div>
        </div>

        <!-- Right Side Nav -->
        <div class="hidden sm:ml-6 sm:flex sm:items-center">
          <button
            @click="logout"
            class="px-4 py-2 rounded-md text-white bg-red-600 hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
          >
            Logout
          </button>
        </div>

        <!-- Mobile menu button -->
        <div class="flex items-center sm:hidden">
          <button
            @click="isMobileMenuOpen = !isMobileMenuOpen"
            class="inline-flex items-center justify-center p-2 rounded-md text-white hover:text-gray-100 hover:bg-blue-800 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white"
          >
            <span class="sr-only">Open main menu</span>
            <!-- Menu icon -->
            <svg
              v-if="!isMobileMenuOpen"
              class="h-6 w-6"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
            </svg>
            <!-- Close icon -->
            <svg
              v-else
              class="h-6 w-6"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
      </div>
    </div>

    <!-- Mobile menu -->
    <div v-show="isMobileMenuOpen" class="sm:hidden">
      <div class="pt-2 pb-3 space-y-1">
        <router-link
          to="/dashboard"
          class="mobile-nav-link"
          :class="{ 'active-mobile-nav-link': currentRoute === 'dashboard' }"
        >
          Overview
        </router-link>
        <router-link
          to="/dashboard/metrics"
          class="mobile-nav-link"
          :class="{ 'active-mobile-nav-link': currentRoute === 'metrics' }"
        >
          Metrics
        </router-link>
        <router-link
          to="/dashboard/settings"
          class="mobile-nav-link"
          :class="{ 'active-mobile-nav-link': currentRoute === 'settings' }"
        >
          Settings
        </router-link>
        <router-link
          to="/dashboard/logs"
          class="mobile-nav-link"
          :class="{ 'active-mobile-nav-link': currentRoute === 'logs' }"
        >
          Logs
        </router-link>
        
      </div>
    </div>
  </nav>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';
import { useRouter, useRoute } from 'vue-router';

const router = useRouter();
const route = useRoute();

const isMobileMenuOpen = ref(false);
const currentRoute = computed(() => route.name);

const logout = () => {
  localStorage.removeItem('token');
  router.push({ name: 'home' }); // Navigate to the home route by name
};
</script>

<style scoped>
.nav-link {
  @apply inline-flex items-center px-1 pt-1 text-sm font-medium text-white hover:text-gray-100;
  @apply border-b-2 border-transparent hover:border-white;
}

.active-nav-link {
  @apply border-white text-white;
}

.mobile-nav-link {
  @apply block pl-3 pr-4 py-2 text-base font-medium text-white hover:text-gray-100 hover:bg-blue-800;
  @apply border-l-4 border-transparent;
}

.active-mobile-nav-link {
  @apply bg-blue-900 border-white text-white;
}
</style>