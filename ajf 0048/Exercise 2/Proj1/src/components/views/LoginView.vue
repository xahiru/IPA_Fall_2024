<template>
    <v-container fluid class="fill-height bg-grey-lighten-4">
      <v-row align="center" justify="center">
        <v-col cols="12" sm="8" md="6" lg="4">
          <v-card class="elevation-12">
            <v-card-title class="text-h4 text-center pt-6">
              <v-icon size="36" color="primary" class="mr-2">mdi-login</v-icon>
              Login
            </v-card-title>
            
            <v-card-text class="pa-6">
              <v-form @submit.prevent="handleLogin" v-model="valid">
                <v-text-field
                  v-model="email"
                  label="Email"
                  prepend-inner-icon="mdi-email"
                  type="email"
                  required
                  :rules="emailRules"
                  class="mb-4"
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
                ></v-text-field>
  
                <v-btn
                  type="submit"
                  color="primary"
                  block
                  size="large"
                  :loading="loading"
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
  
  const handleLogin = async () => {
    if (!valid.value) return
    
    loading.value = true
    setTimeout(() => {
      loading.value = false
      router.push('/dashboard')
    }, 1000)
  }
  </script>