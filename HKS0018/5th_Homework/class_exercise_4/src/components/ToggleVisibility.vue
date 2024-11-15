<script setup>
import { ref } from 'vue';

const isActive = ref(false);

const handleClick = () => {
    isActive.value = !isActive.value;
};
</script>

<template>
    <div>
        <div v-if="isActive">
            <h2>You died!</h2>
        </div>

        <button @click="handleClick">Don't Click</button>
    </div>
</template>

<style scoped>
button {
    padding: 10px 20px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #d50e0e;
}

h2 {
    color: #0c0c0b;
}
</style>
