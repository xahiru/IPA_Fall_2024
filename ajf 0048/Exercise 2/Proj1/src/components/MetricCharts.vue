<template>
    <v-card class="mt-6">
      <v-card-title class="d-flex align-center justify-space-between">
        <span>Environmental History</span>
        <v-btn-group>
          <v-btn
            v-for="period in timePeriods"
            :key="period.value"
            :color="selectedPeriod === period.value ? 'primary' : undefined"
            @click="changePeriod(period.value)"
            size="small"
          >
            {{ period.label }}
          </v-btn>
        </v-btn-group>
      </v-card-title>
      
      <v-card-text style="height: 400px">
        <Line 
          :data="chartData" 
          :options="chartOptions" 
          @click="handleChartClick"
        />
      </v-card-text>
    </v-card>
  </template>
  
  <script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { Line } from 'vue-chartjs'
import api from '../services/api';
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

const selectedPeriod = ref('24h')
const timePeriods = [
  { label: '24H', value: '24h' },
  { label: '7D', value: '7d' },
  { label: '30D', value: '30d' }
]

const chartData = ref({
  labels: [],
  datasets: [
    {
      label: 'Temperature °C',
      data: [],
      borderColor: 'rgb(255, 99, 132)',
      tension: 0.1
    },
    {
      label: 'Humidity %',
      data: [],
      borderColor: 'rgb(54, 162, 235)',
      tension: 0.1
    }
  ]
})

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  interaction: {
    intersect: false,
    mode: 'index'
  },
  plugins: {
    legend: {
      position: 'top',
      labels: {
        usePointStyle: true
      }
    },
    tooltip: {
      backgroundColor: 'rgba(255, 255, 255, 0.9)',
      titleColor: '#000',
      bodyColor: '#000',
      borderColor: '#ddd',
      borderWidth: 1,
      padding: 10,
      displayColors: true
    },
    zoom: {
      zoom: {
        wheel: {
          enabled: true
        },
        pinch: {
          enabled: true
        },
        mode: 'xy'
      },
      pan: {
        enabled: true
      }
    }
  },
  scales: {
    y: {
      beginAtZero: false,
      grid: {
        drawBorder: false
      }
    },
    x: {
      grid: {
        display: false
      }
    }
  }
}

// Add click handler
const handleChartClick = (event, elements) => {
  if (elements.length > 0) {
    const dataIndex = elements[0].index
    console.log('Clicked data point:', {
      time: chartData.value.labels[dataIndex],
      temperature: chartData.value.datasets[0].data[dataIndex],
      humidity: chartData.value.datasets[1].data[dataIndex]
    })
  }
}

let updateInterval

const changePeriod = (period) => {
  selectedPeriod.value = period
  updateChart()
}

const updateChart = () => {
  const times = []
  const temperatures = []
  const humidities = []
  
  const dataPoints = selectedPeriod.value === '24h' ? 24 : 
                    selectedPeriod.value === '7d' ? 7 : 30
                    
  for (let i = 0; i < dataPoints; i++) {
    const time = new Date()
    if (selectedPeriod.value === '24h') {
      time.setHours(time.getHours() - i)
      times.unshift(time.toLocaleTimeString())
    } else {
      time.setDate(time.getDate() - i)
      times.unshift(time.toLocaleDateString())
    }
    temperatures.unshift(Math.random() * (30 - 20) + 20)
    humidities.unshift(Math.random() * (80 - 40) + 40)
  }
  
  chartData.value.labels = times
  chartData.value.datasets[0].data = temperatures
  chartData.value.datasets[1].data = humidities
}
const fetchHistoricalData = async () => {
  const data = await api.getMetrics()
  chartData.value.datasets[0].data.push(data.temperature)
  chartData.value.datasets[1].data.push(data.humidity)
  
  // Keep only last N points based on selected period
  const maxPoints = selectedPeriod.value === '24h' ? 24 : 
                   selectedPeriod.value === '7d' ? 7 : 30
                   
  if (chartData.value.datasets[0].data.length > maxPoints) {
    chartData.value.datasets[0].data.shift()
    chartData.value.datasets[1].data.shift()
    chartData.value.labels.shift()
  }
}

onMounted(() => {
  updateChart()
  updateInterval = setInterval(fetchHistoricalData, 5000)
})
onUnmounted(() => {
  if (updateInterval) clearInterval(updateInterval)
})
</script>