<template>
  <div>
    <h2>Login</h2>

    <form @submit.prevent="handleSubmit">
      <div>
        <label for="username">Username:</label>
        <input
          type="text"
          id="username"
          v-model="username"
          placeholder="Enter your username"
          required
        />
        <p v-if="username && username.length < 3" class="error">Username must be at least 3 characters long.</p>
      </div>

      <div>
        <label for="password">Password:</label>
        <input
          type="password"
          id="password"
          v-model="password"
          placeholder="Enter your password"
          required
        />
        <p v-if="password && password.length < 6" class="error">Password must be at least 6 characters long.</p>
      </div>

      <button type="submit" :disabled="isLoading">Submit</button>
    </form>

    <p v-if="submittedUsername">Welcome, {{ submittedUsername }}!</p>
    <p v-if="isLoading">Logging in...</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
      submittedUsername: null,
      isLoading: false,
    };
  },
  methods: {
    handleSubmit() {
      if (this.username.length < 3) {
        alert('Username must be at least 3 characters long.');
        return;
      }
      if (this.password.length < 6) {
        alert('Password must be at least 6 characters long.');
        return;
      }

      this.isLoading = true;

      setTimeout(() => {
        this.submittedUsername = this.username;
        alert(`Welcome, ${this.username}!`);
        
        this.username = '';
        this.password = '';
        this.isLoading = false;
      }, 2000);
    }
  }
};
</script>

<style scoped>
form {
  max-width: 300px;
  margin: 0 auto;
}
input {
  width: 100%;
  padding: 8px;
  margin: 8px 0;
}
button {
  padding: 10px 15px;
  background-color: #007BFF;
  color: white;
  border: none;
  cursor: pointer;
}
button:disabled {
  background-color: #c0c0c0;
  cursor: not-allowed;
}
button:hover:not(:disabled) {
  background-color: #0056b3;
}
.error {
  color: red;
  font-size: 12px;
}
</style>
