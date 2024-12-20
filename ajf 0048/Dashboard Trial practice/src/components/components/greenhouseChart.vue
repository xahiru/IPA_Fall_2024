<template>
    <v-card elevation="2" class="pa-4">
      <v-card-title class="d-flex align-center">
        <v-icon color="primary" class="mr-2">mdi-chart-line</v-icon>
        Greenhouse Metrics
        <v-spacer></v-spacer>
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
  
      <v-card-text>
        <v-row>
          <v-col cols="12" md="3">
            <v-checkbox
              v-for="dataset in datasets"
              :key="dataset.id"
              v-model="dataset.visible"
              :label="dataset.label"
              :color="dataset.color"
              hide-details
            ></v-checkbox>
          </v-col>
          <v-col cols="12" md="9">
            <div style="height: 400px">
              <Line 
                :data="chartData" 
                :options="chartOptions" 
                @click="handleChartClick"
              />
            </div>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>
  </template>
  
  <script setup>
  import { ref, computed, onMounted, watch } from 'vue'
  import { Line } from 'vue-chartjs'
  import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
    Filler
  } from 'chart.js'
  
  ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
    Filler
  )
  
  const selectedPeriod = ref('1h')
  const timePeriods = [
    { label: '1H', value: '1h' },
    { label: '24H', value: '24h' },
    { label: '7D', value: '7d' },
  ]
  
  const datasets = ref([
    {
      id: 'temp',
      label: 'Temperature (°C)',
      color: '#F44336',
      visible: true,
      data: []
    },
    {
      id: 'humidity',
      label: 'Humidity (%)',
      color: '#2196F3',
      visible: true,
      data: []
    },
    {
      id: 'soil',
      label: 'Soil Moisture (%)',
      color: '#4CAF50',
      visible: true,
      data: []
    },
    {
      id: 'light',
      label: 'Light (lux)',
      color: '#FFC107',
      visible: true,
      data: []
    }
  ])
  
  const chartData = computed(() => ({
    labels: generateTimeLabels(),
    datasets: datasets.value
      .filter(d => d.visible)
      .map(dataset => ({
        label: dataset.label,
        borderColor: dataset.color,
        backgroundColor: `${dataset.color}20`,
        borderWidth: 2,
        fill: true,
        tension: 0.4,
        data: dataset.data,
        pointRadius: 0,
        pointHitRadius: 20,
      }))
  }))
  
  const chartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    interaction: {
      intersect: false,
      mode: 'index'
    },
    plugins: {
      legend: {
        display: false
      },
      tooltip: {
        backgroundColor: 'rgba(255, 255, 255, 0.9)',
        titleColor: '#000',
        bodyColor: '#000',
        borderColor: '#ddd',
        borderWidth: 1,
        padding: 12,
        displayColors: true
      }
    },
    scales: {
      x: {
        grid: {
          display: false
        }
      },
      y: {
        grid: {
          color: '#eee'
        }
      }
    }
  }
  
  function generateTimeLabels() {
    const now = new Date()
    const labels = []
    const intervals = {
      '1h': { count: 60, unit: 'minute' },
      '24h': { count: 24, unit: 'hour' },
      '7d': { count: 7, unit: 'day' }
    }
    
    const { count, unit } = intervals[selectedPeriod.value]
    for (let i = count - 1; i >= 0; i--) {
      const date = new Date(now)
      if (unit === 'minute') date.setMinutes(date.getMinutes() - i)
      if (unit === 'hour') date.setHours(date.getHours() - i)
      if (unit === 'day') date.setDate(date.getDate() - i)
      labels.push(date.toLocaleTimeString())
    }
    return labels
  }
  
  function generateRandomData(min, max, count) {
    return Array.from({ length: count }, () => 
      Math.random() * (max - min) + min
    )
  }
  
  function updateDatasets() {
    const dataPoints = {
      '1h': 60,
      '24h': 24,
      '7d': 7
    }
    
    datasets.value.forEach(dataset => {
      const count = dataPoints[selectedPeriod.value]
      switch(dataset.id) {
        case 'temp':
          dataset.data = generateRandomData(20, 30, count)
          break
        case 'humidity':
          dataset.data = generateRandomData(40, 80, count)
          break
        case 'soil':
          dataset.data = generateRandomData(30, 70, count)
          break
        case 'light':
          dataset.data = generateRandomData(500, 2000, count)
          break
      }
    })
  }
  
  function changePeriod(period) {
    selectedPeriod.value = period
    updateDatasets()
  }
  
  function handleChartClick(event) {
    const points = event.chart.getElementsAtEventForMode(
      event,
      'index',
      { intersect: false },
      true
    )
    if (points.length) {
      const point = points[0]
      console.log('Clicked data:', {
        label: chartData.value.labels[point.index],
        value: chartData.value.datasets[point.datasetIndex].data[point.index]
      })
    }
  }
  
  watch(datasets, () => {
    updateDatasets()
  }, { deep: true })
  
  onMounted(() => {
    updateDatasets()
    setInterval(() => {
      if (selectedPeriod.value === '1h') {
        updateDatasets()
      }
    }, 5000)
  })
  </script>