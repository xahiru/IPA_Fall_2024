<script setup>
import { ref } from 'vue';

const num1 = ref(0);
const num2 = ref(0);
</script>

<template>
  <div>
    <h2>JavaScript Expressions</h2>
    <input v-model.number="num1" type="number" placeholder="Enter first number" />
    <input v-model.number="num2" type="number" placeholder="Enter second number" />
    <p>The sum of {{ num1 }} and {{ num2 }} is: {{ num1 + num2 }}</p>
    <p>The difference is: {{ num1 - num2 }}</p>
    <p>The product is: {{ num1 * num2 }}</p>
    <p v-if="num2 !== 0">The quotient is: {{ num1 / num2 }}</p>
    <p v-else>The quotient is undefined (cannot divide by zero).</p>
  </div>
</template>

<style scoped>
input {
  margin-right: 10px;
  padding: 5px;
}
</style>
