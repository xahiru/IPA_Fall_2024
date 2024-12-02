<template>
  <v-container fluid class="home-container">
    <!-- Hero Section -->
    <v-row class="hero-section" align="center">
      <v-col cols="12" md="6">
        <h1 class="hero-title">Greenhouse Management</h1>
        <p class="hero-subtitle">Monitor and control your greenhouse environment with precision</p >
        <v-btn
          color="primary"
          size="large"
          class="get-started-btn mt-4"
          @click="$router.push('/register')"
        >
          Get Started
          <v-icon right>mdi-arrow-right</v-icon>
        </v-btn>
      </v-col>
      <v-col cols="12" md="6" class="text-center">
        <v-img src="@/assets/greenhouse.png" class="hero-image" />
      </v-col>
    </v-row>

    <!-- Features Section -->
    <v-row class="features-section mt-6">
      <v-col cols="12" class="text-center mb-4">
        <h2 class="section-title">Key Features</h2>
      </v-col>
    </v-row>

    <!-- Benefits Section -->
    <v-row class="benefits-section mt-6">
      <v-col cols="12" class="text-center mb-8">
        <h2 class="section-title">Why Choose Us</h2>
      </v-col>
      <v-col cols="12" md="4" v-for="benefit in benefits" :key="benefit.title">
        <div class="benefit-item">
          <v-icon size="36" color="primary">{{ benefit.icon }}</v-icon>
          <h3 class="benefit-title">{{ benefit.title }}</h3>
          <p class="benefit-text">{{ benefit.text }}</p >
        </div>
      </v-col>
    </v-row>

    <!-- Call to Action -->
    <v-row class="cta-section mt-16">
      <v-col cols="12" class="text-center">
        <v-card class="cta-card">
          <h2 class="cta-title">Ready to optimize your greenhouse?</h2>
          <p class="cta-text">Join thousands of successful greenhouse owners</p >
          <v-btn
            color="primary"
            size="large"
            class="mt-4"
            @click="$router.push('/register')"
          >
            Start Now
          </v-btn>
        </v-card>
      </v-col>
    </v-row>
    <!-- Footer Section -->
     <v-row class="mt-16">
       <v-col cols="12" class="text-center">
         <v-divider class="mb-6"></v-divider>
         <div class="text-body-2 text-black">
          <v-icon small class="mr-2">mdi-leaf</v-icon>
          Greenhouse Monitor System
          <v-icon small class="mx-2">mdi-circle-small</v-icon>
          {{ new Date().getFullYear() }}
        </div>
      </v-col>
    </v-row>

  </v-container>
</template>

<script setup>
import { ref } from 'vue'

const demoData = ref([23, 45, 30, 52, 38, 46, 29])
const demoControl = ref(60)
const demoAlerts = ref([
  { id: 1, text: 'Temperature Alert', color: 'error' },
  { id: 2, text: 'Humidity Optimal', color: 'success' },
  { id: 3, text: 'Water Level Low', color: 'warning' }
])

const benefits = ref([
  {
    icon: 'mdi-chart-timeline-variant',
    title: 'Data-Driven Insights',
    text: 'Make informed decisions with comprehensive analytics and reporting'
  },
  {
    icon: 'mdi-shield-check',
    title: 'Reliable Monitoring',
    text: '24/7 automated monitoring ensures your greenhouse is always protected'
  },
  {
    icon: 'mdi-leaf',
    title: 'Optimal Growth',
    text: 'Maintain perfect growing conditions for maximum yield'
  }
])
</script>

<style scoped>
.home-container {
  padding: 16px;
  height: 100vh;
  display: flex;
  flex-direction: column;
}

.hero-section {
  height: 40vh;
  padding: 16px 0;
}

.hero-title {
  font-size: 3.5rem;
  font-weight: bold;
  background: linear-gradient(45deg, #FC466B, #3F5EFB);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  line-height: 1.2;
}

.hero-subtitle {
  font-size: 1.2rem;
  color: rgba(255, 255, 255, 0.8);
  margin-top: 8px;
}

.hero-image {
  max-width: 80%;
  margin: 0 auto;
  animation: float 6s ease-in-out infinite;
}

.section-title {
  font-size: 2rem;
  font-weight: bold;
  background: linear-gradient(45deg, #FC466B, #3F5EFB);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 20px;
}

.features-section {
  margin-top: 20px;
  padding-top: 0;
}

.feature-card {
  padding: 16px;
}

.feature-title {
  font-size: 1.2rem;
  margin-bottom: 8px;
}

.benefits-section {
  margin-top: 20px;
}

.mt-16 {
  margin-top: 1rem !important;
}

.mb-8 {
  margin-bottom: 1rem !important;
}

.benefit-item {
  text-align: center;
  padding-top: 0;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(12px);
  border-radius: 16px;
  transition: transform 0.3s ease;
}

.benefit-item:hover {
  transform: translateY(-5px);
}

.benefit-title {
  font-size: 1.5rem;
  margin: 16px 0;
  color: rgba(255, 255, 255, 0.9);
}

.benefit-text {
  color: rgba(255, 255, 255, 0.7);
}

.cta-card {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(12px);
  padding: 24px;
  border-radius: 24px;
  text-align: center;
}

.cta-section {
  margin-top: 20px;
}

.cta-title {
  font-size: 2rem;
  color: rgba(255, 255, 255, 0.9);
  margin-bottom: 16px;
}

.cta-text {
  color: rgba(255, 255, 255, 0.7);
  font-size: 1.2rem;
}

@keyframes float {
  0% { transform: translateY(0px); }
  50% { transform: translateY(-20px); }
  100% { transform: translateY(0px); }
}

</style>