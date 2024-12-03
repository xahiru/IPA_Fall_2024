<!-- eslint-disable vue/multi-word-component-names -->
// eslint-disable-next-line vue/multi-word-component-names  
<template>
  <div class="background-image">
  <div class="container d-flex align-items-center justify-content-center" style="height: 100vh;">
    <div class="card shadow-lg p-4" style="width: 400px;">
      <h2 class="text-center mb-4">Login To SGM</h2>
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
.background-image {
  background-image: url('/src/assets/L.jpg');
  background-size: cover;
  background-position: right;
  min-height: 100vh; /* Sets the minimum height to fill the viewport */
  min-height: 100vh;

}

.card {
  border-radius: 10px;
}
</style>