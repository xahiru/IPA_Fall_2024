<template>
    <v-navigation-drawer
    v-model="drawer"
    :permanent="$vuetify.display.mdAndUp"
    :temporary="$vuetify.display.smAndDown"
    >
      <v-list-item
        prepend-avatar="https://randomuser.me/api/portraits/men/78.jpg"
        title="Greenhouse Admin"
      ></v-list-item>
  
      <v-divider></v-divider>
  
      <v-list density="compact" nav>
        
       <v-list-item
        v-for="item in menuItems"
        :key="item.path"
        :to="item.path"
        :prepend-icon="item.icon"
        :title="item.title"
      ></v-list-item>
      </v-list>
    </v-navigation-drawer>

 <!-- Mobile Header -->
 <v-app-bar v-if="$vuetify.display.smAndDown">
    <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
    <v-toolbar-title>Greenhouse Monitor</v-toolbar-title>
  </v-app-bar>
  </template>

<script setup>
import { ref } from 'vue'

const drawer = ref(true)
const menuItems = [
  { title: 'Dashboard', icon: 'mdi-view-dashboard', path: '/dashboard' },
  { title: 'Settings', icon: 'mdi-cog', path: '/settings' }
]
</script>