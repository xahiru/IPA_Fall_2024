<template>
  <div id="app">
    <h1>Vue 3 Application</h1>
   
    <LoginForm />
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

#app {
  text-align: center;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  font-size: 16px;
  color: #2c3e50;
  margin-top: 60px;
}

h1 {
  color: #42b983;
}
</style>
