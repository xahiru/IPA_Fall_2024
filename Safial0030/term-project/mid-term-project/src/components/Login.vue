<!-- eslint-disable vue/multi-word-component-names -->
// eslint-disable-next-line vue/multi-word-component-names  
<template>
  <div class="container mt-5">
    <h1 class="text-center mb-4">Welcome to Greenhouse Monitoring System</h1></div>
  <div class="container d-flex align-items-center justify-content-center" style="height: 100vh;">
    <div class="card shadow-lg p-4" style="width: 400px;">
      <h2 class="text-center mb-4">Login</h2>
      <form @submit.prevent="login">
        <div class="mb-3">
          <label for="email" class="form-label">Email</label>
          <input
            v-model="email"
            type="email"
            class="form-control"
            id="email"
            placeholder="Enter your email"
            required
          />
        </div>
        <div class="mb-3">
          <label for="password" class="form-label">Password</label>
          <input
            v-model="password"
            type="password"
            class="form-control"
            id="password"
            placeholder="Enter your password"
            required
          />
        </div>
        <button type="submit" class="btn btn-primary w-100">Login</button>
        <p class="text-center mt-3">
          <router-link to="/register" class="text-decoration-none">Don't have an account? Register</router-link>
        </p>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: '',
      password: ''
    };
  },
  methods: {
    login() {
      localStorage.setItem('token', 'dummy_token'); // Simulating login
      this.$router.push('/dashboard'); // Redirect to dashboard after login
    }
  }
};
</script>

<style scoped>
.card {
  border-radius: 10px; /* Rounded corners for the card */
}

.card h2 {
  color: #007bff; /* Primary color for the heading */
}

.btn-primary {
  background-color: #007bff; /* Primary button color */
  border: none; /* Remove border */
}

.btn-primary:hover {
  background-color: #0056b3; /* Darker shade on hover */
}

.text-center a {
  color: #007bff; /* Primary color for links */
}

.text-center a:hover {
  text-decoration: underline; /* Underline on hover */
}
</style>
<style scoped>
.login-container {
  background-image: url('@/assets/2.jpg.jpg'); /* Path to your image */
  background-size: cover; /* Makes the background cover the entire container */
  background-position: center; /* Centers the image */
  min-height: 100vh; /* Sets the minimum height to fill the viewport */
  color: white; /* Change text color if necessary for contrast */
  padding: 20px; /* Adds padding around the content */
}

.card {
  border-radius: 10px;
}
</style>