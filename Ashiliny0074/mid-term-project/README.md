# Greenhouse Monitoring Dashboard

A Vue.js dashboard application designed to monitor and visualize key metrics of a greenhouse farming system. This application provides real-time monitoring of essential greenhouse parameters, featuring both public and authenticated access areas.

## 🌟 Project Overview

This greenhouse monitoring system is designed to help farmers and agricultural professionals monitor their greenhouse environments effectively. The application provides real-time visualization of crucial farming metrics and secure access to detailed monitoring data.

### Key Features:

- **Public Home Page**
  - General information about the greenhouse monitoring system
  - Overview of available features
  - No authentication required

- **Authentication System**
  - Secure user registration
  - Login functionality
  - Password reset capabilities
  - Remember me feature

- **Protected Dashboard**
  - Real-time monitoring of key metrics:
    - Temperature tracking
    - Humidity levels
    - Soil moisture measurements
    - Light intensity monitoring
  - Historical data visualization
  - System status overview

- **Mock API Integration**
  - Simulated real-time data updates
  - Realistic data patterns
  - Configurable update intervals

## 🚀 Live Demo

Visit the live application: [Greenhouse Monitor](https://your-deployment-url.netlify.app)

Test Account:
- Email: test@example.com
- Password: test123

## 🛠️ Technologies Used

- **Frontend Framework**
  - Vue.js 3
  - TypeScript
  - Tailwind CSS

- **State Management & Routing**
  - Vue Router for navigation
  - Local/Session Storage for data persistence

- **Data Visualization**
  - Chart.js for metrics display
  - Real-time data updates

- **Authentication**
  - Custom authentication system
  - Protected route guards
  - Session management

## 📋 Prerequisites

- Node.js (v14.0.0 or higher)
- npm (v6.0.0 or higher)
- Modern web browser with JavaScript enabled

## ⚙️ Installation

1. Clone the repository
```bash
git clone https://github.com/your-username/greenhouse-monitor.git
cd greenhouse-monitor
```

2. Install dependencies
```bash
npm install
```

3. Start the development server
```bash
npm run dev
```

4. Build for production
```bash
npm run build
```

## 📊 Mock Data Configuration

The application uses simulated data to demonstrate greenhouse metrics:

```typescript
// Example mock data structure
interface GreenhouseMetrics {
  temperature: number;    // in Celsius
  humidity: number;      // percentage
  soilMoisture: number; // percentage
  lightLevel: number;    // lux
  timestamp: Date;
}
```

Configure update intervals in `src/utils/mockApi.ts`:
```typescript
const UPDATE_INTERVAL = 5000; // 5 seconds
```

## 📁 Project Structure

```
src/
├── assets/              # Static assets and images
├── components/          # Reusable components
│   ├── auth/           # Authentication components
│   ├── dashboard/      # Dashboard components
│   └── metrics/        # Metrics visualization components
├── router/             # Route configurations
├── utils/              # Utility functions and mock API
├── views/              # Page components
│   ├── Home.vue        # Public home page
│   ├── Login.vue       # Login page
│   ├── Register.vue    # Registration page
│   └── Dashboard/      # Dashboard views
└── App.vue             # Root component
```

## 🔐 Authentication System

The application implements a secure authentication flow:

1. User Registration
   - Email validation
   - Password requirements
   - Duplicate account prevention

2. User Login
   - Credential validation
   - Session management
   - Remember me functionality

3. Protected Routes
   - Authentication verification
   - Unauthorized access prevention
   - Secure routing

## 📈 Dashboard Metrics

The dashboard displays the following metrics:

1. **Temperature**
   - Range: 15°C to 35°C
   - Real-time updates
   - Historical trends

2. **Humidity**
   - Range: 40% to 80%
   - Current levels
   - Daily averages

3. **Soil Moisture**
   - Range: 20% to 80%
   - Current readings
   - Alert thresholds

4. **Light Levels**
   - Range: 0 to 100,000 lux
   - Daily patterns
   - Peak hours

## 🚀 Deployment

The application can be deployed to various hosting platforms:

### Netlify Deployment

1. Create a Netlify account
2. Connect your GitHub repository
3. Configure build settings:
   - Build command: `npm run build`
   - Publish directory: `dist`
4. Deploy!

Current deployment: [https://greenhouse-monitor.netlify.app](https://greenhouse-monitor.netlify.app)

### Vercel Deployment

1. Create a Vercel account
2. Import your GitHub repository
3. Configure build settings:
   - Framework Preset: Vue.js
   - Build Command: `npm run build`
   - Output Directory: `dist`
4. Deploy!

Current deployment: [https://greenhouse-monitor.vercel.app](https://greenhouse-monitor.vercel.app)

## 🧪 Testing

Run the test suite:
```bash
npm run test
```

Run tests in watch mode:
```bash
npm run test:watch
```

## 📝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Open a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- Your Name - Initial work - [YourGitHub](https://github.com/your-username)

## 🌱 Future Enhancements

- Integration with real IoT sensors
- Mobile application
- Advanced analytics
- Automated alert system
- Export functionality for data analysis

## 📞 Support

For support, email your-email@example.com or create an issue in the repository.