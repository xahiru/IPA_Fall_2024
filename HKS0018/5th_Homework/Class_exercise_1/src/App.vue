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
  background:rgb(241, 243, 207);
}
#app {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 100;
  font-family: Arial, sans-serif;
}
</style>
