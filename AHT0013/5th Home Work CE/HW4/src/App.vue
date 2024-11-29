<template>
  <div id="app">
    <h1>Vue 3 Conditional Rendering Example</h1>
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
  color: #0a5198;
  margin-top: 60px;
}
</style>