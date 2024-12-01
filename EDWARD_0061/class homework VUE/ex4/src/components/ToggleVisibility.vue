<template>
  <div class="toggle-container">
    <button @click="toggleVisibility">
      {{ isVisible ? 'Hide' : 'Show' }} Message
    </button>
    
    <p v-if="isVisible" class="message show">I love Programming</p>
    <p v-show="isVisible" class="message show">v-show</p>
  </div>
</template>

<script>
export default {
  name: "ToggleVisibility",
  data() {
    return {
      isVisible: false,
    };
  },
  methods: {
    toggleVisibility() {
      this.isVisible = !this.isVisible;
    },
  },
};
</script>

<style scoped>
.toggle-container {
  background-color: #e0f7fa; 
  padding: 20px;
  border-radius: 8px;
  text-align: center;
  margin: 20px auto;
  width: 300px; 
  box-shadow: 0 4px 6px rgb(0, 0, 0, 0.1); 
}

/* Button styling */
button {
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  background-color: #3e9c90;
  color: #fff;
  border: 2px solid #217065;
  border-radius: 5px;
  transition: background-color 0.3s, transform 0.2s ease-in-out;
}

button:hover {
  background-color: #217065;
  transform: scale(1.05); 
}

.message {
  font-size: 18px;
  color: #004d40;
  margin: 10px 0;
  opacity: 1;
  transition: opacity 0.3s ease-in-out;
}

/* Optional: Styling for hidden messages */
.message.show {
  visibility: visible;
  opacity: 1;
}

/* If using v-if, ensure there's a smooth transition when hidden */
.message:not(.show) {
  visibility: hidden;
  opacity: 0;
}
</style>
