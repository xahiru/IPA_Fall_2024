<template>
    <div id="chart-page">
    <nav class="navbar">
      <div class="logo">Greenhouse</div>
     
      <!-- Hamburger Icon for mobile -->
      <div class="hamburger" @click="toggleMenu">
        <span class="bar"></span>
        <span class="bar"></span>
        <span class="bar"></span>
      </div>
     
      <!-- Navbar Links -->
      <ul class="nav-links" :class="{'active': menuActive}">
        <li><router-link to="/">Home</router-link></li>
        <li><router-link to="/dashboard">Dashboard</router-link></li>
        <li><router-link to="/overview">Overview</router-link></li>
        <li><router-link to="/settings">Settings</router-link></li>
        <li><router-link to="/charts">Charts</router-link></li>
        <li><a @click="logout">Logout</a></li>
      </ul>
    </nav>

      <h1 class="title">Static Historical Data Charts</h1>
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
          <Line :data="tempChartData" :options="chartOptions" />
        </div>
  
        <!-- Humidity Chart -->
        <div class="chart-container">
          <Line :data="humidityChartData" :options="chartOptions" />
        </div>
  
        <!-- Moisture Chart -->
        <div class="chart-container">
          <Line :data="moistureChartData" :options="chartOptions" />
        </div>
  
        <!-- Light Chart -->
        <div class="chart-container">
          <Line :data="lightChartData" :options="chartOptions" />
        </div>
      </div>
    </div>
  </template> 
  
  <script setup>
  import { ref, watch, onMounted, onBeforeUnmount } from 'vue';
  import { Line } from 'vue-chartjs';
  import { Chart as ChartJS, registerables } from 'chart.js';
  
  const menuActive = ref(false);
  
  const toggleMenu = () => {
    menuActive.value = !menuActive.value;
  };
  
  const logout = async () => {
    localStorage.removeItem("user");
    window.location.href = '/login';
  };

  // Register Chart.js components
  ChartJS.register(...registerables);
  
  // Static data for historical data (replace with actual data as needed)
  const staticHistoricalData = {
    '1h': {
      labels: ['10:00', '10:05', '10:10', '10:15', '10:20', '10:25', '10:30', '10:35', '10:40', '10:45', '10:50', '10:55'],
      tempData: [25, 27, 28, 29, 30, 29, 28, 27, 26, 25, 26, 27],
      humidityData: [60, 62, 61, 63, 65, 64, 63, 62, 61, 60, 61, 62],
      moistureData: [30, 32, 34, 35, 33, 34, 36, 37, 39, 40, 41, 42],
      lightData: [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310],
    },
  };
  
  // Reactive state for chart data and configuration
  const tempChartData = ref({
    labels: staticHistoricalData['1h'].labels,
    datasets: [
      {
        label: 'Temperature (°C)',
        borderColor: '#3498db',
        backgroundColor: 'rgba(52, 152, 219, 0.2)',
        data: staticHistoricalData['1h'].tempData,
      },
    ],
  });
  
  const humidityChartData = ref({
    labels: staticHistoricalData['1h'].labels,
    datasets: [
      {
        label: 'Humidity (%)',
        borderColor: '#2ecc71',
        backgroundColor: 'rgba(46, 204, 113, 0.2)',
        data: staticHistoricalData['1h'].humidityData,
      },
    ],
  });
  
  const moistureChartData = ref({
    labels: staticHistoricalData['1h'].labels,
    datasets: [
      {
        label: 'Moisture (%)',
        borderColor: '#f39c12',
        backgroundColor: 'rgba(243, 156, 18, 0.2)',
        data: staticHistoricalData['1h'].moistureData,
      },
    ],
  });
  
  const lightChartData = ref({
    labels: staticHistoricalData['1h'].labels,
    datasets: [
      {
        label: 'Light (lux)',
        borderColor: '#e74c3c',
        backgroundColor: 'rgba(231, 76, 60, 0.2)',
        data: staticHistoricalData['1h'].lightData,
      },
    ],
  });
  
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
  
  // Function to update chart data based on selected period
  const updateChartData = () => {
    const data = staticHistoricalData[selectedPeriod.value] || staticHistoricalData['1h'];
  
    // Update each chart dataset based on the selected period
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
  };
  
  // Watch period changes and update chart data
  watch(selectedPeriod, updateChartData, { immediate: true });
  
  // Interval for auto-updating chart every 5 seconds
  let dataChangeInterval = null;
  
  onMounted(() => {
    let dataIndex = 0;
  
    // Update the chart data every 5 seconds
    dataChangeInterval = setInterval(() => {
      const data = staticHistoricalData[selectedPeriod.value] || staticHistoricalData['1h'];
      dataIndex = (dataIndex + 1) % data.labels.length;
  
      // Update each chart dataset with sliced data
      tempChartData.value.datasets = [
        {
          label: 'Temperature (°C)',
          borderColor: '#3498db',
          backgroundColor: 'rgba(52, 152, 219, 0.2)',
          data: data.tempData.slice(0, dataIndex + 1),
        },
      ];
  
      humidityChartData.value.datasets = [
        {
          label: 'Humidity (%)',
          borderColor: '#2ecc71',
          backgroundColor: 'rgba(46, 204, 113, 0.2)',
          data: data.humidityData.slice(0, dataIndex + 1),
        },
      ];
  
      moistureChartData.value.datasets = [
        {
          label: 'Moisture (%)',
          borderColor: '#f39c12',
          backgroundColor: 'rgba(243, 156, 18, 0.2)',
          data: data.moistureData.slice(0, dataIndex + 1),
        },
      ];
  
      lightChartData.value.datasets = [
        {
          label: 'Light (lux)',
          borderColor: '#e74c3c',
          backgroundColor: 'rgba(231, 76, 60, 0.2)',
          data: data.lightData.slice(0, dataIndex + 1),
        },
      ];
    }, 5000); // Change every 5 seconds
  });
  
  onBeforeUnmount(() => {
    if (dataChangeInterval) {
      clearInterval(dataChangeInterval);
    }
  });
  </script>
  
    
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
    padding-top: 70px;
  }
  
  .navbar {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1.2rem 2rem;
    background: #2d3e50;
    color: white;
    z-index: 100;
    transition: all 0.3s ease; /* Add smooth transition */
  }
  
  .logo {
    font-size: 1.8rem;
    font-weight: bold;
  }
  
  .nav-links {
    list-style: none;
    display: flex;
    gap: 30px;
  }
  
  .nav-links a {
    color: #ffffff;
    text-decoration: none;
    font-size: 1.1rem;
  }
  
  .hamburger {
    display: none;
    flex-direction: column;
    gap: 5px;
    cursor: pointer;
  }
  
  .hamburger .bar {
    width: 25px;
    height: 4px;
    background-color: white;
    border-radius: 5px;
  }
  
  @media (max-width: 768px) {
    .nav-links {
      display: none;
      width: 100%;
      flex-direction: column;
      gap: 1rem;
      position: absolute;
      top: 70px;
      left: 0;
      background-color: #2d3e50;
      padding: 1rem 0;
      z-index: -1; /* Fix issue where links appear behind navbar */
    }
  
    .nav-links.active {
      display: flex;
      z-index: 9999; /* Ensure the links show above other elements */
    }
  
    .hamburger {
      display: flex;
    }
  
    .nav-links li {
      width: 100%;
    }
  
    .nav-links a {
      padding: 0.5rem 1rem;
      font-size: 1.2rem;
    }
  }
