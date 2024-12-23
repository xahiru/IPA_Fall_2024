<template>
  <div>
    <h2>Welcome to the Greenhouse Dashboard</h2>
    <button @click="goToLogin">Login</button>
    <button @click="goToRegister">Register</button>
  </div>
</template>

<script>
export default {
  methods: {
    goToLogin() {
      this.$router.push('/login');
    },
    goToRegister() {
      this.$router.push('/register');
    },
  },
};
</script>
