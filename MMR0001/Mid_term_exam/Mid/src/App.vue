<template>
  <div id="app">
    <header class="top-bar">
      <nav class="nav-container">
        <router-link to="/">Home</router-link> 
      </nav>
    </header>

    <main class="content">
      <router-view></router-view>
    </main>
  </div>
</template>

<script>
export default {
  computed: {
    isAuthenticated() {
      return !!localStorage.getItem('authenticated');
    }
  }
};
</script>

<style>
.top-bar {
  width: 100%;
  background-color: #4CAF50; 
  color: white;
  padding: 1em;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
}
.nav-container {
  display: flex;
  justify-content: space-around;
}

.nav-link {
  color: white;
  text-decoration: none;
  font-weight: bold;
}

.nav-link:hover {
  color: #ffd700; 
}

.content {
  padding-top: 4em;
}
</style>
