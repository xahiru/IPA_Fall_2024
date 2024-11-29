<template>
  <div>
    <h2>Event Handling Demo</h2>

    <div @click="handleDivClick">
      <p>Click anywhere inside the div, but outside the button, to trigger the div's click event.</p>
      <button @click.stop="handleButtonClick">Click Me (Button)</button>
    </div>
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
