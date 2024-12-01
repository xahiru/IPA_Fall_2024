<template>
  <div @click="handleDivClick">
    <button @click.stop="handleButtonClick">Click here to continue👆</button>
  </div>
</template>

<script>
export default {
  name: 'EventDemo',
  methods: {
    handleDivClick() {
      alert('You clicked the div!');
    },
    handleButtonClick(event) {
      event.stopPropagation();  
    }
  }
};
</script>

<style scoped>
div {
  padding: 30px;
  background-color: rgb(103, 176, 192);
  text-align: center;
  border: 2px solid #776ce9;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgb(0, 0, 0, 0.2);
  transition: background-color 0.3s ease; 
}

div:hover {
  background-color: rgb(129, 194, 206); 
}

button {
  padding: 12px 25px;
  background-color: #274b28;
  color: #a2e0df;
  border: none;
  cursor: pointer;
  border-radius: 5px;
  font-size: 16px;
  transition: background-color 0.3s ease, transform 0.2s ease; 
}

button:hover {
  background-color: #e444c4;
  transform: scale(1.1); 
}

button:active {
  transform: scale(1); 
}

button:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(255, 255, 255, 0.7); 
}
</style>
