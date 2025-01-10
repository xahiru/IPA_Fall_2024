<script setup>
import { ref, watch, onMounted, onBeforeUnmount } from 'vue';
import { Line } from 'vue-chartjs';
import { Chart as ChartJS, registerables } from 'chart.js';
import Navbar from './Navbar.vue';

// Register Chart.js components
ChartJS.register(...registerables);

// Simulated API call to fetch data
const fetchDataForPeriod = (period) => {
  // Simulate API call with different data for each period
  const mockData = {
    '1h': {
      labels: ['10:00', '10:05', '10:10', '10:15', '10:20', '10:25', '10:30', '10:35', '10:40', '10:45', '10:50', '10:55'],
      tempData: [23, 24, 25, 26, 27, 28, 27, 26, 25, 24, 23, 22],
      humidityData: [55, 57, 59, 60, 62, 64, 63, 61, 60, 59, 58, 57],
      moistureData: [25, 27, 28, 30, 32, 33, 32, 31, 30, 29, 28, 27],
      lightData: [180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290],
    },
    '6h': {
      labels: ['08:00', '09:00', '10:00', '11:00', '12:00', '13:00'],
      tempData: [20, 21, 22, 23, 24, 25],
      humidityData: [50, 52, 55, 57, 60, 62],
      moistureData: [20, 22, 24, 26, 28, 30],
      lightData: [150, 160, 170, 180, 190, 200],
    },
    '24h': {
      labels: ['Yesterday', 'Morning', 'Afternoon', 'Evening'],
      tempData: [22, 23, 24, 25],
      humidityData: [50, 55, 60, 62],
      moistureData: [20, 25, 30, 35],
      lightData: [180, 190, 210, 220],
    }
  };
  return mockData[period] || mockData['1h']; // default to '1h' data
};

// Reactive state for chart data and configuration
const tempChartData = ref({});
const humidityChartData = ref({});
const moistureChartData = ref({});
const lightChartData = ref({});
const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      position: 'top',
    },
  },
  scales: {
    x: {
      type: 'category',
      title: {
        display: true,
        text: 'Time',
      },
    },
    y: {
      title: {
        display: true,
        text: 'Value',
      },
    },
  },
};

// Period selection
const selectedPeriod = ref('1h'); // Default period
const periods = [
  { label: 'Last 1 Hour', value: '1h' },
  { label: 'Last 6 Hours', value: '6h' },
  { label: 'Last 24 Hours', value: '24h' },
];

// Loading state
const isLoading = ref(false);

// Function to update chart data based on selected period
const updateChartData = () => {
  isLoading.value = true;
  const data = fetchDataForPeriod(selectedPeriod.value);
  tempChartData.value = {
    labels: data.labels,
    datasets: [
      {
        label: 'Temperature (°C)',
        borderColor: '#3498db',
        backgroundColor: 'rgba(52, 152, 219, 0.2)',
        data: data.tempData,
      },
    ],
  };

  humidityChartData.value = {
    labels: data.labels,
    datasets: [
      {
        label: 'Humidity (%)',
        borderColor: '#2ecc71',
        backgroundColor: 'rgba(46, 204, 113, 0.2)',
        data: data.humidityData,
      },
    ],
  };

  moistureChartData.value = {
    labels: data.labels,
    datasets: [
      {
        label: 'Moisture (%)',
        borderColor: '#f39c12',
        backgroundColor: 'rgba(243, 156, 18, 0.2)',
        data: data.moistureData,
      },
    ],
  };

  lightChartData.value = {
    labels: data.labels,
    datasets: [
      {
        label: 'Light (lux)',
        borderColor: '#e74c3c',
        backgroundColor: 'rgba(231, 76, 60, 0.2)',
        data: data.lightData,
      },
    ],
  };

  isLoading.value = false;
};

// Watch period changes and update chart data
watch(selectedPeriod, updateChartData, { immediate: true });

// Interval for auto-updating chart every 5 seconds
let dataChangeInterval = null;

