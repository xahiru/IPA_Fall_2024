<template>
  <div class="p-6">
    <div class="md:flex md:items-center md:justify-between mb-6">
      <h2 class="text-2xl font-bold text-gray-900">Metrics & Analytics</h2>
      <div class="mt-4 flex space-x-3 md:mt-0">
        <select 
          v-model="timeRange" 
          class="rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
        >
          <option value="1h">Last Hour</option>
          <option value="24h">Last 24 Hours</option>
          <option value="7d">Last 7 Days</option>
          <option value="30d">Last 30 Days</option>
        </select>
        <button 
          @click="exportData"
          class="inline-flex items-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700"
        >
          Export Data
        </button>
      </div>
    </div>

    <!-- Charts Grid -->
    <div class="grid grid-cols-1 gap-6 lg:grid-cols-2">
      <!-- Temperature Chart -->
      <div class="bg-white rounded-lg shadow p-6">
        <h3 class="text-lg font-medium mb-4">Temperature Trends</h3>
        <div class="h-80">
          <Line 
            :data="temperatureData" 
            :options="chartOptions.temperature"
          />
        </div>
      </div>

      <!-- Humidity Chart -->
      <div class="bg-white rounded-lg shadow p-6">
        <h3 class="text-lg font-medium mb-4">Humidity Trends</h3>
        <div class="h-80">
          <Line 
            :data="humidityData" 
            :options="chartOptions.humidity"
          />
        </div>
      </div>

      <!-- Soil Moisture Chart -->
      <div class="bg-white rounded-lg shadow p-6">
        <h3 class="text-lg font-medium mb-4">Soil Moisture Trends</h3>
        <div class="h-80">
          <Line 
            :data="soilMoistureData" 
            :options="chartOptions.soilMoisture"
          />
        </div>
      </div>

      <!-- Light Level Chart -->
      <div class="bg-white rounded-lg shadow p-6">
        <h3 class="text-lg font-medium mb-4">Light Level Trends</h3>
        <div class="h-80">
          <Line 
            :data="lightLevelData" 
            :options="chartOptions.lightLevel"
          />
        </div>
      </div>
    </div>

    <!-- Statistics Summary -->
    <div class="mt-6 bg-white rounded-lg shadow">
      <div class="px-4 py-5 sm:p-6">
        <h3 class="text-lg font-medium mb-4">Statistics Summary</h3>
        <div class="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">
          <div v-for="(stat, key) in statistics" :key="key" class="p-4 border rounded-lg">
            <h4 class="text-sm font-medium text-gray-500">{{ stat.label }}</h4>
            <div class="mt-1 flex items-baseline justify-between">
              <div class="text-2xl font-semibold">{{ stat.value }}</div>
              <div :class="`text-sm ${stat.trend >= 0 ? 'text-green-600' : 'text-red-600'}`">
                {{ stat.trend >= 0 ? '+' : '' }}{{ stat.trend }}%
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, watch } from 'vue';
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

const timeRange = ref('24h');

// Chart configurations
const temperatureData = ref({
  labels: [],
  datasets: [{
    label: 'Temperature (°C)',
    backgroundColor: 'rgba(239, 68, 68, 0.2)',
    borderColor: '#EF4444',
    data: [],
    tension: 0.4
  }]
});

const humidityData = ref({
  labels: [],
  datasets: [{
    label: 'Humidity (%)',
    backgroundColor: 'rgba(59, 130, 246, 0.2)',
    borderColor: '#3B82F6',
    data: [],
    tension: 0.4
  }]
});

const soilMoistureData = ref({
  labels: [],
  datasets: [{
    label: 'Soil Moisture (%)',
    backgroundColor: 'rgba(16, 185, 129, 0.2)',
    borderColor: '#10B981',
    data: [],
    tension: 0.4
  }]
});

const lightLevelData = ref({
  labels: [],
  datasets: [{
    label: 'Light Level (lux)',
    backgroundColor: 'rgba(245, 158, 11, 0.2)',
    borderColor: '#F59E0B',
    data: [],
    tension: 0.4
  }]
});

const chartOptions = {
  temperature: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: 'top' as const
      }
    },
    scales: {
      y: {
        beginAtZero: true,
        title: {
          display: true,
          text: 'Temperature (°C)'
        }
      }
    }
  },
  humidity: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: 'top' as const
      }
    },
    scales: {
      y: {
        beginAtZero: true,
        max: 100,
        title: {
          display: true,
          text: 'Humidity (%)'
        }
      }
    }
  },
  soilMoisture: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: 'top' as const
      }
    },
    scales: {
      y: {
        beginAtZero: true,
        max: 100,
        title: {
          display: true,
          text: 'Soil Moisture (%)'
        }
      }
    }
  },
  lightLevel: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: 'top' as const
      }
    },
    scales: {
      y: {
        beginAtZero: true,
        title: {
          display: true,
          text: 'Light Level (lux)'
        }
      }
    }
  }
};

const statistics = ref({
  avgTemp: {
    label: 'Average Temperature',
    value: '23.5°C',
    trend: 2.4
  },
  avgHumidity: {
    label: 'Average Humidity',
    value: '65%',
    trend: -1.2
  },
  avgMoisture: {
    label: 'Average Soil Moisture',
    value: '72%',
    trend: 0.8
  },
  avgLight: {
    label: 'Average Light Level',
    value: '5240 lux',
    trend: 3.5
  }
});

