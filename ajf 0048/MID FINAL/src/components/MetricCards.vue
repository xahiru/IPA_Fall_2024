<template>
    <v-card class="metric-card" :class="{ 'pulse': isUpdating }" elevation="10">
      <v-card-text>
        <div class="d-flex align-center justify-space-between">
          <div class="metric-title">{{ title }}</div>
          <v-icon :color="iconColor" class="floating-icon" size="32">{{ icon }}</v-icon>
        </div>
        <div class="metric-value">{{ value }}</div>
        <div class="metric-trend">
          <v-icon :color="getTrendColor" size="small">
            {{ Number(trend) > 0 ? 'mdi-arrow-up' : 'mdi-arrow-down' }}
          </v-icon>
          <span :class="getTrendColor">{{ trend }}%</span>
        </div>
      </v-card-text>
    </v-card>
  </template>
  
  <script setup>
  import { computed } from 'vue'
  
  const props = defineProps({
    title: String,
    value: String,
    icon: String,
    iconColor: String,
    trend: String,
    isUpdating: Boolean
  })
  
  const getTrendColor = computed(() => {
    const value = Number(props.trend)
    if (value > 0) return 'success'
    return 'error'
  })
  </script>
  
  <style scoped>
  .metric-card {
    background: rgba(255, 255, 255, 0.8) !important;
    backdrop-filter: blur(12px);
    border-radius: 16px;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    cursor: pointer;
  }
  
  .metric-card:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 20px 40px rgba(31, 38, 135, 0.15);
  }
  
  .floating-icon {
    animation: float 3s ease-in-out infinite;
  }
  
  .metric-value {
    font-size: 2.5rem;
    font-weight: bold;
    background: linear-gradient(45deg, #FC466B, #3F5EFB);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 10px 0;
  }
  
  .metric-title {
    font-size: 1.1rem;
    color: #1A1A1A;
    font-weight: 500;
  }
  
  .metric-trend {
    display: flex;
    align-items: center;
    gap: 4px;
    font-size: 0.9rem;
  }
  
  .success {
    color: #00C9FF;
  }
  
  .error {
    color: #FC466B;
  }
  
  @keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
    100% { transform: translateY(0px); }
  }
  
  .pulse {
    animation: pulse 2s infinite;
  }
  
  @keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.05); }
    100% { transform: scale(1); }
  }
  </style>