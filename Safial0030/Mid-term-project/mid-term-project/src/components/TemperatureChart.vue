<template>
    <div class="temperature-chart">
      <navbar />
      <div class="chart-container">
        <canvas id="temperatureChart"></canvas>
      </div>
    </div>
  </template>
  
  <script>
  import Chart from 'chart.js/auto';
  
  export default {
    name: 'TemperatureChart',
    data() {
      return {
        chart: null,
        temperatureData: [
          { x: '00:00am', y: 5 },
          { x: '01:00am', y: 4 },
          { x: '02:00am', y: 4 },
          { x: '03:00am', y: 3 },
          { x: '04:00am', y: 4 },
          { x: '05:00am', y: 5 },
          { x: '06:00am', y: 5 },
          { x: '07:00am', y: 7 },
          { x: '08:00am', y: 10 },
          { x: '09:00am', y: 12 },
          { x: '10:00am', y: 12 },
          { x: '11:00am', y: 14 },
          { x: '12:00pm', y: 13 },
          { x: '01:00pm', y: 15 },
          { x: '02:00pm', y: 17 },
          { x: '03:00pm', y: 16 },
          { x: '04:00pm', y: 15 },
          { x: '05:00pm', y: 13 },
          { x: '06:00pm', y: 10 },
          { x: '07:00pm', y: 9 },
          { x: '08:00pm', y: 9 },
          { x: '09:00pm', y: 7 },
          { x: '10:00pm', y: 8 },
          { x: '11:00pm', y: 7 },
          { x: '11:59pm', y: 6 },
          
          
        ]
      };
    },
    mounted() {
      const ctx = document.getElementById('temperatureChart').getContext('2d');
  
      this.chart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: this.temperatureData.map(data => data.x),
          datasets: [{
            label: 'Temperature (°C)',
            data: this.temperatureData.map(data => data.y),
            borderColor: 'rgb(255, 99, 132)',
            fill: false
          }]
        },
        options: {
          scales: {
            x: {
              title: {
                display: true,
                text: 'Time'
              }
            },
            y: {
              title: {
                display: true,
                text: 'Temperature (°C)'
              },
              beginAtZero: true
            }
          }
        }
      });
    },
    // eslint-disable-next-line vue/no-deprecated-destroyed-lifecycle
    beforeDestroy() {
      if (this.chart) {
        this.chart.destroy();
      }
    }
  };
  </script>
  
  <style scoped>
  
  
  .chart-container {
    margin-top: 80px; /* Adjust this value according to the navbar height */
    width: 1600x;
    height: 700px;
  }
  </style>