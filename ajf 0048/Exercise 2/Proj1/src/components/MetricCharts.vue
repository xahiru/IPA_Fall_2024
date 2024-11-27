<template>
  <v-card class="chart-card">
    <v-card-title class="d-flex justify-space-between align-center">
      Environmental Metrics
      <v-btn-toggle v-model="timeRange" mandatory class="time-range-toggle">
        <v-btn value="1h">1H</v-btn>
        <v-btn value="24h">24H</v-btn>
        <v-btn value="7d">7D</v-btn>
      </v-btn-toggle>
    </v-card-title>
    
    <v-card-text>
      <div class="alerts-banner" v-if="activeAlerts.length">
        <v-alert
          v-for="alert in activeAlerts"
          :key="alert.id"
          :type="alert.type"
          :title="alert.title"
          class="ma-2"
          variant="tonal"
        >
          {{ alert.message }}
        </v-alert>
      </div>
      <Line :data="chartData" :options="chartOptions" height="300" />
    </v-card-text>
  </v-card>
</template>

<script setup>
import { ref, watch } from 'vue'
import { Line } from 'vue-chartjs'
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js'

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
)

const timeRange = ref('24h')
const activeAlerts = ref([])

const generateChartData = (range) => {
  const dataPoints = {
    '1h': 60,
    '24h': 24,
    '7d': 7
  }

  const points = dataPoints[range]
  const labels = Array.from({ length: points }, (_, i) => {
    switch(range) {
      case '1h': return `${i}m`
      case '24h': return `${i}h`
      case '7d': return `Day ${i + 1}`
    }
  })

  return {
    labels,
    datasets: [
      {
        label: 'Temperature °C',
        data: Array.from({ length: points }, () => Math.random() * 30 + 15),
        borderColor: '#FC466B',
        backgroundColor: 'rgba(252, 70, 107, 0.2)',
        tension: 0.4
      },
      {
        label: 'Humidity %',
        data: Array.from({ length: points }, () => Math.random() * 40 + 40),
        borderColor: '#00C9FF',
        backgroundColor: 'rgba(0, 201, 255, 0.2)',
        tension: 0.4
      }
    ]
  }
}

const chartData = ref(generateChartData('24h'))

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  interaction: {
    mode: 'index',
    intersect: false,
  },
  animation: {
    duration: 750,
    easing: 'easeInOutQuart'
  },
  plugins: {
    legend: {
      position: 'top',
      labels: {
        usePointStyle: true,
        pointStyle: 'circle',
        font: {
          weight: 600
        }
      }
    },
    tooltip: {
      backgroundColor: 'rgba(255, 255, 255, 0.9)',
      titleColor: '#1A1A1A',
      bodyColor: '#1A1A1A',
      borderColor: 'rgba(0, 0, 0, 0.1)',
      borderWidth: 1,
      padding: 12,
      cornerRadius: 8
    }
  },
  scales: {
    y: {
      beginAtZero: true,
      grid: {
        color: 'rgba(0, 0, 0, 0.1)'
      }
    },
    x: {
      grid: {
        color: 'rgba(0, 0, 0, 0.1)'
      }
    }
  }
}

watch(timeRange, (newRange) => {
  chartData.value = generateChartData(newRange)
})
</script>

<style scoped>
.chart-card {
  background: rgba(255, 255, 255, 0.8) !important;
  backdrop-filter: blur(12px);
  border-radius: 16px;
  transition: all 0.3s ease;
}

.time-range-toggle {
  background: rgba(0, 0, 0, 0.05);
  border-radius: 8px;
  padding: 4px;
}

.alerts-banner {
  margin-bottom: 20px;
}

.v-alert {
  transition: all 0.3s ease;
}

.v-alert:hover {
  transform: translateX(5px);
}
</style>