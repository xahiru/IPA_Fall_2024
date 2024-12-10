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
      alert('Div clicked!');
    },
    handleButtonClick() {
      alert('Button clicked!');
    }
  }
};
</script>

<style scoped>
div {
  padding: 20px;
  background-color: rgb(103, 176, 192) ;
  text-align: center;
  border: 2px solid #776ce9;
}

button {
  padding: 10px 20px;
  background-color: #274b28;
  color: #a2e0df;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: #e444c4;
  color: rgb(11, 121, 161);
  }

</style>
