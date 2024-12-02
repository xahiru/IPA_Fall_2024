<template>
    <div>
      <h2>Expression Demo</h2>
      
      
      <label for="num1">Number 1:</label>
      <input id="num1" type="number" v-model="num1" />
      
      <label for="num2">Number 2:</label>
      <input id="num2" type="number" v-model="num2" />

      <p>The sum of num1 and num2 is: {{ num1 + num2 }}</p>
      <p>The difference is: {{ num1 - num2 }}</p>
      <p>The product is: {{ num1 * num2 }}</p>
      <p>The quotient is: {{ num2 !== 0 ? (num1 / num2).toFixed(2) : 'undefined (division by zero)' }}</p>
    </div>
  </template>
  
  <script>
  export default {
    name: "ExpressionDemo",
    data() {
      return {
        num1: 0,
        num2: 0,
      };
    },
  };
  </script>
  
  <style scoped>
  h2 {
    color: #333;
  }
  input {
    margin: 5px;
  }
  p {
    font-size: 1.2em;
  }
  </style>  