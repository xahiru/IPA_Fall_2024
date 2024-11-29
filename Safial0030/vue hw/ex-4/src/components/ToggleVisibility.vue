<template>
    <div class="toggle-visibility">
      <h2>Toggle Visibility Demo</h2>
      <button @click="toggleVisibility">{{ isVisible ? 'Hide' : 'Show' }} Messages</button>
  
      <div v-if="isVisible">
        <p>This is visible when using v-if</p >
      </div>
  
      <div v-show="isVisible">
        <p>This is visible when using v-show</p >
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ToggleVisibility',
    data() {
      return {
        isVisible: false, // Initially set to false
      };
    },
    methods: {
      toggleVisibility() {
        this.isVisible = !this.isVisible; // Toggle the visibility
      },
    },
  };
  </script>
  
  <style scoped>
  .toggle-visibility {
    max-width: 400px;
    margin: auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    text-align: center;
  }
  
  button {
    padding: 10px 20px;
    margin-bottom: 20px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #0056b3;
  }
  
  p {
    margin: 10px 0;
  }
  </style>