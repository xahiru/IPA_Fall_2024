<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8">
      <div>
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">Sign in to your account</h2>
        <p class="mt-2 text-center text-sm text-gray-600">
          Or
          <router-link to="/register" class="font-medium text-blue-600 hover:text-blue-500">
            create a new account
          </router-link>
        </p>
      </div>

      <!-- Error Alert -->
      <div v-if="error" class="rounded-md bg-red-50 p-4">
        <div class="flex">
          <div class="text-sm text-red-700">{{ error }}</div>
        </div>
      </div>

      <form @submit.prevent="handleSubmit">
        <div class="rounded-md shadow-sm -space-y-px">
          <div>
            <label for="email" class="sr-only">Email address</label>
            <input
              id="email"
              v-model="email"
              type="email"
              required
              class="appearance-none rounded-t-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-blue-500 focus:border-blue-500 focus:z-10 sm:text-sm"
              placeholder="Email address"
            />
          </div>
          <div>
            <label for="password" class="sr-only">Password</label>
            <input
              id="password"
              v-model="password"
              type="password"
              required
              class="appearance-none rounded-b-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-blue-500 focus:border-blue-500 focus:z-10 sm:text-sm"
              placeholder="Password"
            />
          </div>
        </div>

        <div class="flex items-center justify-between mt-4">
          <div class="flex items-center">
            <input
              id="remember-me"
              v-model="rememberMe"
              type="checkbox"
              class="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
            />
            <label for="remember-me" class="ml-2 block text-sm text-gray-900">
              Remember me
            </label>
          </div>
        </div>

        <div class="mt-4">
          <button
            type="submit"
            :disabled="loading"
            class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
          >
            {{ loading ? 'Signing in...' : 'Sign in' }}
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const email = ref('');
const password = ref('');
const rememberMe = ref(false);
const loading = ref(false);
const error = ref('');

const handleSubmit = async () => {
  loading.value = true;
  error.value = '';

  try {
    // Get registered users
    const users = JSON.parse(localStorage.getItem('users') || '[]');
    const user = users.find(u => u.email === email.value && u.password === password.value);

    if (!user) {
      throw new Error('Invalid email or password');
    }

    // Set authentication
    localStorage.setItem('token', 'user-token');
    localStorage.setItem('currentUser', JSON.stringify(user));
    
    if (rememberMe.value) {
      localStorage.setItem('rememberedEmail', email.value);
    }

    router.push('/dashboard');
  } catch (err: any) {
    error.value = err.message || 'Invalid credentials';
  } finally {
    loading.value = false;
  }
};

// Check for remembered email
const rememberedEmail = localStorage.getItem('rememberedEmail');
if (rememberedEmail) {
  email.value = rememberedEmail;
  rememberMe.value = true;
}
</script>
