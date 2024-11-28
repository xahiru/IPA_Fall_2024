<template>
  <div id="app">
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
  text-align: center;
  margin-top: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 100;
}
</style>
