<template>
    <div class="event-demo" @click="handleDivClick">
      <h2>Event Demo</h2>
      <p>Click the button below to see the event propagation in action!</p >
      <button @click.stop="handleButtonClick">Click Me</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'EventDemo',
    methods: {
      handleDivClick() {
        alert('Div clicked!');
      },
      handleButtonClick() {
        alert('Button clicked!');
      },
    },
  };
  </script>
  
  <style scoped>
  .event-demo {
    padding: 20px;
    border: 1px solid #ccc;
    text-align: center;
    cursor: pointer;
  }
  
  button {
    padding: 10px 20px;
    margin-top: 20px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #0056b3;
  }
  </style>