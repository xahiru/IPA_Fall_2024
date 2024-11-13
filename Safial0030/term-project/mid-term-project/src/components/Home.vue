<!-- eslint-disable vue/multi-word-component-names -->
<!-- eslint-disable vue/multi-word-component-names -->
<!-- eslint-disable vue/multi-word-component-names -->
<!-- eslint-disable vue/multi-word-component-names -->
<!-- eslint-disable vue/multi-word-component-names -->
<!-- eslint-disable vue/multi-word-component-names -->
// eslint-disable-next-line vue/multi-word-component-names
<template>
  <div class="home-container">
    <h1 class="text-center mb-4">Welcome to Greenhouse Monitoring System</h1>
    <div class="row justify-content-center">
      <div class="col-md-8">
        <h3 class="text-center mb-5">
          This system allows you to monitor your greenhouse environment and receive alerts when conditions deviate from your desired thresholds.
        </h3>
        <div class="row mt-4">
          <div class="col-md-6">
            <div class="card shadow">
              <div class="card-body text-center">
                <h5 class="card-title">Get Started</h5>
                <p class="card-text">
                  To begin, register for an account and access the dashboard to view real-time data.
                </p>
                <router-link to="/register" class="btn btn-primary">Register</router-link>
              </div>
            </div>
          </div>
          <div class="col-md-6">
            <div class="card shadow">
              <div class="card-body text-center">
                <h5 class="card-title">Already a User?</h5>
                <p class="card-text">
                  Log in to your account to view data and manage your settings and access the dashboard to view real-time data.
                </p>
                <router-link to="/login" class="btn btn-primary">Login</router-link>
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
  name: 'HomePage',
};
</script>

<style scoped>
.home-container {
  background-image: url('@/assets/2.jpg.jpg'); /* Path to your image */
  background-size: cover; /* Makes the background cover the entire container */
  background-position: right; /* Centers the image */
  min-height: 100vh; /* Sets the minimum height to fill the viewport */
  color: #120542; /* Change text color if necessary for contrast */
  padding: 20px; /* Adds padding around the content */
}

.card {
  border-radius: 10px;
}
</style>