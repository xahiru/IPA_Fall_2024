<template>
    <div class="chart-wrapper">
      <Line
        v-if="loaded"
        :data="chartData"
        :options="chartOptions"
      />
    </div>
  </template>
  
  <script>
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
  import { Line } from 'vue-chartjs'
  
  ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
  )
  
  export default {
    name: 'SimpleLineChart',
    components: { Line },
    props: {
      label: {
        type: String,
        required: true
      },
      data: {
        type: Array,
        required: true
      }
    },
    data() {
      return {
        loaded: false
      }
    },
    computed: {
      chartData() {
        return {
          labels: this.data.map((_, index) => `${index + 1} second(s) ago`).reverse(),
          datasets: [
            {
              label: this.label,
              data: [...this.data],
              borderColor: '#42b983',
              tension: 0.4
            }
          ]
        }
      },
      chartOptions() {
        return {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: {
              position: 'top'
            }
          }
        }
      }
    },
    mounted() {
      this.loaded = true
    }
  }
  </script>
  
  <style scoped>
  .chart-wrapper {
    height: 300px;
    margin: 20px 0;
  }
  </style>