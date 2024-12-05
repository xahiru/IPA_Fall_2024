<template>
  <div class="calculator">
    <h2>Calculate your math here</h2>

    <div class="input-group">
      <label for="num1">Enter Num 1:</label>
      <input type="number" v-model.number="num1" id="num1" placeholder="Enter Num" />
    </div>
    
    <div class="input-group">
      <label for="num2">Enter Num 2:</label>
      <input type="number" v-model.number="num2" id="num2" placeholder="Enter Num" />
    </div>

    <div class="buttons">
      <button @click="calculate('add')">Add</button>
      <button @click="calculate('subtract')">Subtract</button>
      <button @click="calculate('multiply')">Multiply</button>
      <button @click="calculate('divide')">Divide</button>
    </div>

    <div v-if="result !== null" class="result">
      <p v-if="operation === 'add'">Total: {{ result }}</p>
      <p v-if="operation === 'subtract'">The difference is: {{ result }}</p>
      <p v-if="operation === 'multiply'">The product is: {{ result }}</p>
      <p v-if="operation === 'divide'">The quotient is: {{ result }}</p>
    </div>

    <div v-if="errorMessage" class="error">
      <p>{{ errorMessage }}</p>
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
      result: null,
      operation: null,
      errorMessage: null,
    };
  },
  methods: {
    calculate(operation) {
      this.errorMessage = null;
      this.operation = operation;

      if (operation === "add") {
        this.result = this.num1 + this.num2;
      } else if (operation === "subtract") {
        this.result = this.num1 - this.num2;
      } else if (operation === "multiply") {
        this.result = this.num1 * this.num2;
      } else if (operation === "divide") {
        if (this.num2 === 0) {
          this.errorMessage = "Cannot divide by zero";
          this.result = null;
        } else {
          this.result = (this.num1 / this.num2).toFixed(2);
        }
      }
    },
  },
};
</script>

<style scoped>
.calculator {
  max-width: 400px;
  margin: 30px auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgb(0, 0, 0, 0.1);
}

h2 {
  text-align: center;
  color: #2d3e50;
}

.input-group {
  margin-bottom: 15px;
}

label {
  margin-right: 10px;
  font-size: 14px;
  color: #333;
}

input {
  padding: 8px;
  width: 100%;
  margin-top: 5px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 14px;
}

.buttons {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}

button {
  background-color: #4CAF50;
  color: white;
  border: none;
  padding: 10px 15px;
  cursor: pointer;
  border-radius: 5px;
  font-size: 16px;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #45a049;
}

.result {
  margin-top: 20px;
  padding: 10px;
  background-color: #f0f8ff;
  border: 1px solid #d1ecf1;
  border-radius: 4px;
  color: #0c5460;
}

.error {
  margin-top: 20px;
  padding: 10px;
  background-color: #f8d7da;
  border: 1px solid #f5c6cb;
  border-radius: 4px;
  color: #721c24;
}
</style>
