<template>
    <div>
      <button @click="toggleVisibility">Toggle Visibility</button>
  

      <p v-if="isVisible">This is visible when using v-if</p>
  

      <p v-show="isVisible">This is visible when using v-show</p>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ToggleVisibility',
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
  </style>
  