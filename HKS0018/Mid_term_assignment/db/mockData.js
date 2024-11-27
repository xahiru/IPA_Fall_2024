export const generateMockData = () => {
    return {
      temperature: Math.floor(Math.random() * (28 - 18 + 1)) + 18,
      humidity: Math.floor(Math.random() * (80 - 40 + 1)) + 40,
      soilMoisture: Math.floor(Math.random() * (90 - 60 + 1)) + 60,
      lightLevel: Math.floor(Math.random() * (1000 - 600 + 1)) + 600,
      timestamp: new Date().toLocaleTimeString('en-US', { 
        hour12: false,
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
      })
    };
  };
  
  export const startMockDataUpdates = (callback) => {
    setInterval(() => {
      const data = generateMockData();
      callback(data);
    }, 5000);
  };
  