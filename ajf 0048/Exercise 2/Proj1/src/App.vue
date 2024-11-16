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
      <router-view v-slot="{ Component }">
        <transition name="page" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </v-main>
  </v-app>
</template>

<script setup>
import { ref } from 'vue'
import NavBar from './components/NavBar.vue'

const drawer = ref(true)
</script>

<style scoped>
/* Fade transition */
.page-enter-active,
.page-leave-active {
  transition: all 0.4s ease;
}

.page-enter-from,
.page-leave-to {
  opacity: 0;
  transform: translateY(20px);
}

/* Slide transition */
.slide-enter-active,
.slide-leave-active {
  transition: all 0.4s ease;
}

.slide-enter-from {
  opacity: 0;
  transform: translateX(50px);
}

.slide-leave-to {
  opacity: 0;
  transform: translateX(-50px);
}
</style>