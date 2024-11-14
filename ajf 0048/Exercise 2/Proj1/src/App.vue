<template>
  <v-app>
    <NavBar  v-if="showNav"/>
    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import NavBar from './components/NavBar.vue'

const route = useRoute()
const showNav = computed(() => {
  return !['/', '/login', '/register'].includes(route.path)
})
</script>