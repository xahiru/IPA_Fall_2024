<template>
    <div class="expression-demo">
      <h2>JavaScript Expressions in Vue</h2>
      <div>
        <label for="num1">Number 1:</label>
        <input v-model.number="num1" type="number" id="num1" placeholder="Enter a number" />
      </div>
  
      <div>
        <label for="num2">Number 2:</label>
        <input v-model.number="num2" type="number" id="num2" placeholder="Enter a number" />
      </div>

        <p>The sum of num1 and num2 is: {{ num1 + num2 }}</p>
        <p>The difference of num1 and num2 is: {{ num1 - num2 }}</p>
        <p>The product of num1 and num2 is: {{ num1 * num2 }}</p>
        <p>The quotient of num1 and num2 is: 
          <span v-if="num2 !== 0">{{ num1 / num2 }}</span>
          <span v-else>Cannot divide by zero</span>
        </p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        num1: 0,
        num2: 0
      };
    }
  };
  </script>
  
  <style scoped>
  .expression-demo {
    max-width: 400px;
    margin: auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
    text-align: center;
  }
  
  input {
    width: 100%;
    padding: 0.5em;
    margin-bottom: 10px;
  }
  
  p {
    font-size: 1.2em;
    margin: 10px 0;
  }
  
  h2 {
    margin-bottom: 20px;
  }
  </style>  