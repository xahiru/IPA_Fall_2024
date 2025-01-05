<template>
  <v-app>
    <v-layout>
    <v-app-bar elevation="4" color="primary">
      <v-app-bar-title class="d-flex align-center">
        <v-icon size="32" color="primary" class="mr-2">mdi-greenhouse</v-icon>  
        Greenhouse Dashboard
      </v-app-bar-title>
      <v-spacer></v-spacer>
      <!-- Public Navigation -->
      <v-btn variant="text" to="/" class="mx-2">Home</v-btn>
      <!-- Guest Navigation -->
      <template v-if="!isAuthenticated">
      <v-btn variant="text" to="/login" class="mx-2">
            <v-icon start>mdi-login</v-icon>
            Login
          </v-btn>
          <v-btn variant="text" to="/register" class="mx-2">
            <v-icon start>mdi-account-plus</v-icon>
            Register
          </v-btn>
             <!-- Authenticated Navigation -->
          <v-btn variant="text" to="/dashboard" class="mx-2">
            <v-icon start>mdi-view-dashboard</v-icon>
            Dashboard
          </v-btn>

            <v-btn variant="text" to="/settings" class="mx-2">
              <v-icon start>mdi-cog</v-icon>
              Settings
            </v-btn>
          <v-btn variant="text" @click="logout" class="mx-2">
            <v-icon start>mdi-logout</v-icon>
            Logout
          </v-btn>
      </template>
    </v-app-bar>

<v-main>
        <router-view v-slot="{ Component }">
          <transition name="fade" mode="out-in">
            <component :is="Component" />
          </transition>
        </router-view>
      </v-main>
    </v-layout>
  </v-app>
</template>


<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>