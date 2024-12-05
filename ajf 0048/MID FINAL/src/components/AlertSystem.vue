<template>
    <div class="alert-system">
      <!-- Status Overview Panel -->
      <v-card class="status-panel mb-4" v-if="hasActiveAlerts">
        <v-card-title class="d-flex align-center">
          System Status
          <v-spacer></v-spacer>
          <v-chip
            :color="systemStatusColor"
            class="status-chip"
          >
            {{ systemStatus }}
          </v-chip>
        </v-card-title>
      </v-card>
  
      <!-- Dynamic Alerts -->
      <TransitionGroup name="alert-transition">
        <v-alert
          v-for="alert in activeAlerts"
          :key="alert.id"
          :type="alert.type"
          :title="alert.title"
          class="alert-item mb-2"
          variant="tonal"
          closable
          @click:close="dismissAlert(alert.id)"
        >
          <div class="alert-content">
            <span>{{ alert.message }}</span>
            <div class="alert-actions" v-if="alert.actions">
              <v-btn
                v-for="action in alert.actions"
                :key="action.label"
                :color="action.color || 'primary'"
                size="small"
                @click="handleAction(action, alert)"
              >
                {{ action.label }}
              </v-btn>
            </div>
          </div>
        </v-alert>
      </TransitionGroup>
    </div>
  </template>
  
  <script setup>
  import { ref, computed } from 'vue'
  
  const activeAlerts = ref([])
  const systemStatus = ref('Normal')
  
  const hasActiveAlerts = computed(() => activeAlerts.value.length > 0)
  const systemStatusColor = computed(() => {
    switch(systemStatus.value) {
      case 'Critical': return 'error'
      case 'Warning': return 'warning'
      default: return 'success'
    }
  })
  
  const addAlert = (alert) => {
    const newAlert = {
      id: Date.now(),
      timestamp: new Date(),
      ...alert
    }
    activeAlerts.value.push(newAlert)
  
    if (alert.timeout !== false) {
      setTimeout(() => dismissAlert(newAlert.id), alert.timeout || 5000)
    }
  
    updateSystemStatus()
  }
  
  const dismissAlert = (id) => {
    activeAlerts.value = activeAlerts.value.filter(alert => alert.id !== id)
    updateSystemStatus()
  }
  
  const handleAction = (action, alert) => {
    if (action.handler) {
      action.handler(alert)
    }
    if (action.dismissOnAction) {
      dismissAlert(alert.id)
    }
  }
  
  const updateSystemStatus = () => {
    const criticalAlerts = activeAlerts.value.filter(alert => alert.type === 'error')
    const warningAlerts = activeAlerts.value.filter(alert => alert.type === 'warning')
  
    if (criticalAlerts.length > 0) {
      systemStatus.value = 'Critical'
    } else if (warningAlerts.length > 0) {
      systemStatus.value = 'Warning'
    } else {
      systemStatus.value = 'Normal'
    }
  }
  
  defineExpose({
    addAlert,
    dismissAlert
  })
  </script>
  
  <style scoped>
  .alert-system {
    position: fixed;
    top: 20px;
    right: 20px;
    z-index: 1000;
    max-width: 400px;
  }
  
  .status-panel {
    background: rgba(255, 255, 255, 0.9);
    backdrop-filter: blur(10px);
    border-radius: 8px;
  }
  
  .status-chip {
    font-weight: 600;
  }
  
  .alert-item {
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(8px);
    border-radius: 8px;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
  }
  
  .alert-content {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }
  
  .alert-actions {
    display: flex;
    gap: 8px;
    margin-top: 8px;
  }
  
  .alert-transition-enter-active,
  .alert-transition-leave-active {
    transition: all 0.3s ease;
  }
  
  .alert-transition-enter-from,
  .alert-transition-leave-to {
    opacity: 0;
    transform: translateX(30px);
  }
  </style>