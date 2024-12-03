<!-- eslint-disable vue/multi-word-component-names -->
// eslint-disable-next-line vue/multi-word-component-names
<template>
 <div class="background-image">
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <div class="card shadow mt-5">
          <div class="card-header text-center">
            <h3>Register To SGM</h3>
          </div>
          <div class="card-body">
            <form @submit.prevent="register">
              <div class="mb-3">
                <label for="email" class="btn2">Email</label>
                <input
                  v-model="email"
                  type="email"
                  id="email"
                  class="form-control"
                  placeholder="Enter your email"
                  required
                />
              </div>
              <div class="mb-3">
                <label for="password" class="btn2">Password</label>
                <input
                  v-model="password"
                  type="password"
                  id="password"
                  class="form-control"
                  placeholder="Create a password"
                  required
                />
              </div>
              <div class="mb-3">
                <label for="confirmPassword" class="btn2">Confirm Password</label>
                <input
                  v-model="confirmPassword"
                  type="password"
                  id="confirmPassword"
                  class="form-control"
                  placeholder="Confirm your password"
                  required
                />
              </div>
              <button type="submit" class="btn btn-primary w-100">Register</button>
            </form>
            <div class="btn2">
              <p>Already have an account? <router-link class="btn1" to="/login">Login here</router-link></p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  data() {
    return {
      email: '',
      password: '',
      confirmPassword: '',
    };
  },
  methods: {
    register() {
      // Basic validation before submission
      if (this.password !== this.confirmPassword) {
        alert("Passwords do not match!");
        return;
      }

      // Simulate registration process
      console.log('Registration successful for:', this.email);
      this.$router.push('/login'); // Redirect to login after registration
    },
  },
};
</script>

<style scoped>
.card {
  border-radius: 1rem;
  background-color: rgba(4, 168, 4, 0.633) ;
  width: 600px;
}

.card-header {
  background-color: #007bff;
  color: white;
}

.btn-primary {
  background-color: #007bff;
  border-color: #007bff;
}

.btn-primary:hover {
  background-color: #065006;
  border-color: #0056b3;
}
.btn1{
  color: #f4dc02;
}

.btn2{
  color: #ffffff;
}
</style>
<style scoped>
.background-image {
  background-image: url('/src/assets/R.jpg');
  background-size: cover;
  background-position: right;
  min-height: 100vh; /* Sets the minimum height to fill the viewport */
  min-height: 100vh;
}
</style>