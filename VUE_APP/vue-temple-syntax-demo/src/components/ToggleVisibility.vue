<script setup>
import { ref } from 'vue';

const isVisible = ref(true);
const toggleVisibility = () => {
  isVisible.value = !isVisible.value;
};
</script>

<template>
  <div>
    <h2>Conditional Rendering</h2>
    <button @click="toggleVisibility">
      Toggle Visibility
    </button>
    <p v-if="isVisible">This is visible when using v-if</p>
    <p v-show="isVisible">This is visible when using v-show</p>
  </div>
</template>

<style scoped>
button {
  background-color: #42b983;
  color: white;
  padding: 5px 10px;
  border: none;
  border-radius: 3px;
  cursor: pointer;
  margin-bottom: 10px;
}
</style>
