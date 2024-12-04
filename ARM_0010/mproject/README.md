# GreenHouse Monitoring System Documentation

## Overview
The GreenHouse Monitoring System is a Vue.js-based web application designed to monitor key greenhouse metrics such as temperature, humidity, soil moisture, and light levels. It features a simple and user-friendly interface, allowi- ng authenticated users to access real-time data simulated through a mock API.

## Features
- Public Home Page: An introductory page accessible to all users.
- Authentication: Login and signup pages to ensure secure access to the dashboard.
- Dashboard: Displays real-time metrics related to the greenhouse environment.
- Simulated Data: Mock API to simulate dynamic updates for greenhouse parameters.
- Responsive Design: Adaptable to various screen sizes using modern styling tools.

## How It Works
1. Home Page:
   Users start on the home page, where they can navigate to the login or signup pages.
   
2. Authentication:
   Users provide their credentials (username and password) to log in. Upon successful authentication, they are redirected to the dashboard.
   
3. Authenticated users view real-time updates of:
   - Temperature (°C)
   - Humidity (%)
   - Soil Moisture (%)
   - Light Level (lux)
     These metrics are simulated using a mock API or dynamically generated in the application.
     
4. Data Updates:
   Metrics are updated every few seconds to simulate real-time behavior.

## Project Development
The GreenHouse Monitoring System was created using the following technologies, tools, and libraries:

1. Primary Tools and Languages
   - Framework: Vue.js (a progressive JavaScript framework for building user interfaces).
   - Language: JavaScript (frontend logic and functionality).
   - Styling: CSS (custom styles) and optionally TailwindCSS for responsiveness.

2. Development Environment
   - Node.js: Used for managing dependencies and running the development server.
   - Vue CLI: Simplified project setup and scaffolding.

3. Libraries and Dependencies
   - Vue Router: For managing page navigation.
   - Vuex or Pinia (Optional): State management library for managing global application state.
   - Mock API: Simulated dynamic data using JavaScript functions.
   - Chart.js: For visualizing greenhouse metrics (temperature, humidity, etc.) on graphs.
     
4. Libraries Used
   - Core Libraries:
       - Vue.js
       - Vue Router

   - Data Visualization:
       - Chart.js (used to render graphs and metrics).

   - Build Tools:
       - Babel (transpilation) and Webpack (bundling).

5. Functionality Workflow

   - Unauthenticated Pages:
       - HomePage.vue: Provides public-facing information about the app.
       - Login.vue and Signup.vue: Manage user authentication.

   - Authenticated Pages:
       - Dashboard.vue: Displays dynamically updated data for greenhouse metrics.

   - Mock API: Simulated metric data is dynamically updated using random number generation.


## Project Installation and Setup
Prerequisites:
 - Node.js and npm installed on your system.
 - Vue CLI installed globally: npm install -g @vue/cli

Steps to Install
 1. Clone the repository:
    - git clone <https://github.com/Ajel88/IPA_Fall_2024/edit/main/ARM_0010/>
    - cd GreenHouseProject
 2. Install dependencies:
    - npm install

 3. Start the development server:
    - npm run serve
      
 4. Open the application in your browser at http://localhost:8080.

