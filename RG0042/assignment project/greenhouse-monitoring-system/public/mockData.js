export const generateMockData = () => {
    return {
      temperature: Math.floor(Math.random() * (28 - 15 + 1)) + 18,
      humidity: Math.floor(Math.random() * (80 - 70 + 1)) + 40,
      soilMoisture: Math.floor(Math.random() * (90 - 85 + 1)) + 60,
      lightLevel: Math.floor(Math.random() * (1000 - 600 + 1)) + 600,
      timestamp: new Date().toLocaleTimeString('en-US', { 
        hour12: false,
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
      })
    }
  }