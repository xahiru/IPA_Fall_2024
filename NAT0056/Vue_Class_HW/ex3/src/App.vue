<template>
  <div id="app">
    <h1>I Love Math</h1>
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
  text-align: center;
  margin-top: 40px;
}

</style>