const getTimeframeData = (timeframe: string) => {
  let dataPoints: number;
  let interval: number;

  switch (timeframe) {
    case '1h':
      dataPoints = 60; // One point per minute
      interval = 60000; // 1 minute in milliseconds
      break;
    case '24h':
      dataPoints = 144; // One point per 10 minutes
      interval = 600000; // 10 minutes in milliseconds
      break;
    case '7d':
      dataPoints = 168; // One point per hour
      interval = 3600000; // 1 hour in milliseconds
      break;
    case '30d':
      dataPoints = 180; // One point per 4 hours
      interval = 14400000; // 4 hours in milliseconds
      break;
    default:
      dataPoints = 144;
      interval = 600000;
  }

  const now = new Date();
  const labels = [];
  const data = {
    temperature: [],
    humidity: [],
    soilMoisture: [],
    lightLevel: []
  };

  for (let i = dataPoints - 1; i >= 0; i--) {
    const time = new Date(now.getTime() - (i * interval));
    
    // Format label based on timeframe
    let label;
    if (timeframe === '1h') {
      label = time.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    } else if (timeframe === '24h') {
      label = time.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    } else {
      label = time.toLocaleDateString([], { month: 'short', day: 'numeric', hour: '2-digit' });
    }
    labels.push(label);

    // Generate realistic data with trends
    const hourOfDay = time.getHours();
    const dayTrend = Math.sin((hourOfDay - 6) * Math.PI / 12); // Peak at noon, low at midnight

    // Temperature: varies between 18-28°C with daily cycle
    const tempBase = 23 + (dayTrend * 5);
    data.temperature.push(+(tempBase + (Math.random() * 2 - 1)).toFixed(1));

    // Humidity: inverse to temperature
    const humidityBase = 55 - (dayTrend * 15);
    data.humidity.push(+(humidityBase + (Math.random() * 5 - 2.5)).toFixed(1));

    // Soil Moisture: slowly varies
    const moistureBase = 65 + (Math.sin(i * 0.1) * 15);
    data.soilMoisture.push(+(moistureBase + (Math.random() * 3 - 1.5)).toFixed(1));

    // Light Level: follows daily cycle
    const lightBase = Math.max(0, dayTrend * 8000);
    data.lightLevel.push(Math.floor(lightBase + (Math.random() * 1000)));
  }

  return { labels, data };
};

const updateChartData = () => {
  const { labels, data } = getTimeframeData(timeRange.value);

  temperatureData.value = {
    labels,
    datasets: [{
      ...temperatureData.value.datasets[0],
      data: data.temperature
    }]
  };

  humidityData.value = {
    labels,
    datasets: [{
      ...humidityData.value.datasets[0],
      data: data.humidity
    }]
  };

  soilMoistureData.value = {
    labels,
    datasets: [{
      ...soilMoistureData.value.datasets[0],
      data: data.soilMoisture
    }]
  };

  lightLevelData.value = {
    labels,
    datasets: [{
      ...lightLevelData.value.datasets[0],
      data: data.lightLevel
    }]
  };

  // Update statistics
  statistics.value = {
    avgTemp: {
      label: 'Average Temperature',
      value: `${(data.temperature.reduce((a, b) => a + b, 0) / data.temperature.length).toFixed(1)}°C`,
      trend: +((data.temperature[data.temperature.length - 1] - data.temperature[0]).toFixed(1))
    },
    avgHumidity: {
      label: 'Average Humidity',
      value: `${(data.humidity.reduce((a, b) => a + b, 0) / data.humidity.length).toFixed(1)}%`,
      trend: +((data.humidity[data.humidity.length - 1] - data.humidity[0]).toFixed(1))
    },
    avgMoisture: {
      label: 'Average Soil Moisture',
      value: `${(data.soilMoisture.reduce((a, b) => a + b, 0) / data.soilMoisture.length).toFixed(1)}%`,
      trend: +((data.soilMoisture[data.soilMoisture.length - 1] - data.soilMoisture[0]).toFixed(1))
    },
    avgLight: {
      label: 'Average Light Level',
      value: `${Math.round(data.lightLevel.reduce((a, b) => a + b, 0) / data.lightLevel.length)} lux`,
      trend: +((data.lightLevel[data.lightLevel.length - 1] - data.lightLevel[0]) / 100).toFixed(1)
    }
  };
};

const exportData = () => {
  const data = {
    timeRange: timeRange.value,
    temperature: temperatureData.value,
    humidity: humidityData.value,
    soilMoisture: soilMoistureData.value,
    lightLevel: lightLevelData.value,
    statistics: statistics.value
  };

  const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `greenhouse-metrics-${timeRange.value}-${new Date().toISOString()}.json`;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
};

// Watch for timeRange changes
watch(timeRange, (newValue) => {
  updateChartData();
});

// Initialize data
onMounted(() => {
  updateChartData();
  
  // Update data periodically based on timeframe
  const updateInterval = setInterval(() => {
    if (timeRange.value === '1h') {
      updateChartData();
    }
  }, 60000); // Update every minute for 1h view

  onUnmounted(() => {
    clearInterval(updateInterval);
  });
});
</script>
