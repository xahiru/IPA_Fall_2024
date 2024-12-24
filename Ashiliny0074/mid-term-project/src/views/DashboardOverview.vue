<template>
    <div class="p-6">
      <h1 class="text-2xl font-semibold text-gray-900 mb-6">Dashboard Overview</h1>
  
      <!-- Metrics Grid -->
      <div class="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-4">
        <!-- Temperature Card -->
        <div class="bg-white overflow-hidden shadow rounded-lg">
          <div class="p-5">
            <div class="flex justify-between">
              <div>
                <p class="text-sm font-medium text-gray-500 truncate">Temperature</p>
                <p class="mt-1 text-3xl font-semibold text-gray-900">{{ metrics.temperature }}°C</p>
              </div>
              <div :class="`mt-1 text-sm ${getStatusColor('temperature')}`">
                {{ getStatusText('temperature') }}
              </div>
            </div>
          </div>
        </div>
  
        <!-- Humidity Card -->
        <div class="bg-white overflow-hidden shadow rounded-lg">
          <div class="p-5">
            <div class="flex justify-between">
              <div>
                <p class="text-sm font-medium text-gray-500 truncate">Humidity</p>
                <p class="mt-1 text-3xl font-semibold text-gray-900">{{ metrics.humidity }}%</p>
              </div>
              <div :class="`mt-1 text-sm ${getStatusColor('humidity')}`">
                {{ getStatusText('humidity') }}
              </div>
            </div>
          </div>
        </div>
  
        <!-- Soil Moisture Card -->
        <div class="bg-white overflow-hidden shadow rounded-lg">
          <div class="p-5">
            <div class="flex justify-between">
              <div>
                <p class="text-sm font-medium text-gray-500 truncate">Soil Moisture</p>
                <p class="mt-1 text-3xl font-semibold text-gray-900">{{ metrics.soilMoisture }}%</p>
              </div>
              <div :class="`mt-1 text-sm ${getStatusColor('soilMoisture')}`">
                {{ getStatusText('soilMoisture') }}
              </div>
            </div>
          </div>
        </div>
  
        <!-- Light Level Card -->
        <div class="bg-white overflow-hidden shadow rounded-lg">
          <div class="p-5">
            <div class="flex justify-between">
              <div>
                <p class="text-sm font-medium text-gray-500 truncate">Light Level</p>
                <p class="mt-1 text-3xl font-semibold text-gray-900">{{ metrics.lightLevel }} lux</p>
              </div>
              <div :class="`mt-1 text-sm ${getStatusColor('lightLevel')}`">
                {{ getStatusText('lightLevel') }}
              </div>
            </div>
          </div>
        </div>
      </div>
  
      <!-- Controls -->
      <div class="mt-6 bg-white shadow rounded-lg p-4">
        <div class="flex justify-between items-center">
          <div class="flex items-center space-x-4">
            <button 
              @click="toggleAutoRefresh" 
              :class="`px-4 py-2 rounded-md text-sm font-medium ${
                isAutoRefreshing 
                  ? 'bg-green-600 text-white hover:bg-green-700' 
                  : 'bg-red-600 text-white hover:bg-red-700'
              }`"
            >
              {{ isAutoRefreshing ? 'Auto Refresh On' : 'Auto Refresh Off' }}
            </button>
            <select 
              v-model="refreshInterval" 
              class="rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
            >
              <option :value="1000">1 second</option>
              <option :value="3000">3 seconds</option>
              <option :value="5000">5 seconds</option>
            </select>
          </div>
          <button 
            @click="updateMetrics"
            class="px-4 py-2 bg-blue-600 text-white rounded-md text-sm font-medium hover:bg-blue-700"
          >
            Refresh Now
          </button>
        </div>
      </div>
  
      <!-- Charts -->
      <div class="mt-6 grid grid-cols-1 lg:grid-cols-2 gap-6">
        <!-- Temperature Line Chart -->
        <div class="bg-white p-6 rounded-lg shadow">
          <h3 class="text-lg font-medium text-gray-900 mb-4">Temperature History</h3>
          <div class="h-64">
            <Line v-if="chartData.labels.length" :data="chartData" :options="chartOptions" />
          </div>
        </div>
  
        <!-- Humidity Line Chart -->
        <div class="bg-white p-6 rounded-lg shadow">
          <h3 class="text-lg font-medium text-gray-900 mb-4">Humidity History</h3>
          <div class="h-64">
            <Line v-if="humidityChartData.labels.length" :data="humidityChartData" :options="chartOptions" />
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref, shallowRef, onMounted, onUnmounted } from 'vue';
  import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
  } from 'chart.js';
  import { Line } from 'vue-chartjs';
  
  // Register Chart.js components
  ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
  );
  
  interface Metrics {
    temperature: number;
    humidity: number;
    soilMoisture: number;
    lightLevel: number;
  }
  
  // State
  const metrics = ref<Metrics>({
    temperature: 0,
    humidity: 0,
    soilMoisture: 0,
    lightLevel: 0
  });
  
  const isAutoRefreshing = ref(true);
  const refreshInterval = ref(3000);
  
  const thresholds = {
    temperature: { min: 18, max: 28 },
    humidity: { min: 40, max: 70 },
    soilMoisture: { min: 50, max: 80 },
    lightLevel: { min: 2000, max: 8000 }
  };
  
  // Chart data
  const chartData = shallowRef({
    labels: [],
    datasets: [{
      label: 'Temperature (°C)',
      borderColor: '#3B82F6',
      data: [],
      fill: false
    }]
  });
  
  const humidityChartData = shallowRef({
    labels: [],
    datasets: [{
      label: 'Humidity (%)',
      borderColor: '#10B981',
      data: [],
      fill: false
    }]
  });
  
  const chartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
      y: {
        beginAtZero: true
      }
    }
  };
  
  // Methods
  const getStatusColor = (metric: keyof Metrics) => {
    const value = metrics.value[metric];
    const threshold = thresholds[metric];
    
    if (value > threshold.max) return 'text-red-600';
    if (value < threshold.min) return 'text-yellow-600';
    return 'text-green-600';
  };
  
  const getStatusText = (metric: keyof Metrics) => {
    const value = metrics.value[metric];
    const threshold = thresholds[metric];
    
    if (value > threshold.max) return 'High';
    if (value < threshold.min) return 'Low';
    return 'Normal';
  };
  
  const updateMetrics = () => {
    // Update metrics with random data
    metrics.value = {
      temperature: +(20 + Math.random() * 10).toFixed(1),
      humidity: +(50 + Math.random() * 30).toFixed(1),
      soilMoisture: +(60 + Math.random() * 20).toFixed(1),
      lightLevel: Math.floor(1000 + Math.random() * 9000)
    };
  
    // Update chart data
    const now = new Date();
    const timeStr = now.toLocaleTimeString();
    
    // Update temperature chart
    chartData.value = {
      labels: [...(chartData.value.labels.slice(-9) || []), timeStr],
      datasets: [{
        ...chartData.value.datasets[0],
        data: [...(chartData.value.datasets[0].data.slice(-9) || []), metrics.value.temperature]
      }]
    };
  
    // Update humidity chart
    humidityChartData.value = {
      labels: [...(humidityChartData.value.labels.slice(-9) || []), timeStr],
      datasets: [{
        ...humidityChartData.value.datasets[0],
        data: [...(humidityChartData.value.datasets[0].data.slice(-9) || []), metrics.value.humidity]
      }]
    };
  };
  
  const toggleAutoRefresh = () => {
    isAutoRefreshing.value = !isAutoRefreshing.value;
    if (isAutoRefreshing.value) {
      updateInterval = window.setInterval(updateMetrics, refreshInterval.value);
    } else {
      clearInterval(updateInterval);
    }
  };
  
  let updateInterval: number;
  
  // Lifecycle hooks
  onMounted(() => {
    updateMetrics();
    updateInterval = window.setInterval(updateMetrics, refreshInterval.value);
  });
  
  onUnmounted(() => {
    if (updateInterval) {
      clearInterval(updateInterval);
    }
  });
  </script>