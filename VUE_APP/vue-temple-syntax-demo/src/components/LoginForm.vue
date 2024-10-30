<script setup>
import { ref } from 'vue';

const username = ref('');
const password = ref('');
const submittedUsername = ref('');

const handleSubmit = () => {
  submittedUsername.value = username.value;
  alert(`Welcome, ${submittedUsername.value}!`);
};
</script>

<template>
  <div>
    <h2>Login Form</h2>
    <form @submit.prevent="handleSubmit">
      <div>
        <label for="username">Username:</label>
        <input id="username" v-model="username" type="text" placeholder="Enter your username" />
      </div>
      <div>
        <label for="password">Password:</label>
        <input id="password" v-model="password" type="password" placeholder="Enter your password" />
      </div>
      <button type="submit">Submit</button>
    </form>
    <p v-if="submittedUsername">Welcome, {{ submittedUsername }}!</p>
  </div>
</template>

<style scoped>
form {
  margin: 20px 0;
}

input {
  margin: 5px;
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
