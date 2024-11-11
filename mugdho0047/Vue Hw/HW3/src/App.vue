<template>
  <div id="app">
    <h1>Vue 3 JavaScript Expressions Demo</h1>
    <ExpressionDemo />
  </div>
</template>

<script>
import ExpressionDemo from './components/ExpressionDemo.vue';

export default {
  name: 'App',
  components: {
    ExpressionDemo
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

h1 {
  font-size: 2em;
  margin-bottom: 20px;
}
</style>
