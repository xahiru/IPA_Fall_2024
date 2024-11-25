<template>
  <v-container>
    <v-card class="mx-auto mt-5" max-width="400">
      <v-card-title class="text-center text-h5">Register</v-card-title>
      <v-card-text>
        <v-form @submit.prevent="handleRegister">
          <v-text-field
            v-model="email"
            label="Email"
            type="email"
            required
          ></v-text-field>
          <v-text-field
            v-model="password"
            label="Password"
            type="password"
            required
          ></v-text-field>
          <v-btn type="submit" color="primary" block class="mt-4">Register</v-btn>
        </v-form>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/store'

const router = useRouter()
const authStore = useAuthStore()
const email = ref('')
const password = ref('')

const handleRegister = async () => {
  await authStore.register({ email: email.value, password: password.value })
  router.push('/dashboard')
}
</script>