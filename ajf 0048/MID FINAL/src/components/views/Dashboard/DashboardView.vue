<template>
  <v-container fluid class="dashboard-container">
    <AlertSystem ref="alertSystem" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    
    <v-row>
      <v-col cols="12" class="d-flex align-center justify-space-between">
        <h1 class="text-h4 mb-6">Greenhouse Dashboard</h1>
        <v-btn
          color="primary"
          @click="refreshData"
          :loading="isLoading"
          class="refresh-btn"
        >
          <v-icon left>mdi-refresh</v-icon>
          Refresh Data
        </v-btn>
      </v-col>
    </v-row>

    <nav class="dashboard-nav">
      <div class="nav-brand">
        <span class="brand-text">MyDashboard</span>
      </div>
      <div class="nav-links">
        <router-link to="/dashboard" class="nav-link" active-class="active">
          <i class="fas fa-chart-line"></i> Dashboard
        </router-link>
        <router-link to="/settings" class="nav-link" active-class="active">
  <i class="fas fa-cog"></i> Settings
</router-link>
      </div>
      <button @click="logout" class="logout-btn">
        <i class="fas fa-sign-out-alt"></i> Logout
      </button>
    </nav>

    <v-row>
      <v-col v-for="metric in metrics" :key="metric.id" cols="12" md="4">
        <MetricCards 
          v-bind="metric" 
          @threshold-exceeded="handleMetricAlert"
          class="slide-in" 
        />
      </v-col>
    </v-row>

    <v-row class="mt-6">
      <v-col cols="12">
        <MetricCharts class="elevation-chart" />
      </v-col>
    </v-row>

    <!-- Metric Details Dialog -->
    <v-dialog v-model="showDetailsDialog" max-width="600">
      <v-card>
        <v-card-title>{{ selectedMetric?.title }} Details</v-card-title>
        <v-card-text>
          <v-list>
            <v-list-item>
              <v-list-item-title>Current Value</v-list-item-title>
              <v-list-item-subtitle>{{ selectedMetric?.value }}</v-list-item-subtitle>
            </v-list-item>
            <v-list-item>
              <v-list-item-title>Trend</v-list-item-title>
              <v-list-item-subtitle>{{ selectedMetric?.trend }}%</v-list-item-subtitle>
            </v-list-item>
          </v-list>
        </v-card-text>
      </v-card>
    </v-dialog>


  </v-container>
</template>


<script setup>
import { ref } from 'vue'
import AlertSystem from '../../AlertSystem.vue';
import MetricCards from '../../MetricCards.vue'
import MetricCharts from '../../MetricCharts.vue'
import { onMounted, onUnmounted } from 'vue'
import { WebSocketService } from '../../../services/websocket'
import { useRouter } from 'vue-router'

const router = useRouter()
const alertSystem = ref(null)
const isLoading = ref(false)
const showDetailsDialog = ref(false)
const selectedMetric = ref(null)

const metrics = ref([
  {
    id: 1,
    title: 'Temperature',
    value: '24°C',
    icon: 'mdi-thermometer',
    iconColor: '#FC466B',
    trend: '+2.3',
    thresholds: { warning: 28, critical: 32 }
  },
  {
    id: 2,
    title: 'Humidity',
    value: '65%',
    icon: 'mdi-water',
    iconColor: '#00C9FF',
    trend: '-1.5',
    thresholds: { warning: 75, critical: 85 }
  },
  {
    id: 3,
    title: 'CO2 Levels',
    value: '450ppm',
    icon: 'mdi-molecule-co2',
    iconColor: '#92FE9D',
    trend: '+0.8',
    thresholds: { warning: 800, critical: 1000 }
  },
  {
    id: 4,
    title: 'Soil Moisture',
    value: '75%',
    icon: 'mdi-water-percent',
    iconColor: '#8B4513',
    trend: '-2.1',
    thresholds: { warning: 30, critical: 20 }
  },
  {
    id: 5,
    title: 'Air Quality',
    value: '95/100',
    icon: 'mdi-air-filter',
    iconColor: '#98FB98',
    trend: '+1.7',
    thresholds: { warning: 60, critical: 40 }
  },
  {
    id: 6,
    title: 'Light Intensity',
    value: '850 lux',
    icon: 'mdi-white-balance-sunny',
    iconColor: '#FFD700',
    trend: '+4.2',
    thresholds: { warning: 1000, critical: 1200 }
  },
])

