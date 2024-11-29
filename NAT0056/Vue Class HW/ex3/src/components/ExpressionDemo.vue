<template>
  <div>
    <h2>Calculate your math here</h2>
    
    <input type="number" v-model.number="num1" placeholder="Enter Num" />
    <input type="number" v-model.number="num2" placeholder="Enter Num" />

    <p>Total: {{ num1 + num2 }}</p>
    <p>The difference is: {{ num1 - num2 }}</p>
    <p>The product is: {{ num1 * num2 }}</p>
    <p>The quotient is: {{ num2 !== 0 ? (num1 / num2).toFixed(2) : "Cannot divide by zero" }}</p>
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
  margin: 30px;
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
  color: #0e69a7;
}
</style>  
