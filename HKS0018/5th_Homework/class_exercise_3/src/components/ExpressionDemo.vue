<script setup>
import { ref } from 'vue';

const num1 = ref('');
const num2 = ref('');
const sum = ref(0);
const difference = ref(0);
const isActive = ref(false);

const handleCalculator = () => {
    const n1 = parseFloat(num1.value);
    const n2 = parseFloat(num2.value);
    
    sum.value = n1 + n2;
    difference.value = n1 - n2;
    isActive.value = true; 
};
</script>

<template>
    <div>
        <div id="from-body">
            <div class="login-container">
                <form @submit.prevent="handleCalculator" class="login-form">
                    <h2 id="text1">Enter two numbers</h2>
                    <div class="form-group">
                        <input type="number" v-model="num1" placeholder="Enter first number" required />
                        <h2>+</h2>
                        <input type="number" v-model="num2" placeholder="Enter second number" required />
                        <h2>=</h2>
                    </div>
                    <button type="submit">Calculate</button>
                </form>
                <div class="calculator" v-if="isActive">
                    <h2>Sum = {{ sum }}</h2>
                    <h2>Difference = {{ difference }}</h2>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>

#from-body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 0;
}
#text1{
    color: black;
}
.login-container {
    background-color: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    width: 300px;
}

.login-form h2 {
    text-align: center;
    margin-bottom: 20px;
}

.form-group {
    margin-bottom: 15px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

input {
    width: 70%;
    padding: 10px;
    border: 1px solid #918787;
    border-radius: 4px;
}

button {
    width: 100%;
    padding: 10px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}

.calculator h2 {
    color: black;
    text-align: center;
    margin-top: 10px;
}
</style>
