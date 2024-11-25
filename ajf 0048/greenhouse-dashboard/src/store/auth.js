import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: localStorage.getItem('token') || null,
    user: null
  }),
  
  actions: {
    login(credentials) {
      // Simulate API login
      this.token = 'mock-token'
      localStorage.setItem('token', this.token)
    },
    
    register(userData) {
      // Simulate API registration
      this.token = 'mock-token'
      localStorage.setItem('token', this.token)
    },
    
    logout() {
      this.token = null
      this.user = null
      localStorage.removeItem('token')
    }
  }
})