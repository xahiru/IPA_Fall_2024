<script setup>
import { ref } from 'vue';

// State to store the form input
const inputText = ref('');
const submittedText = ref('');

// Function to handle form submission
const onSubmit = () => {
  submittedText.value = inputText.value;
  alert('Form submitted!');
};

// Function to handle the click event with `.stop` modifier
const handleClick = () => {
  alert('Button clicked!');
};
</script>

<template>
  <div>
    <h2>Event Modifiers Demo</h2>
    <!-- Form with .prevent modifier to prevent default form submission -->
    <form @submit.prevent="onSubmit">
      <label for="inputText">Enter text:</label>
      <input id="inputText" v-model="inputText" type="text" placeholder="Type something..." />
      <button type="submit">Submit</button>
    </form>

    <!-- Show submitted text -->
    <p v-if="submittedText">You submitted: {{ submittedText }}</p>

    <!-- Button with .stop modifier to stop event propagation -->
    <div @click="() => alert('Div clicked!')">
      <button @click.stop="handleClick">Click me without triggering div click</button>
    </div>
  </div>
</template>

<style scoped>
h2 {
  color: #35495e;
}

form {
  margin: 20px 0;
}

input {
  margin-right: 10px;
  padding: 5px;
}

button {
  padding: 5px 10px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}

p {
  color: #42b983;
}
</style>
