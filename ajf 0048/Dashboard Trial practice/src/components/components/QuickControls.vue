<template>
    <v-card elevation="2" class="pa-4">
      <v-card-title class="d-flex align-center">
        <v-icon color="primary" class="mr-2">mdi-controller</v-icon>
        Quick Controls
      </v-card-title>
      <v-card-text>
        <v-row>
          <v-col cols="6" md="3">
            <v-switch
              v-model="controls.ventilation"
              label="Ventilation"
              color="success"
            ></v-switch>
          </v-col>
          <v-col cols="6" md="3">
            <v-switch
              v-model="controls.irrigation"
              label="Irrigation"
              color="info"
            ></v-switch>
          </v-col>
          <v-col cols="6" md="3">
            <v-switch
              v-model="controls.lighting"
              label="Lighting"
              color="warning"
            ></v-switch>
          </v-col>
          <v-col cols="6" md="3">
            <v-switch
              v-model="controls.autoMode"
              label="Auto Mode"
              color="primary"
            ></v-switch>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  
  const controls = ref({
    ventilation: false,
    irrigation: false,
    lighting: true,
    autoMode: true
  })
  </script>