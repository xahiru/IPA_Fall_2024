const api = {
    getMetrics() {
      return new Promise((resolve) => {
        setTimeout(() => {
          resolve({
            temperature: Math.random() * (30 - 20) + 20,
            humidity: Math.random() * (80 - 40) + 40,
            soilMoisture: Math.random() * (100 - 20) + 20,
            lightLevel: Math.random() * (2000 - 100) + 100,
            co2Level: Math.random() * (600 - 300) + 300,
            nutrientLevel: Math.random() * (100 - 20) + 20
          })
        }, 1000)
      })
    }
  }
  
  export default api