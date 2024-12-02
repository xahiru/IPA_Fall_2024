<script setup>
const handleClick = () => {
  alert('Button clicked!');
};
const handleDevClick = () => {
  alert('Dev clicked!');
};
</script>

<template>
  <div>
    <h2>Event Modifiers: Stop Propagation</h2>
    <div @click="handleDevClick" style="border: 2px solid #ccc; padding: 20px;">
      <button @click.stop="handleClick">Click me without triggering div click</button>
    </div>
  </div>
</template>

<style scoped>
div {
  margin: 20px 0;
}

button {
  background-color: #42b983;
  color: white;
  padding: 5px 10px;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}
</style>
