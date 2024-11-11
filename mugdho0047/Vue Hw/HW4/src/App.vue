<template>
  <div id="app">
    <h1>Vue 3 Conditional Rendering Demo</h1>
    <ToggleVisibility />
  </div>
</template>

<script>
import ToggleVisibility from './components/ToggleVisibility.vue';

export default {
  name: 'App',
  components: {
    ToggleVisibility
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