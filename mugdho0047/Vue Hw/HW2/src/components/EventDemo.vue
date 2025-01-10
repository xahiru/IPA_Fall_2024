<template>
    <div @click="handleDivClick" class="container">
      <p>Click anywhere inside this div.</p>
      <button @click.stop="handleButtonClick">Click Me</button>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      handleDivClick() {
        alert('Div clicked!');
      },
      handleButtonClick() {
        alert('Button clicked!');
      }
    }
  };
  </script>
  
  <style scoped>
  .container {
    padding: 20px;
    border: 1px solid #ccc;
    text-align: center;
  }
  
  button {
    padding: 10px 20px;
    margin-top: 10px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #0056b3;
  }
  </style>  