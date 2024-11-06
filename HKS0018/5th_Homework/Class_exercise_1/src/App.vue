<template>
  <div id="app">
    <login-form />
  </div>
</template>

<script>
import LoginForm from './components/LoginForm.vue';

export default {
  name: 'App',
  components: {
    LoginForm
  }
};
</script>

<style>

body{
  background:white;
}
#app {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 100;
  background: linear-gradient(135deg, #4b79a1, #283e51);
  font-family: Arial, sans-serif;
}
</style>
