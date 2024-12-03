<template>
    <div>
      <button @click="toggleVisibility">
        See me
      </button>
  
      <p v-if="isVisible">I love Programming</p>
  
      <p v-show="isVisible">v-show</p>
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
/* Styling for the container */
.toggle-container {
  background-color: #e0f7fa; /* Light cyan background color */
  padding: 20px;
  border-radius: 8px;
  text-align: center;
  margin: 10px 0;
}

button {
  margin-bottom: 15px;
  padding: 8px 16px;
  font-size: 16px;
  cursor: pointer;
  background-color: #3e9c90; 
  color: rgb(199, 192, 208);
  border: 15px;
  border-color: rgb(219, 14, 14);
  border-radius: 10px;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #217065; 
}

.message {
  font-size: 18px;
  color: #004d40; 
  margin: 5px 0;
}
</style>