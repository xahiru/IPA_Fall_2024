<script setup>
import { ref } from 'vue';

const isActive = ref(false);

const handleClick = () => {
    isActive.value = !isActive.value;
}
</script>

<template>
    <div class="container">
        <div v-if="isActive" class="message">
            <h2>This is visible</h2>
        </div>
        <button @click="handleClick" class="toggle-btn">Toggle Visibility</button>
    </div>
</template>

<style scoped>
.container {
    font-family: 'Arial', sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #f7f7f7;
    margin: 0;
}

.message {
    background-color: #28a745;
    color: white;
    padding: 15px;
    border-radius: 8px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.toggle-btn {
    padding: 12px 20px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 16px;
    cursor: pointer;
    margin-top: 20px;
    transition: background-color 0.3s ease;
}

.toggle-btn:hover {
    background-color: #0056b3;
}
</style>
