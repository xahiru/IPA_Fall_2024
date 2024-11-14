<template>
    <v-card elevation="2" class="mb-6">
      <v-card-title class="d-flex align-center">
        <v-icon color="primary" class="mr-2">mdi-controller</v-icon>
        Greenhouse Controls
      </v-card-title>
      
      <v-card-text>
        <v-row>
          <v-col cols="12" md="6">
            <v-card class="control-card">
              <v-switch
                v-model="controls.ventilation"
                color="success"
                :loading="loading.ventilation"
                @change="handleVentilation"
              >
                <template v-slot:label>
                  <div class="d-flex align-center">
                    <v-icon :color="controls.ventilation ? 'success' : 'grey'" class="mr-2">
                      mdi-fan
                    </v-icon>
                    Ventilation System
                  </div>
                </template>
              </v-switch>
            </v-card>
          </v-col>
  
          <v-col cols="12" md="6">
            <v-card class="control-card">
              <v-switch
                v-model="controls.irrigation"
                color="info"
                :loading="loading.irrigation"
                @change="handleIrrigation"
              >
                <template v-slot:label>
                  <div class="d-flex align-center">
                    <v-icon :color="controls.irrigation ? 'info' : 'grey'" class="mr-2">
                      mdi-water-pump
                    </v-icon>
                    Irrigation System
                  </div>
                </template>
              </v-switch>
            </v-card>
          </v-col>
  
          <v-col cols="12" md="6">
            <v-card class="control-card">
              <v-switch
                v-model="controls.lighting"
                color="warning"
                :loading="loading.lighting"
                @change="handleLighting"
              >
                <template v-slot:label>
                  <div class="d-flex align-center">
                    <v-icon :color="controls.lighting ? 'warning' : 'grey'" class="mr-2">
                      mdi-lightbulb-group
                    </v-icon>
                    Lighting System
                  </div>
                </template>
              </v-switch>
            </v-card>
          </v-col>
  
          <v-col cols="12" md="6">
            <v-card class="control-card">
              <v-switch
                v-model="controls.autoMode"
                color="primary"
                :loading="loading.autoMode"
                @change="handleAutoMode"
              >
                <template v-slot:label>
                  <div class="d-flex align-center">
                    <v-icon :color="controls.autoMode ? 'primary' : 'grey'" class="mr-2">
                      mdi-robot
                    </v-icon>
                    Automatic Mode
                  </div>
                </template>
              </v-switch>
            </v-card>
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
  
  const loading = ref({
    ventilation: false,
    irrigation: false,
    lighting: false,
    autoMode: false
  })
  
  const handleVentilation = async () => {
    loading.value.ventilation = true
    await new Promise(resolve => setTimeout(resolve, 1000))
    loading.value.ventilation = false
  }
  
  const handleIrrigation = async () => {
    loading.value.irrigation = true
    await new Promise(resolve => setTimeout(resolve, 1000))
    loading.value.irrigation = false
  }
  
  const handleLighting = async () => {
    loading.value.lighting = true
    await new Promise(resolve => setTimeout(resolve, 1000))
    loading.value.lighting = false
  }
  
  const handleAutoMode = async () => {
    loading.value.autoMode = true
    await new Promise(resolve => setTimeout(resolve, 1000))
    loading.value.autoMode = false
  }
  </script>
  
  <style scoped>
  .control-card {
    padding: 16px;
    transition: all 0.3s ease;
  }
  
  .control-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  }
  </style>