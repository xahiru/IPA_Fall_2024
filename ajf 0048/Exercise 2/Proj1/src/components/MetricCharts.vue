<template>
    <v-card class="mt-6">
      <v-card-title>Temperature History</v-card-title>
      <v-card-text style="height: 300px">
        <Line :data="chartData" :options="chartOptions" />
      </v-card-text>
    </v-card>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
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
  
  const chartData = ref({
    labels: [],
    datasets: [{
      label: 'Temperature °C',
      data: [],
      borderColor: 'rgb(255, 99, 132)',
      tension: 0.1
    }]
  })
  
  const chartOptions = {
    responsive: true,
    maintainAspectRatio: false
  }
  
  onMounted(() => {
    updateChart()
  })
  
  const updateChart = () => {
    const times = []
    const temperatures = []
    for (let i = 0; i < 12; i++) {
      const time = new Date()
      time.setMinutes(time.getMinutes() - i * 5)
      times.unshift(time.toLocaleTimeString())
      temperatures.unshift(Math.random() * (30 - 20) + 20)
    }
    
    chartData.value.labels = times
    chartData.value.datasets[0].data = temperatures
  }
  </script>