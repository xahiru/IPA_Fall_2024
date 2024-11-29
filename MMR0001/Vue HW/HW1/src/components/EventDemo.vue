<template>
    <div @click="handleDivClick">
      <h1>EventDemo</h1>
      <button @click.stop="handleButtonClick">Click Me</button>
    </div>
  </template>
  
  <script>
  export default {
    name: "EventDemo",
    methods: {
      handleDivClick() {
        alert("Div clicked!");
      },
      handleButtonClick() {
        alert("Button clicked!");
      },
    },
  };
  </script>
  
  <style scoped>
  div {
    padding: 100px;
    border: 1px solid #cd6d6d;
  }
  
  button {
    padding: 10px;
  }
  </style>
  