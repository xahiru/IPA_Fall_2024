<template>
  <TheNavigation />
  <the-loader v-if="showLoading"></the-loader>
  <div class="container">
      <div class="row">
          <div class="col-md-12">
              <div>
                  <router-view></router-view>
              </div>
          </div>
      </div>
  </div>
</template>


<script>
import TheNavigation from './components/TheNavigation.vue';
export default {
  name: 'App',
  components: {
    TheNavigation
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #0b2e51;
  margin-top: 60px;
}
</style>
