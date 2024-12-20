export class WebSocketService {
    constructor() {
      this.socket = null
      this.subscribers = new Map()
    }
  
    connect() {
      this.socket = new WebSocket('wss://your-greenhouse-api/ws')
      this.setupListeners()
    }
  
    setupListeners() {
      this.socket.onmessage = (event) => {
        const data = JSON.parse(event.data)
        this.notifySubscribers(data)
      }
    }
  
    subscribe(metricType, callback) {
      if (!this.subscribers.has(metricType)) {
        this.subscribers.set(metricType, new Set())
      }
      this.subscribers.get(metricType).add(callback)
    }
  
    notifySubscribers(data) {
      const { type, value } = data
      if (this.subscribers.has(type)) {
        this.subscribers.get(type).forEach(callback => callback(value))
      }
    }
  }