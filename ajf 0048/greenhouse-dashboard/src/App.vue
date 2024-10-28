<template>
  <v-app>
    <v-layout>
    <v-app-bar app color="primary">
      <v-app-bar-title>Greenhouse Dashboard</v-app-bar-title>
      <v-spacer></v-spacer>
      <v-btn variant="text" to="/">Home</v-btn>
      <v-btn variant="text" to="/dashboard">Dashboard</v-btn>
      <v-btn variant="text" to="/settings">Settings</v-btn>
    </v-app-bar>

    <v-main>
      <router-view></router-view>
    </v-main>
  </v-layout>
 </v-app>
</template>

<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()
</script>