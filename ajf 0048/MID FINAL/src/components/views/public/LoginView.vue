<template>
    <v-container fluid class="login-container">
      <v-row justify="center" align="center" style="height: 100vh;">
        <v-col cols="12" sm="8" md="6" lg="4">
        <v-card class="login-card">
          <v-card-title class="text-center">
            <h2 class="gradient-text">Welcome Back</h2>
          </v-card-title>
            
            <v-card-text class="pa-6">
              <v-form @submit.prevent="login" v-model="valid">
                <v-text-field
                  v-model="email"
                  label="Email"
                  prepend-inner-icon="mdi-email"
                  type="email"
                  required
                  :rules="emailRules"
                  class="mb-4"
                  variant="outlined"
                ></v-text-field>
  
                <v-text-field
                  v-model="password"
                  label="Password"
                  prepend-inner-icon="mdi-lock"
                  :type="showPassword ? 'text' : 'password'"
                  required
                  :rules="passwordRules"
                  :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                  @click:append="showPassword = !showPassword"
                  class="mb-6"
                  variant="outlined"
                ></v-text-field>
  
                <v-btn
                  type="submit"
                  color="primary"
                  block
                  size="large"
                  :loading="loading"
                  class="mt-6 login-btn"
                >
                  Login
                </v-btn>
              </v-form>
            </v-card-text>
  

            <v-card-text class="text-center pb-6">
              <router-link to="/register" class="text-decoration-none">
                Don't have an account? Register here
              </router-link>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  
  const router = useRouter()
  const valid = ref(false)
  const loading = ref(false)
  const showPassword = ref(false)
  const email = ref('')
  const password = ref('')
  
  const emailRules = [
    v => !!v || 'Email is required',
    v => /.+@.+\..+/.test(v) || 'Email must be valid'
  ]
  
  const passwordRules = [
    v => !!v || 'Password is required',
    v => v.length >= 6 || 'Password must be at least 6 characters'
  ]

    const login = () => {
  // Simple hardcoded credentials for demonstration
  if (email.value && password.value) {
    // Set token for authentication
    localStorage.setItem('token', 'logged-in-' + Date.now())
    router.push('/dashboard')
  } else {
    alert('Invalid credentials')
  }
}
  </script>

  <style scoped>
  .login-page {
  background-size: cover;
  background-position: center;
  min-height: 100vh;
}

.login-container {
  background: linear-gradient(135deg, rgba(255,255,255,0.1), rgba(255,255,255,0.2));
  backdrop-filter: blur(10px);
  background: var(--gradient-primary);
}

.login-card {
  background: rgba(255, 255, 255, 0.15) !important;
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  padding: 20px;
}

.gradient-text {
  background: linear-gradient(45deg, #FC466B, #3F5EFB);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  font-weight: bold;
}

.login-btn {
  transition: transform 0.3s ease;
}

.login-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 16px rgba(0,0,0,0.2);
}
  </style>