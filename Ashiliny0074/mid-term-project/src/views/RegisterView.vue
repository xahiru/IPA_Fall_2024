<template>
    <div class="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div class="max-w-md w-full space-y-8">
        <div>
          <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">Create your account</h2>
          <p class="mt-2 text-center text-sm text-gray-600">
            Or
            <router-link to="/login" class="font-medium text-blue-600 hover:text-blue-500">
              sign in to your account
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
              <label for="name" class="sr-only">Full name</label>
              <input
                id="name"
                v-model="name"
                type="text"
                required
                class="appearance-none rounded-t-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-blue-500 focus:border-blue-500 focus:z-10 sm:text-sm"
                placeholder="Full name"
              />
            </div>
            <div>
              <label for="email" class="sr-only">Email address</label>
              <input
                id="email"
                v-model="email"
                type="email"
                required
                class="appearance-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-blue-500 focus:border-blue-500 focus:z-10 sm:text-sm"
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
                class="appearance-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-blue-500 focus:border-blue-500 focus:z-10 sm:text-sm"
                placeholder="Password"
              />
            </div>
            <div>
              <label for="confirmPassword" class="sr-only">Confirm password</label>
              <input
                id="confirmPassword"
                v-model="confirmPassword"
                type="password"
                required
                class="appearance-none rounded-b-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-blue-500 focus:border-blue-500 focus:z-10 sm:text-sm"
                placeholder="Confirm password"
              />
            </div>
          </div>
  
          <div class="mt-4">
            <button
              type="submit"
              :disabled="loading"
              class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
            >
              {{ loading ? 'Creating account...' : 'Create account' }}
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
  const name = ref('');
  const email = ref('');
  const password = ref('');
  const confirmPassword = ref('');
  const loading = ref(false);
  const error = ref('');
  
  const handleSubmit = async () => {
    // Validate form
    if (!name.value || !email.value || !password.value || !confirmPassword.value) {
      error.value = 'All fields are required';
      return;
    }
  
    if (password.value !== confirmPassword.value) {
      error.value = 'Passwords do not match';
      return;
    }
  
    if (password.value.length < 6) {
      error.value = 'Password must be at least 6 characters';
      return;
    }
  
    loading.value = true;
    error.value = '';
  
    try {
      // Get existing users
      const users = JSON.parse(localStorage.getItem('users') || '[]');
      
      // Check if email already exists
      if (users.some(u => u.email === email.value)) {
        throw new Error('Email already registered');
      }
  
      // Add new user
      users.push({
        name: name.value,
        email: email.value,
        password: password.value
      });
  
      // Save updated users
      localStorage.setItem('users', JSON.stringify(users));
  
      // Show success message
      alert('Registration successful! Please login.');
      
      // Redirect to login
      router.push('/login');
    } catch (err: any) {
      error.value = err.message || 'Failed to create account';
    } finally {
      loading.value = false;
    }
  };
  </script>