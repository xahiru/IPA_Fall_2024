<template>
    <v-list>
    <v-list-item
      prepend-avatar="https://randomuser.me/api/portraits/men/78.jpg"
      title="Jane Frances"
      subtitle="Greenhouse Admin"
    ></v-list-item>

    <v-divider></v-divider>

    <v-list density="compact" nav>
      <v-list-item
        v-for="item in menuItems"
        :key="item.title"
        :to="item.path"
        :prepend-icon="item.icon"
        :title="item.title"
        rounded="lg"
      ></v-list-item>
    </v-list>
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
.nav-container {
  height: 100%;
  display: flex;
  flex-direction: column;
}
</style>