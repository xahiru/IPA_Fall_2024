<template>
    <div class="card" :class="{ warning: isWarning }">
      <div class="label">{{ label }}</div>
      <div class="value">
        {{ value }} <span class="unit">{{ unit }}</span>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "DataCard",
    props: {
      label: {
        type: String,
        required: true,
      },
      unit: {
        type: String,
        default: "",
      },
      initialValue: {
        type: Number,
        default: 0,
      },
      min: {
        type: Number,
        default: 0,
      },
      max: {
        type: Number,
        default: 100,
      },
      autoUpdate: {
        type: Boolean,
        default: true,
      },
      warningThreshold: {
        type: Number,
        default: 80,
      },
    },
    data() {
      return {
        value: this.initialValue,
      };
    },
    computed: {
      isWarning() {
        return this.value > this.warningThreshold;
      },
    },
    methods: {
      updateValue() {
  
        this.value = parseFloat((this.min + Math.random() * (this.max - this.min)).toFixed(1));
      },
    },
    mounted() {
      if (this.autoUpdate) {
  
        this.updateInterval = setInterval(this.updateValue, 5000);
      }
    },
    beforeUnmount() {
  
      clearInterval(this.updateInterval);
    },
  };
  </script>
  
  <style scoped>
  .card {
    background-color: #ffffff;
    padding: 1.5rem;
    border-radius: 12px;
    box-shadow: 0 6px 10px rgba(0, 0, 0, 0.1);
    text-align: center;
    transition: transform 0.3s, background-color 0.3s;
  }
  
  .card:hover {
    transform: translateY(-5px);
  }
  
  .label {
    font-size: 1.2rem;
    color: #333;
    font-weight: 600;
  }
  
  .value {
    font-size: 2rem;
    font-weight: 700;
    color: #222;
  }
  
  .unit {
    font-size: 1rem;
    font-weight: 400;
    color: #666;
  }
  
  .card.warning {
    background-color: #ffe5e5;
    color: #d80000;
  }
  
  .card.warning .value {
    color: #d80000;
  }
  </style>  