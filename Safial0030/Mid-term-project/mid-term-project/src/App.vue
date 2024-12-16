<template>
  <div id="app">
    <Navbar v-if="showNavbar" :bgColor="'green'" />
    <router-view />
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue';

export default {
  name: 'App',
  components: {
    Navbar,
  },
  computed: {
    showNavbar() {
      const isAuthenticated = localStorage.getItem('token');
      return (
        (this.$route.path === '/dashboard' ||
          this.$route.path === '/settings' ||
          this.$route.path === '/temperature-chart') &&
        isAuthenticated
      );
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  margin-top: 0px;
}
</style>