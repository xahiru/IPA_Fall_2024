
<template>
  <div id="app">

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
body{
  background-color: #eee;
}
#app {
  text-align: center;
  margin-top: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 100;
}
</style>
