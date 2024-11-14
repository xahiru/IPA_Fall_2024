<template>
    <Line :data="chartData" :options="chartOptions" />
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
  
  const chartData = ref({
    labels: [],
    datasets: [
      {
        label: 'Temperature (°C)',
        borderColor: '#F44336',
        backgroundColor: 'rgba(244, 67, 54, 0.1)',
        fill: true,
        tension: 0.4,
        data: []
      },
      {
        label: 'Humidity (%)',
        borderColor: '#2196F3',
        backgroundColor: 'rgba(33, 150, 243, 0.1)',
        fill: true,
        tension: 0.4,
        data: []
      }
    ]
  })
  
  const chartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: 'top'
      },
      tooltip: {
        mode: 'index',
        intersect: false
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
          display: false
        }
      }
    },
    interaction: {
      intersect: false,
      mode: 'index'
    }
  }
  
  onMounted(() => {
    updateChartData()
    setInterval(updateChartData, 5000)
  })
  
  function updateChartData() {
    const currentTime = new Date().toLocaleTimeString()
    chartData.value.labels.push(currentTime)
    chartData.value.datasets[0].data.push(Math.random() * (30 - 20) + 20)
    chartData.value.datasets[1].data.push(Math.random() * (80 - 40) + 40)
  
    if (chartData.value.labels.length > 10) {
      chartData.value.labels.shift()
      chartData.value.datasets.forEach(dataset => dataset.data.shift())
    }
  }
  </script>