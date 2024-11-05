<template>
    <div @click="handleDivClick">
      <button @click.stop="handleButtonClick">Click me!</button>
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
  div {
    padding: 20px;
    background-color: #f0f0f0;
    border: 1px solid #ddd;
  }
  
  button {
    margin: 10px;
  }
  </style>
  