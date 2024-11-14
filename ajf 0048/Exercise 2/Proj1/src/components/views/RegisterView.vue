<template>
    <v-container fluid class="fill-height bg-grey-lighten-4">
      <v-row align="center" justify="center">
        <v-col cols="12" sm="8" md="6" lg="4">
          <v-card class="elevation-12">
            <v-card-title class="text-h4 text-center pt-6">
              <v-icon size="36" color="primary" class="mr-2">mdi-account-plus</v-icon>
              Register
            </v-card-title>
            
            <v-card-text class="pa-6">
              <v-form @submit.prevent="handleRegister" v-model="valid">
                <v-text-field
                  v-model="name"
                  label="Full Name"
                  prepend-inner-icon="mdi-account"
                  required
                  :rules="nameRules"
                  class="mb-4"
                ></v-text-field>
  
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
                  class="mb-4"
                ></v-text-field>
  
                <v-text-field
                  v-model="confirmPassword"
                  label="Confirm Password"
                  prepend-inner-icon="mdi-lock-check"
                  :type="showPassword ? 'text' : 'password'"
                  required
                  :rules="[...passwordRules, passwordMatch]"
                  class="mb-6"
                ></v-text-field>
  
                <v-btn
                  type="submit"
                  color="primary"
                  block
                  size="large"
                  :loading="loading"
                >
                  Register
                </v-btn>
              </v-form>
            </v-card-text>
  
            <v-card-text class="text-center pb-6">
              <router-link to="/login" class="text-decoration-none">
                Already have an account? Login here
              </router-link>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script setup>
  import { ref, computed } from 'vue'
  import { useRouter } from 'vue-router'
  
  const router = useRouter()
  const valid = ref(false)
  const loading = ref(false)
  const showPassword = ref(false)
  
  const name = ref('')
  const email = ref('')
  const password = ref('')
  const confirmPassword = ref('')
  
  const nameRules = [
    v => !!v || 'Name is required',
    v => v.length >= 3 || 'Name must be at least 3 characters'
  ]
  
  const emailRules = [
    v => !!v || 'Email is required',
    v => /.+@.+\..+/.test(v) || 'Email must be valid'
  ]
  
  const passwordRules = [
    v => !!v || 'Password is required',
    v => v.length >= 6 || 'Password must be at least 6 characters'
  ]
  
  const passwordMatch = computed(() => {
    return () => password.value === confirmPassword.value || 'Passwords must match'
  })
  
  const handleRegister = async () => {
    if (!valid.value) return
    
    loading.value = true
    setTimeout(() => {
      loading.value = false
      router.push('/login')
    }, 1000)
  }
  </script>