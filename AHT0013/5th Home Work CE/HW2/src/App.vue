<template>
  <div id="app">
    <h1>Event Propagation Demo</h1>
    <EventDemo />
  </div>
</template>

<script>
import EventDemo from './components/EventDemo.vue';

export default {
  name: 'App',
  components: {
    EventDemo,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #0064c8;
  margin-top: 60px;
}
</style>