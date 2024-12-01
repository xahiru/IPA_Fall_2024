<template>
    <v-list class="nav-list">
      <v-list-item
       prepend-avatar="https://randomuser.me/api/portraits/women/79.jpg"
      title="RITAH"
      subtitle="Greenhouse Admin"
    ></v-list-item>
      <v-list-item
      v-for="item in menuItems"
      :key="item.title"
      :to="item.path"
      class="nav-item"
      v-ripple
    >
    <v-icon class="nav-icon">{{ item.icon }}</v-icon>
      <span class="nav-text">{{ item.title }}</span>
    </v-list-item>

    <v-divider></v-divider>

    <v-divider class="mt-auto"></v-divider>
    
    <v-list-item
      prepend-icon="mdi-logout"
      title="Logout"
      @click="handleLogout"
      class="logout-item"
    ></v-list-item>
  </v-list>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()


const menuItems = [
{ title: 'Home', icon: 'mdi-home', path: '/' },
  { title: 'Dashboard', icon: 'mdi-view-dashboard', path: '/dashboard' },
  { title: 'Settings', icon: 'mdi-cog', path: '/settings' },
  { title: 'Login', icon: 'mdi-login', path: '/login' },
  { title: 'Register', icon: 'mdi-account-plus', path: '/register' }
]

const handleLogout = () => {
  router.push('/login')
}
</script>

<style scoped>
.nav-background {
  height: 100%;
  background: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(10px);
}

.profile-item {
  color: white;
  margin-bottom: 10px;
}

.profile-section {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 16px;
  margin: 16px 8px;
  padding: 16px;
}

.v-list-item {
  margin: 8px;
  border-radius: 12px;
  color: white !important;
  transition: all 0.3s ease;
}

.v-list-item:hover {
  background: linear-gradient(45deg, #00C9FF, #92FE9D) !important;
  transform: translateX(5px);
}

.active {
  background: linear-gradient(45deg, #FC466B, #3F5EFB) !important;
}

.divider {
  border-color: rgba(255, 255, 255, 0.1);
}

.nav-item {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.nav-icon {
  transition: transform 0.3s ease;
}

.nav-item:hover .nav-icon {
  transform: translateX(5px) rotate(5deg);
}

.nav-text {
  position: relative;
  overflow: hidden;
}

.nav-text::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background: linear-gradient(90deg, #00C9FF, #92FE9D);
  transform: translateX(-100%);
  transition: transform 0.3s ease;
}

.nav-item:hover .nav-text::after {
  transform: translateX(0);
}
</style>