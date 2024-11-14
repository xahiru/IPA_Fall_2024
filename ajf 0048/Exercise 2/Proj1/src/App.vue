<template>
  <v-app>
    <!-- Mobile Header -->
    <v-app-bar
      v-if="$vuetify.display.smAndDown"
      color="primary"
      density="compact"
    >
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>Greenhouse Monitor</v-toolbar-title>
    </v-app-bar>

    <!-- Navigation Drawer -->
    <v-navigation-drawer v-model="drawer" permanent>
      <NavBar />
    </v-navigation-drawer>

    <!-- Main Content -->
    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script setup>
import { ref } from 'vue'
import NavBar from './components/NavBar.vue'

const drawer = ref(true)
</script>