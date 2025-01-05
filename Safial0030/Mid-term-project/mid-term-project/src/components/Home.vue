<!-- eslint-disable vue/multi-word-component-names -->
<!-- eslint-disable vue/multi-word-component-names -->
<!-- eslint-disable vue/multi-word-component-names -->
<!-- eslint-disable vue/multi-word-component-names -->
<!-- eslint-disable vue/multi-word-component-names -->
<!-- eslint-disable vue/multi-word-component-names -->
// eslint-disable-next-line vue/multi-word-component-names
<template>
  <div class="home-container">
    <h1 class="card-up">Welcome to Safial's Greenhouse Monitoring System(SGM)</h1>
    <div class="row justify-content-center">
      <div class="col-md-8">
        <h3 class="card-down">
          This system allows you to monitor your greenhouse environment and receive alerts when conditions deviate from your desired thresholds.
        </h3>
        <div class="row mt-4">
          <div class="col-md-6">
            <div class="card shadow">
              <div class="card-body text-center">
                <h5 class="let">Get Started</h5>
                <p class="let">
                  To begin, register for an account and access the dashboard to view real-time data.
                </p>
                <router-link to="/register" class="btn btn-primary">Register</router-link>
              </div>
            </div>
          </div>
          <div class="col-md-6">
            <div class="card shadow">
              <div class="card-body text-center">
                <h5 class="let">Already a User?</h5>
                <p class="let">
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
  background-image: url('@/assets/Home.jpg'); /* Path to your image */
  background-size: cover; /* Makes the background cover the entire container */
  background-position: right; /* Centers the image */
  min-height: 100vh; /* Sets the minimum height to fill the viewport */
  color: #dbdb0d; /* Change text color if necessary for contrast */
  padding: 20px; /* Adds padding around the content */
}

.card {
  border-radius: 10px;
  background-color: #11637cb7;

}
.card-up {
  background-color: #000000bd; /* background for card */
  border-radius: 10px;
  display: flex;
  justify-content: center;
  align-items: center;

}
.card-down {
  background-color: #0b81a5fa; /* background for card */
  border-radius: 10px;
  color: #ffffff;
  
  }
  .let{
    color: #11ff0d;
  }
</style>