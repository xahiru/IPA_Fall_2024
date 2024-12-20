<template>
    <div>
      <h2>Conditional Rendering with v-if and v-show</h2>
      <button @click="toggleVisibility">Toggle Visibility</button>
      <p v-if="isVisible">This is visible when using v-if</p>
      <p v-show="isVisible">This is visible when using v-show</p>
    </div>
  </template>
  
  <script>
  export default {
    name: "ToggleVisibility",
    data() {
      return {
        isVisible: true,
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
  button {
    padding: 10px 20px;
    font-size: 16px;
    margin-bottom: 20px;
    cursor: pointer;
  }
  
  p {
    font-size: 18px;
    color: #898989;
  }
  </style>  