/* Adjust Main Content to account for navbar */
main {
  padding: 2rem;
  margin-top: 80px; /* Add margin top to prevent overlap with navbar */
  flex: 1;
}

/* Media Queries for Responsiveness */

/* For Tablets and Larger Screens (min-width: 1024px) */
@media (min-width: 1024px) {
  .nav-links {
    display: flex;
    gap: 30px;
  }
}

/* For Mobile Screens (max-width: 767px) */
@media (max-width: 767px) {
  /* Navbar - Stack links vertically on small screens */
  .nav-links {
    display: block;
    text-align: center;
    gap: 10px;
    padding: 0;
  }

  /* Adjust navbar padding on small screens */
  .navbar {
    padding: 1rem 1.5rem;
  }

  /* Adjust logo font size for mobile */
  .logo {
    font-size: 1.6rem;
  }
}

#chart-page {
  font-family: 'Roboto', sans-serif;
  max-width: 100%;
  margin: 2rem auto;
  padding: 2rem;
  background: white;
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
a:hover{
    cursor: pointer;
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

/* Flexbox to align charts in a row */
.chart-container-wrapper {
  display: flex;
  flex-wrap: wrap; /* Allow wrapping of charts to the next line if space is limited */
  justify-content: space-between;
  gap: 20px; /* Space between charts */
}

.chart-container {
  position: relative;
  height: 400px;
  width: 48%; /* Adjust width to allow two charts per row */
}


@media (max-width: 1024px) {
  /* For tablets */
  .chart-container {
    height: 350px;
    width: 48%; /* Keep charts side by side on smaller screens */
  }

  .input-field {
    width: 80%;
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
  /* For mobile screens */
  #chart-page {
    padding: 1rem;
  }

  .chart-container-wrapper {
    flex-direction: column; /* Stack charts vertically on mobile */
  }

  .chart-container {
    height: 300px;
    width: 100%; /* Full width for each chart on smaller screens */
  }

  .input-field {
    width: 100%;
  }

  .title {
    font-size: 1.6rem;
    margin-top: 200px;
  }

  .subtitle {
    font-size: 0.85rem;
  }
}

@media (max-width: 480px) {
  /* For very small mobile screens */
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
}
</style>
