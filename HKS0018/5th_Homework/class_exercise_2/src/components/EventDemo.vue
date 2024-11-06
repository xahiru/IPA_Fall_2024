<template>
    <div @click="onDivClick">
      <button @click.stop="onButtonClick">Click Me</button>
    </div>
  </template>
  
  <script>
  export default {
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

  div {
    padding: 20px;
    background-color: #e99292;
  }
  button {
    padding: 30px 50px;
    cursor: pointer;
    background-color: #d55c5c;
  }

  :hover{color: #ffffff;}
  
  </style>
  