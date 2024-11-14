<template>
  <v-container fluid>
    <!-- Control Panel -->
    <v-row>
      <v-col cols="12">
        <v-card class="mb-6">
          <v-card-text>
            <v-switch
              v-model="autoRefresh"
              label="Auto Refresh Data"
              color="primary"
               density="compact"
            ></v-switch>
            <v-select
              v-model="refreshInterval"
              :items="refreshOptions"
              label="Refresh Interval"
              :disabled="!autoRefresh"
            ></v-select>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <!-- Status Alert -->
    <v-row>
      <v-col cols="12">
        <v-alert
          v-if="isSystemActive"
          color="success"
          icon="mdi-check-circle"
        >
          System is running normally
        </v-alert>
      </v-col>
    </v-row>

    <!-- Metric Cards -->
    <v-row>
      <v-col 
        v-for="(metric, index) in metricsList" 
        :key="index"
        cols="12" 
        sm="6" 
        md="4"
        lg="4"
      >
        <v-card 
          :class="['metric-card', {'alert': isMetricInDanger(metric)}]"
          @click="showMetricDetails(metric)"
        >
          <v-card-text class="d-flex flex-column align-center pa-4">
            <v-icon 
              size="$vuetify.display.smAndDown ? 36 : 48"  
              :color="metric.color" 
              class="mb-2"
            >
              {{ metric.icon }}
            </v-icon>
            <div class="$vuetify.display.smAndDown ? 'text-h5' : 'text-h4' mb-2" >
              {{ metric.value }}
            </div>
            <div class="text-subtitle-1">{{ metric.label }}</div>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <v-row>
    <v-col cols="12" lg="8">
      <MetricsChart />
    </v-col>
  </v-row>

    <!-- Metric Details Dialog -->
    <v-dialog v-model="showDialog" max-width="500">
      <v-card v-if="selectedMetric">
        <v-card-title>{{ selectedMetric.label }} Details</v-card-title>
        <v-card-text>
          <v-list>
            <v-list-item>
              <v-list-item-title>Current Value</v-list-item-title>
              <v-list-item-subtitle>{{ selectedMetric.value }}</v-list-item-subtitle>
            </v-list-item>
            <v-list-item>
              <v-list-item-title>Status</v-list-item-title>
              <v-list-item-subtitle>
                <v-chip
                  :color="isMetricInDanger(selectedMetric) ? 'error' : 'success'"
                  small
                >
                  {{ isMetricInDanger(selectedMetric) ? 'Alert' : 'Normal' }}
                </v-chip>
              </v-list-item-subtitle>
            </v-list-item>
          </v-list>
        </v-card-text>
      </v-card>
    </v-dialog>

     <!-- Chart Section - Full width on mobile, responsive on larger screens -->
     <v-row>
      <v-col cols="12" lg="8">
        <MetricCharts />
      </v-col>
    </v-row>
  </v-container>
</template>


<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import MetricCharts from '../MetricCharts.vue';
import api from '../../services/api';

const metrics = ref({})
const isSystemActive = ref(true)
const autoRefresh = ref(true)
const refreshInterval = ref(5000)
const showDialog = ref(false)
const selectedMetric = ref(null)
let intervalId

const refreshOptions = [
  { title: '5 seconds', value: 5000 },
  { title: '10 seconds', value: 10000 },
  { title: '30 seconds', value: 30000 }
]

const metricsList = computed(() => [
  {
    label: 'Temperature',
    value: `${metrics.value.temperature?.toFixed(1)}°C`,
    icon: 'mdi-thermometer',
    color: 'error'
  },
  {
    label: 'Humidity',
    value: `${metrics.value.humidity?.toFixed(1)}%`,
    icon: 'mdi-water',
    color: 'blue'
  },
  {
    label: 'Soil Moisture',
    value: `${metrics.value.soilMoisture?.toFixed(1)}%`,
    icon: 'mdi-water-percent',
    color: 'brown'
  },
  {
    label: 'Light Level',
    value: `${metrics.value.lightLevel?.toFixed(0)} lux`,
    icon: 'mdi-white-balance-sunny',
    color: 'orange'
  },
  {
    label: 'CO2 Level',
    value: `${metrics.value.co2Level?.toFixed(0)} ppm`,
    icon: 'mdi-molecule-co2',
    color: 'grey-darken-1'
  },
  {
    label: 'Nutrient Level',
    value: `${metrics.value.nutrientLevel?.toFixed(1)}%`,
    icon: 'mdi-leaf',
    color: 'green'
  }
])

const fetchMetrics = async () => {
  const data = await api.getMetrics()
  metrics.value = data
}

const showMetricDetails = (metric) => {
  selectedMetric.value = metric
  showDialog.value = true
}

const isMetricInDanger = (metric) => {
  if (!metric) return false
  const thresholds = {
    Temperature: 30,
    Humidity: 80,
    'Soil Moisture': 20
  }
  return thresholds[metric.label] && parseFloat(metric.value) > thresholds[metric.label]
}

onMounted(() => {
  fetchMetrics()
  intervalId = setInterval(fetchMetrics, refreshInterval.value)
})

onUnmounted(() => {
  if (intervalId) clearInterval(intervalId)
})
</script>

<style scoped>
.metric-card {
  transition: all 0.3s ease;
  cursor: pointer;
}

.metric-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}

.alert {
  border: 2px solid red;
}
</style>