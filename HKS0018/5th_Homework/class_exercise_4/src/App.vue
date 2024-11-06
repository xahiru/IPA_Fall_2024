<template>
  <div id="app">
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
body{
  background: white;
}
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
