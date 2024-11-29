<template>
  <div>
    <h2>Login Form</h2>
    <form @submit.prevent="submitForm">
      <label for="username">Username:</label>
      <input type="text" id="username" v-model="username" required />

      <label for="password">Password:</label>
      <input type="password" id="password" v-model="password" required />

      <button type="submit">Submit</button>
    </form>

    <p v-if="welcomeMessage">Welcome, {{ welcomeMessage }}!</p>
  </div>
</template>

<script>
export default {
  name: 'LoginForm',
  data() {
    return {
      username: '',
      password: '',
      welcomeMessage: ''
    };
  },
  methods: {
    submitForm() {
      this.welcomeMessage = this.username;
      alert(Welcome, ${this.username}!);
    }
  }
};
</script> humanzize
