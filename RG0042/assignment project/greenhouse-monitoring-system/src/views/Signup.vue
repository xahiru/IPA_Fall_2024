<template>
    <div class="signup-page">
      <div class="signup-container max-w-md mx-auto p-4">
        <h1 class="text-2xl font-bold mb-4">Sign Up</h1>
        <form @submit.prevent="register" class="flex flex-col gap-4">
          <div>
            <label for="username" class="block font-medium">Username</label>
            <input
              id="username"
              type="text"
              v-model="username"
              required
              class="input-field"
              placeholder="Enter your username"
            />
          </div>
          <div>
            <label for="email" class="block font-medium">Email</label>
            <input
              id="email"
              type="email"
              v-model="email"
              required
              class="input-field"
              placeholder="Enter your email"
            />
          </div>
          <div>
            <label for="password" class="block font-medium">Password</label>
            <input
              id="password"
              type="password"
              v-model="password"
              required
              class="input-field"
              placeholder="Enter your password"
            />
          </div>
          <button type="submit" class="btn-primary">Sign Up</button>
        </form>
        <p class="mt-4 text-center">
          Already have an account?
          <router-link to="/login" class="text-blue-500 hover:underline">Log in</router-link>
        </p>
      </div>
    </div>  
    </template>
    
    <script>
    export default {
      data() {
        return {
          username: '',
          email: '',
          password: '',
        };
      },
      methods: {
        register() {
          // Basic registration logic (for demonstration purposes)
          if (this.username && this.email && this.password) {
            const userData = {
              username: this.username,
              email: this.email,
              password: this.password,
            };
    
            // Store user data in localStorage (as a basic simulation of registration)
            localStorage.setItem('user', JSON.stringify(userData));
            localStorage.setItem('auth', true); // Mark the user as authenticated
    
            // Redirect to dashboard after registration
            this.$router.push('/dashboard');
          } else {
            alert('Please fill in all fields');
          }
        },
      },
    };
    </script>
    
    <style scoped>
    .signup-container {
      background-color: #f9fafb;
      border: 1px solid #e5e7eb;
      border-radius: 8px;
      padding: 2rem;
    }
    
    .input-field {
      width: 100%;
      padding: 0.75rem;
      margin-top: 0.25rem;
      border: 1px solid #d1d5db;
      border-radius: 4px;
    }
    
    .btn-primary {
      background-color: #3b82f6;
      color: white;
      padding: 0.75rem;
      font-weight: bold;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      transition: background-color 0.3s;
    }
    
    .btn-primary:hover {
      background-color: #2563eb;
    }
    </style>
    