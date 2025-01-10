<template>
  <div>
    <h2>Login</h2>
    <form @submit.prevent="handleLogin">
      <label for="username">Username:</label>
      <input type="text" v-model="username" required />

      <label for="password">Password:</label>
      <input type="password" v-model="password" required />

      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    handleLogin() {
      if (this.username && this.password) {
        // Simulate a login and store authenticated state in localStorage
        localStorage.setItem('authenticated', true);
        this.$router.push('/dashboard');
      }
    },
  },
};
</script>
