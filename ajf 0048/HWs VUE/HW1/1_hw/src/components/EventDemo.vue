<template>
    <div class="event-demo" @click="handleDivClick">
      <p>Click anywhere in this box</p >
      <button @click.stop="handleButtonClick">Click this button</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'EventDemo',
    methods: {
      handleDivClick() {
        alert('Div clicked!')
      },
      handleButtonClick() {
        alert('Button clicked!')
      }
    }
  }
  </script>
  
  <style scoped>
  .event-demo {
    padding: 40px;
    background-color: #f0f0f0;
    border: 2px solid #ccc;
    border-radius: 8px;
    text-align: center;
    cursor: pointer;
  }
  
  button {
    padding: 10px 20px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #45a049;
  }
  
  p {
    margin-bottom: 20px;
    color: #666;
  }
  </style>