onMounted(() => {
  updateChartData(); // Initialize chart data on mounted

  // Update the chart data every 5 seconds (simulating live data update)
  dataChangeInterval = setInterval(() => {
    updateChartData(); // Update chart data every 5 seconds
  }, 5000);
});

onBeforeUnmount(() => {
  if (dataChangeInterval) {
    clearInterval(dataChangeInterval);
  }
});
</script>

<template>
  <div>
    <Navbar />
    <div id="chart-page">
      <h1 class="title">Historical Data Charts</h1>
      <p class="subtitle">View trends of temperature, humidity, moisture, and light over time.</p>

      <!-- Period Selector -->
      <div class="period-selector">
        <label for="period">Select Period:</label>
        <select id="period" v-model="selectedPeriod" class="input-field">
          <option v-for="period in periods" :key="period.value" :value="period.value">
            {{ period.label }}
          </option>
        </select>
      </div>

      <!-- Chart Containers Wrapper -->
      <div class="chart-container-wrapper">
        <!-- Temperature Chart -->
        <div class="chart-container">
          <Line v-if="!isLoading" :data="tempChartData" :options="chartOptions" />
          <p v-else>Loading...</p>
        </div>

        <!-- Humidity Chart -->
        <div class="chart-container">
          <Line v-if="!isLoading" :data="humidityChartData" :options="chartOptions" />
          <p v-else>Loading...</p>
        </div>

        <!-- Moisture Chart -->
        <div class="chart-container">
          <Line v-if="!isLoading" :data="moistureChartData" :options="chartOptions" />
          <p v-else>Loading...</p>
        </div>

        <!-- Light Chart -->
        <div class="chart-container">
          <Line v-if="!isLoading" :data="lightChartData" :options="chartOptions" />
          <p v-else>Loading...</p>
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Roboto', sans-serif;
  background: #f4f6f9;
  color: #333;
}

#chart-page {
  max-width: 100%;
  margin: 2rem auto;
  padding: 2rem;
  background: white;
  margin-top: 200px;
  border-radius: 10px;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
}

.title {
  font-size: 2rem;
  color: #34495e;
  margin-bottom: 0.5rem;
  text-align: center;
}

.subtitle {
  font-size: 1rem;
  color: #7f8c8d;
  margin-bottom: 1.5rem;
  text-align: center;
}

.period-selector {
  margin-bottom: 1rem;
  text-align: center;
}

.input-field {
  padding: 10px;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
  outline: none;
  width: 200px;
  max-width: 100%;
}

.input-field:focus {
  border-color: #3498db;
}

.chart-container-wrapper {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  gap: 20px;
}

.chart-container {
  position: relative;
  height: 400px;
  width: 48%; /* Keep it to 48% width on larger screens */
}

/* Media Queries for different screen sizes */

@media (max-width: 1024px) {
  #chart-page{
    margin-top: 200px;
  }
  .chart-container {
    height: 400px;
    width: 48%; /* Charts will take 48% of the screen width */
  }

  .input-field {
    width: 80%; /* Reduce the width of the input field to 80% */
    margin: 0 auto;
  }

  .title {
    font-size: 1.8rem;
  }

  .subtitle {
    font-size: 0.9rem;
  }
}

@media (max-width: 768px) {
  #chart-page {
    padding: 1rem; 
    margin-top: 770px;
  }

  .chart-container-wrapper {
    flex-direction: column; /* Stack charts vertically */
  }

  .chart-container {
    height: 300px;
    width: 100%; /* Make charts take up full width */
    margin-bottom: 20px; /* Add some space between stacked charts */
  }

  .input-field {
    width: 100%; /* Make the input field full width */
  }

  .title {
    font-size: 1.6rem;
  }

  .subtitle {
    font-size: 0.85rem;
  }
}

@media (max-width: 480px) {
  .title {
    font-size: 1.4rem;
    margin-top: 100px;
  }

  .subtitle {
    font-size: 0.8rem;
  }

  .input-field {
    font-size: 0.9rem;
  }

  .chart-container {
    height: 250px; /* Reduce chart height for very small screens */
  }
}
</style>
