<template>
    <div class="toggle-visibility">
      <button @click="toggleVisibility">Toggle Visibility</button>
      <div v-if="isVisible">
        <p>This is visible when using v-if</p>
      </div>
      <div v-show="isVisible">
        <p>This is visible when using v-show</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        isVisible: false
      };
    },
    methods: {
      toggleVisibility() {
        // Toggle the isVisible variable between true and false
        this.isVisible = !this.isVisible;
      }
    }
  };
  </script>
  
  <style scoped>
  .toggle-visibility {
    max-width: 400px;
    margin: auto;
    padding: 20px;
    text-align: center;
    border: 1px solid #ccc;
    border-radius: 8px;
  }
  
  button {
    padding: 10px 20px;
    margin-bottom: 20px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #0056b3;
  }
  
  p {
    font-size: 1.2em;
    margin-top: 10px;
  }
  </style>  