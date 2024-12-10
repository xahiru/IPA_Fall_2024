<template>
  <div id="app">
    <h1>Toggle Visibility</h1>
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
  text-align: center;
  margin-top: 40px;
  background-color: #f0f4f8;
  padding: 20px;
  border-radius: 8px;
}

</style>