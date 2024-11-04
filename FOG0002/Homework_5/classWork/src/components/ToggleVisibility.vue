<script setup>
    import { ref } from 'vue';
    const isActive = ref(false);
    const handleClick=()=>{
        isActive.value = !isActive.value;
    }
</script>

<template>
    <div>
        <div v-if="isActive">
            <h2>This is visible</h2>
        </div>
        <button @click="handleClick">BTN</button>
    </div>
</template>