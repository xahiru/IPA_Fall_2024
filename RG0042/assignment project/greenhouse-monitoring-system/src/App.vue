<template>
  <div id="app">
    <nav>
      <router-link to="/" class="nav-link">Home</router-link>
      <router-link to="/loginPage" class="nav-link">login</router-link>
      <router-link to="/signuppage" class="nav-link">Sign Up</router-link>

      <button v-if="isAuthenticated" @click="logout" class="nav-link logout-btn">logout</button>
    </nav>

    <main>
      <router-view></router-view>
    </main>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      isAuthenticated: false,
    };
  },

  created() {
    this.checkAutj();
  },

  methods: {
    checkAuth() {
      // check local storage to see if user is authenticated
      this.isAuthenticated = !!localStorage.getItem("auth");
    },
    logout() {
      localStorage.removeItem("auth");
      this.isAuthenticated = false;
      this.$router.push("/login");  //redirect to login page
    },
  },

  watch: {
    // watch route change and update authenticated status
    $router() {
      this.checkAuth();
    }
  }
};
</script>


<style scoped>
#app {
  font-family: Arial, Helvetica, sans-serif;
  text-align: center;
  color: darkviolet;
}

nav {
  display: flex;
  justify-content: center;
  padding: 15px;
  background-color: blueviolet;
}


.nav-link {
  margin: 0 10px;
  color: white;
  text-decoration: none;
  font-weight: bold;
}

.nav-link:hover {
  text-decoration: underline;
}

.logout-btn {
  background: none;
  border: none;
  color: white;
  font-weight: bold;
  cursor: pointer;
}

main {
  padding: 20px;
}
</style>