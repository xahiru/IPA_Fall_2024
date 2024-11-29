<template>
    <div class="expression-demo">
      <h2>JavaScript Expressions Demo</h2>
      <div>
        <label for="num1">Number 1:</label>
        <input type="number" id="num1" v-model.number="num1" />
      </div>
      <div>
        <label for="num2">Number 2:</label>
        <input type="number" id="num2" v-model.number="num2" />
      </div>
      
      <h3>Results:</h3>
      <p>The sum of num1 and num2 is: {{ num1 + num2 }}</p >
      <p>The difference is: {{ num1 - num2 }}</p >
      <p>The product is: {{ num1 * num2 }}</p >
      <p>The quotient is: {{ num2 !== 0 ? (num1 / num2) : 'Cannot divide by zero' }}</p >
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
  .expression-demo {
    max-width: 400px;
    margin: auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    text-align: center;
  }
  
  label {
    display: block;
    margin: 10px 0 5px;
  }
  
  input {
    width: 100%;
    padding: 8px;
    margin-bottom: 20px;
  }
  
  p {
    margin: 10px 0;
  }
  </style>