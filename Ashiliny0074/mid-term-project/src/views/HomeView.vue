<template>
  <div class="min-h-screen bg-gradient-to-r from-green-400 to-blue-500">
    <div class="flex flex-col items-center justify-center min-h-screen px-4 sm:px-6 lg:px-8">
      <!-- Title Section -->
      <div class="text-center mb-12">
        <h1 class="text-5xl font-extrabold text-white mb-4 tracking-tight sm:text-6xl lg:text-7xl">
          Smart Greenhouse
        </h1>
        <h2 class="text-4xl font-bold text-blue-100 mb-8 sm:text-5xl lg:text-6xl">
          Monitoring System
        </h2>
        <p class="max-w-2xl mx-auto text-xl text-white mb-12">
          Monitor your greenhouse environment in real-time. Track temperature, humidity, soil 
          moisture, and light levels to ensure optimal growing conditions.
        </p>
      </div>

      <!-- Buttons -->
      <div class="flex flex-col sm:flex-row gap-4 w-full max-w-md mx-auto">
        <router-link 
          to="/login" 
          class="flex-1 px-8 py-3 text-center bg-white text-blue-600 rounded-lg font-semibold hover:bg-blue-50 transition-colors duration-200"
        >
          Login to Get Started
        </router-link>
        <router-link 
          to="/register" 
          class="flex-1 px-8 py-3 text-center bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 transition-colors duration-200"
        >
          Register
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()
</script>

<style scoped>
.bg-gradient-to-r {
  background-image: linear-gradient(to right, rgba(52, 211, 153, 1), rgba(59, 130, 246, 1));
}

/* Add some animation */
h1, h2 {
  animation: fadeInDown 1s ease-out;
}

p {
  animation: fadeIn 1s ease-out 0.5s both;
}

.router-link-active {
  animation: fadeIn 1s ease-out 1s both;
}

@keyframes fadeInDown {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
</style>