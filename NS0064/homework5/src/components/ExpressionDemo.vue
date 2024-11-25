<script setup>
import { ref } from 'vue';

const num1 = ref('');
const num2 = ref('');
const sum = ref(0);
const difference = ref(0);
const product = ref(0);
const quotient = ref(0);
const isActive = ref(false);

const handleCalculator = () => {
    const n1 = parseFloat(num1.value);
    const n2 = parseFloat(num2.value);
    
    sum.value = n1 + n2;
    difference.value = n1 - n2;
    product.value = n1 * n2;
    quotient.value = n2 !== 0 ? (n1 / n2) : 'Cannot divide by zero'; 
    isActive.value = true; 
};
</script>

<template>
    <div>
        <div id="form-body">
            <div class="calculator-container">
                <form @submit.prevent="handleCalculator" class="calculator-form">
                    <h2>Enter two numbers</h2>
                    <div class="form-group">
                        <input type="text" id="num1" v-model="num1" required placeholder="First number">
                        <span class="operator">+</span>
                        <input type="text" id="num2" v-model="num2" required placeholder="Second number">
                    </div>
                    <button type="submit">Calculate</button>
                </form>
                <div class="calculator-result" v-if="isActive">
                    <h3>Results</h3>
                    <p>Sum = {{ sum }}</p>
                    <p>Difference = {{ difference }}</p>
                    <p>Product = {{ product }}</p>
                    <p>Quotient = {{ quotient }}</p>
                    <router-link to="/toggle-visibility" class="btn-link">Go to 4th homework</router-link>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
#form-body {
    font-family: 'Arial', sans-serif;
    background-color: #eaeaea;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
}

.calculator-container {
    background-color: #fff;
    padding: 30px;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    width: 350px;
    text-align: center;
}

.calculator-form h2 {
    color: #333;
    margin-bottom: 20px;
    font-size: 24px;
}

.form-group {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom: 20px;
}

input {
    width: 40%;
    padding: 10px;
    margin: 0 10px;
    border: 1px solid #ccc;
    border-radius: 8px;
    font-size: 16px;
    text-align: center;
}

.operator {
    font-size: 24px;
    font-weight: bold;
}

button {
    width: 100%;
    padding: 12px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 18px;
    cursor: pointer;
    margin-top: 20px;
}

button:hover {
    background-color: #45a049;
}

.calculator-result {
    margin-top: 20px;
    background-color: #f9f9f9;
    padding: 15px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
}

.calculator-result h3 {
    margin-bottom: 15px;
    color: #333;
}

.calculator-result p {
    font-size: 18px;
    color: #555;
    margin-bottom: 10px;
}

.btn-link {
    display: inline-block;
    margin-top: 20px;
    padding: 10px 20px;
    background-color: #007bff;
    color: white;
    text-decoration: none;
    border-radius: 4px;
}

.btn-link:hover {
    background-color: #0056b3;
}
</style>
