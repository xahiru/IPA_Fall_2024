<template>
  <div class="toggle-demo">
    <button @click="toggleVisibility">
      {{ isVisible ? 'Hide' : 'Show' }} Content
    </button>

    <div class="message-container">
      <div v-if="isVisible" class="message">
        This is visible when using v-if
      </div>

      <div v-show="isVisible" class="message">
        This is visible when using v-show
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const isVisible = ref(false)

const toggleVisibility = () => {
  isVisible.value = !isVisible.value
}
</script>

<style scoped>
.toggle-demo {
  padding: 20px;
  max-width: 400px;
  margin: 0 auto;
}

button {
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-bottom: 20px;
}

button:hover {
  background-color: #45a049;
}

.message-container {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.message {
  padding: 15px;
  background-color: #f0f0f0;
  border-radius: 4px;
  border: 1px solid #ddd;
}
</style>