const handleMetricAlert = (metric) => {
  alertSystem.value?.addAlert({
    type: metric.severity,
    title: `${metric.title} Alert`,
    message: metric.message,
    actions: [
      {
        label: 'Adjust Settings',
        color: 'primary',
        handler: () => adjustMetricSettings(metric),
        dismissOnAction: true
      },
      {
        label: 'View Details',
        color: 'secondary',
        handler: () => showMetricDetails(metric)
      }
    ]
  })
}

const refreshData = async () => {
  isLoading.value = true
  setTimeout(() => {
    metrics.value = metrics.value.map(metric => ({
      ...metric,
      value: updateValue(metric.value),
      trend: updateTrend()
    }))
    isLoading.value = false
  }, 1000)
}

const updateValue = (currentValue) => {
  const num = parseFloat(currentValue)
  const variation = (Math.random() - 0.5) * 2
  return `${(num + variation).toFixed(1)}${currentValue.replace(/[\d.]/g, '')}`
}

const updateTrend = () => {
  return (Math.random() * 5 - 2.5).toFixed(1)
}

const adjustMetricSettings = (metric) => {
  console.log(`Adjusting settings for ${metric.title}`)
}

const showMetricDetails = (metric) => {
  selectedMetric.value = metric
  showDetailsDialog.value = true
}
const wsService = new WebSocketService()

onMounted(() => {
  wsService.connect()
  
  metrics.value.forEach(metric => {
    wsService.subscribe(metric.title.toLowerCase(), (value) => {
      updateMetricValue(metric.id, value)
    })
  })
})

const updateMetricValue = (id, newValue) => {
  const metric = metrics.value.find(m => m.id === id)
  if (metric) {
    const oldValue = parseFloat(metric.value)
    metric.value = `${newValue}${metric.value.replace(/[\d.]/g, '')}`
    metric.trend = ((newValue - oldValue) / oldValue * 100).toFixed(1)
    checkThresholds(metric)
  }

}

const checkThresholds = (metric) => {
  const value = parseFloat(metric.value)
  if (value >= metric.thresholds.critical) {
    handleMetricAlert({
      ...metric,
      severity: 'error',
      message: `${metric.title} has reached critical level: ${metric.value}`
    })
  } else if (value >= metric.thresholds.warning) {
    handleMetricAlert({
      ...metric,
      severity: 'warning',
      message: `${metric.title} is approaching warning level: ${metric.value}`
    })
  }
}
</script>

<style scoped>
.dashboard-container {
  padding: 24px;
  background: var(--gradient-primary);
}

.elevation-chart {
  animation: slideUp 0.6s ease-out;
}

.slide-in {
  animation: slideIn 0.6s ease-out;
}

.refresh-btn {
  transition: transform 0.3s ease;
}

.refresh-btn:hover {
  transform: scale(1.05);
}

@keyframes slideUp {
  from { transform: translateY(30px); opacity: 0; }
  to { transform: translateY(0); opacity: 1; }
}

@keyframes slideIn {
  from { transform: translateX(30px); opacity: 0; }
  to { transform: translateX(0); opacity: 1; }
}

.text-h4 {
  background: linear-gradient(45deg, #FC466B, #3F5EFB);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  font-weight: bold;
}

.dashboard-nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background: linear-gradient(to right, #1a1a2e, #16213e);
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.nav-brand {
  font-size: 1.5rem;
  font-weight: bold;
  color: white;
}

.nav-links {
  display: flex;
  gap: 2rem;
}

.nav-link {
  color: white;
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.nav-link:hover {
  background-color: rgba(255, 255, 255, 0.1);
  transform: translateY(-2px);
}

.nav-link.active {
  background-color: rgba(255, 255, 255, 0.2);
  font-weight: bold;
}

.logout-btn {
  background-color: #ff4757;
  color: white;
  border: none;
  padding: 0.5rem 1.5rem;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 1rem;
}

.logout-btn:hover {
  background-color: #ff6b81;
  transform: translateY(-2px);
}

/* Add smooth hover transitions */
* {
  transition: all 0.3s ease;
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .nav-links {
    gap: 1rem;
  }
  
  .nav-link, .logout-btn {
    padding: 0.4rem 0.8rem;
  }
}
</style>