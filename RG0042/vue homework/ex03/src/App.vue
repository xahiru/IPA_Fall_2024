<template>
  <div id="app">
    <h1>Welcome to the Vue 3 Expression Demo</h1>
  
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

<style scoped>
#app {
  text-align: center;
  margin-top: 50px;
}

h1 {
  font-size: 2em;
  color: #42b983;
}
</style>