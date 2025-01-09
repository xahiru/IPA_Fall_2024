<template>
  <div>
    <h2>Register</h2>
    <form @submit.prevent="handleRegister">
      <label for="username">Username:</label>
      <input type="text" v-model="username" required />

      <label for="password">Password:</label>
      <input type="password" v-model="password" required />

      <button type="submit">Register</button>
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
    handleRegister() {
      alert(`Registered with username: ${this.username}`);
      this.$router.push('/login');
    },
  },
};
</script>
