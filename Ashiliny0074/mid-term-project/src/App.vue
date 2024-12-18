<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Main Content -->
    <main>
      <router-view v-slot="{ Component }">
        <transition name="fade" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </main>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import { useRouter, useRoute } from 'vue-router';

const router = useRouter();
const route = useRoute();

const isAuthenticated = computed(() => localStorage.getItem('token') !== null);

const handleLogout = () => {
  localStorage.removeItem('token');
  localStorage.removeItem('currentUser');
  router.push('/');
};
</script>

<style>
@import '@/assets/main.css';

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>