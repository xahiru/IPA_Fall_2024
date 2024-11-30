<template>
  <div class="login-container">
    <!-- Back Button -->
    <router-link to="/" class="back-btn">← Back to Home</router-link>

    <h2>Login</h2>
    <form @submit.prevent="submitLogin">
      <div class="form-group">
        <label for="email">Email</label>
        <input v-model="email" type="email" id="email" required />
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input v-model="password" type="password" id="password" required />
      </div>
      <button type="submit" class="btn login-btn">Login</button>
    </form>

    <div class="register-link">
      <p>Don't have an account?</p>
      <router-link to="/register" class="btn register-btn">Register</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UserLogin',
  data() {
    return {
      email: '',
      password: '',
    };
  },
  methods: {
    submitLogin() {
      // Simulate login logic
      console.log('Logging in with', this.email, this.password);
      // Redirect to Dashboard
      this.$router.push({ name: 'Dashboard' });
    },
  },
};
</script>

<style scoped>
/* Styles for UserLogin */
.login-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-color: #f4f7fc;
  font-family: 'Roboto', sans-serif;
}

h2 {
  font-size: 2rem;
  color: #4e2a84; /* Dark purple */
  margin-bottom: 20px;
}

form {
  max-width: 400px;
  width: 100%;
  padding: 20px;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  font-size: 1rem;
  margin-bottom: 5px;
}

input {
  width: 100%;
  padding: 10px;
  font-size: 1rem;
  border-radius: 5px;
  border: 1px solid #ddd;
  box-sizing: border-box;
}

button {
  width: 100%;
  padding: 12px;
  font-size: 1.2rem;
  font-weight: 600;
  border: none;
  border-radius: 50px;
  background-color: #4caf50; /* Green color */
  color: white;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #45a049;
}

.register-link {
  margin-top: 20px;
  text-align: center;
}

.register-link p {
  font-size: 1rem;
  color: #333;
}

.register-btn {
  display: inline-block;
  margin-top: 10px;
  padding: 12px 30px;
  font-size: 1.1rem;
  font-weight: 600;
  background-color: #ff5733; /* Orange color */
  color: white;
  text-decoration: none;
  border-radius: 50px;
  transition: background-color 0.3s ease;
}

.register-btn:hover {
  background-color: #ff4023;
}

/* Back Button Styling */
.back-btn {
  margin-top: 20px;
  font-size: 1rem;
  color: #4caf50;
  text-decoration: none;
  font-weight: 600;
  transition: color 0.3s ease;
}

.back-btn:hover {
  color: #45a049;
}
</style>
