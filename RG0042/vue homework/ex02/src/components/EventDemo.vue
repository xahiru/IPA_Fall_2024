<template>
    <div @click="onDivClick" style="padding: 20px; border: 1px solid black;">
      <p>Click inside this area to see event propagation in action.</p>
      <button @click.stop="onButtonClick">Click Me</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'EventDemo',
    methods: {
      onDivClick() {
        alert("Div clicked!");
      },
      onButtonClick() {
        alert("Button clicked!");
      }
    }
  };
  </script>
  
  <style scoped>
  button {
    margin-top: 10px;
  }
  </style>  