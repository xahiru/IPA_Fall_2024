import { defineStore } from 'pinia'
import axios from 'axios'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    token: localStorage.getItem('token') || null,
  }),
  actions: {
    async login(email, password) {
      // Simulate API call
      const response = await axios.post('/api/login', { email, password })
      this.user = response.data.user
      this.token = response.data.token
      localStorage.setItem('token', this.token)
    },
    async register(email, password) {
      // Simulate API call
      const response = await axios.post('/api/register', { email, password })
      this.user = response.data.user
      this.token = response.data.token
      localStorage.setItem('token', this.token)
    },
    logout() {
      this.user = null
      this.token = null
      localStorage.removeItem('token')
    },
  },
})

export const useGreenhouseStore = defineStore('greenhouse', {
  state: () => ({
    temperature: 0,
    humidity: 0,
    soilMoisture: 0,
    lightLevel: 0,
    settings: {
      temperatureThreshold: 30,
      humidityThreshold: 60,
      soilMoistureThreshold: 40,
      lightLevelThreshold: 1000,
    },
  }),
  actions: {
    async fetchData() {
      // Simulate API call
      const response = await axios.get('/api/greenhouse-data')
      this.temperature = response.data.temperature
      this.humidity = response.data.humidity
      this.soilMoisture = response.data.soilMoisture
      this.lightLevel = response.data.lightLevel
    },
    updateSettings(newSettings) {
      this.settings = { ...this.settings, ...newSettings }
    },
  },
})