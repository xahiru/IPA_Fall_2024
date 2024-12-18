<template>
    <v-container fluid class="fill-height bg-grey-lighten-4">
      <v-row align="center" justify="center">
        <v-col cols="12" sm="8" md="6" lg="4">
      <v-card class="[login-card]" max-width="400" elevation="8">
        <div class="text-center pt-8">
            <v-icon size="64" color="primary">mdi-greenhouse</v-icon>
          </div>
        <v-card-title class="text-center text-h5">Login</v-card-title>
        <v-card-text>
          <v-card-title class="text-h4 text-center pt-4">
            Welcome Back
          </v-card-title>
          <v-card-subtitle class="text-center pb-4">
            Sign in to manage your greenhouse
          </v-card-subtitle>

          <v-form @submit.prevent="handleLogin" ref="form" >
            <v-text-field
              v-model="email"
               :rules="emailRules"
              label="Email"
              type="email"
              required
              prepend-inner-icon="mdi-email"
                variant="outlined"
                class="mb-4"
            ></v-text-field>
            <v-text-field
              v-model="password"
                :rules="passwordRules"
              label="Password"
              prepend-inner-icon="mdi-lock"
                :append-inner-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                @click:append-inner="showPassword = !showPassword"
                :type="showPassword ? 'text' : 'password'"
                variant="outlined"
                class="mb-6" 
                required
            ></v-text-field>
            <v-btn type="submit" color="primary" block class="mt-4" :loading="loading" >Login</v-btn>
          </v-form>

          <div class="text-center">
              <v-btn variant="text" to="/register" color="primary">
                Create an account
              </v-btn>
            </div>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
  
  <script setup>
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  import { useAuthStore } from '@/store'
  
  const router = useRouter()
  const authStore = useAuthStore() 
  const form = ref(null)
  const email = ref('')
  const password = ref('')
  const showPassword = ref(false)
  const loading = ref(false)

  const emailRules = [
  v => !!v || 'Email is required',
  v => /.+@.+\..+/.test(v) || 'Email must be valid'
]

  const passwordRules = [
  v => !!v || 'Password is required',
  v => v.length >= 6 || 'Password must be at least 6 characters'
]

  
  const handleLogin = async () => {
    const { valid } = await form.value.validate()
  
  if (valid) {
    loading.value = true
    try {
      await authStore.login({ email: email.value, password: password.value })
      router.push('/dashboard')
    } catch (error) {
      console.error('Login failed:', error)
    } finally {
      loading.value = false
    }
  }
}
</script>

<style scoped>
.login-card {
  border-radius: 16px;
  padding: 16px;
  animation: fadeIn 0.5s ease-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>