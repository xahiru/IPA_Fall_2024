<template>
    <div class="metric-card">
      <h3>{{ title }}</h3>
      <p>{{ value }} {{ unit }}</p>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      title: String,
      value: Number,
      unit: String,
    },
  };
  </script>
  
  <style>
  .metric-card {
    border: 1px solid #ccc;
    padding: 1rem;
    border-radius: 8px;
    text-align: center;
    width: 200px;
  }
  </style>
  