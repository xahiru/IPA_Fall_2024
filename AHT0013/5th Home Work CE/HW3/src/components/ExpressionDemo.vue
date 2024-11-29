<template>
    <div>
      <h2>Expression Demo</h2> 
      <div>
        <label for="num1">Number 1:</label>
        <input v-model="num1" type="number" id="num1" />
      </div>
  
      <div>
        <label for="num2">Number 2:</label>
        <input v-model="num2" type="number" id="num2" />
      </div>
      <div>
        <p>The sum of num1 and num2 is: {{ num1 + num2 }}</p>
        <p>The difference of num1 and num2 is: {{ num1 - num2 }}</p>
        <p>The product of num1 and num2 is: {{ num1 * num2 }}</p>
        <p>The quotient of num1 and num2 is: {{ num2 !== 0 ? num1 / num2 : 'Cannot divide by zero' }}</p>
      </div>
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
  div {
    margin: 20px;
  }
  
  label {
    margin-right: 10px;
  }
  
  input {
    padding: 8px;
    width: 150px;
    margin-bottom: 20px;
  }
  
  p {
    font-size: 16px;
    color: #b9b9b9;
  }
  </style>  