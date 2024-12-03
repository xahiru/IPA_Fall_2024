<template>
    <div>
      <label for="num1">Number 1:</label>
      <input type="number" v-model="num1" id="num1" />
  
      <label for="num2">Number 2:</label>
      <input type="number" v-model="num2" id="num2" />
  
      <div>
        <p>The sum of num1 and num2 is: {{ num1 + num2 }}</p>
        <p>The difference is: {{ num1 - num2 }}</p>
        <p>The product is: {{ num1 * num2 }}</p>
        <p>The quotient is: {{ num2 !== 0 ? (num1 / num2) : 'Cannot divide by zero' }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ExpressionDemo',
    data() {
      return {
        num1: 0,
        num2: 0,
      };
    },
  };
  </script>
  
  <style scoped>
  div {
    padding: 20px;
  }
  
  label {
    margin-right: 10px;
  }
  
  input {
    margin-bottom: 10px;
  }
  
  p {
    font-size: 1.1em;
  }
  </style>
  