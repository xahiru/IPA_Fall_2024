<template>
  <div id="app">
    <h1>Vue 3 Event Propagation Demo</h1>
    <EventDemo />
  </div>
</template>

<script>
import EventDemo from './components/EventDemo.vue';

export default {
  name: 'App',
  components: {
    EventDemo
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