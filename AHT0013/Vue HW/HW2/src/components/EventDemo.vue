<template>
    <div @click="handleDivClick">
      <p></p>
      <button @click.stop="handleButtonClick">Click me</button>
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
  </style>