<template>
  <v-container fluid class="fill-height bg-grey-lighten-4">
    <v-row align="center" justify="center">
      <v-col cols="12" md="8" class="text-center">
        <h1 class="text-h2 mb-6">
          <v-icon size="48" color="primary" class="mr-2">mdi-greenhouse</v-icon>
          Greenhouse Monitor
        </h1>
        
        <p class="text-h5 mb-12">
          Monitor and control your greenhouse environment in real-time
        </p >

        <v-row justify="center" class="mt-6">
          <v-col cols="12" sm="6" md="4">
            <v-card class="mb-4">
              <v-card-text>
                <v-icon size="48" color="success" class="mb-4">mdi-chart-line</v-icon>
                <h3 class="text-h5 mb-2">Real-time Monitoring</h3>
                <p>Track temperature, humidity, and soil conditions instantly</p >
              </v-card-text>
            </v-card>
          </v-col>

          <v-col cols="12" sm="6" md="4">
            <v-card class="mb-4">
              <v-card-text>
                <v-icon size="48" color="info" class="mb-4">mdi-bell-ring</v-icon>
                <h3 class="text-h5 mb-2">Smart Alerts</h3>
                <p>Get notified when conditions need attention</p >
              </v-card-text>
            </v-card>
          </v-col>

          <v-col cols="12" sm="6" md="4">
            <v-card class="mb-4">
              <v-card-text>
                <v-icon size="48" color="warning" class="mb-4">mdi-cog</v-icon>
                <h3 class="text-h5 mb-2">Easy Control</h3>
                <p>Adjust settings and thresholds with simple controls</p >
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>

            <!-- Add CTA Section -->
        <v-row justify="center" class="mt-12">
          <v-col cols="12" md="6">
            <v-btn
              to="/dashboard"
              size="x-large"
              color="primary"
              block
              class="mb-4"
            >
              View Dashboard
              <v-icon end>mdi-arrow-right</v-icon>
            </v-btn>
            <v-btn
              to="/register"
              size="x-large"
              color="secondary"
              block
              variant="outlined"
            >
              Create Account
              <v-icon end>mdi-account-plus</v-icon>
          </v-btn>
      </v-col>
    </v-row>
    <!-- Footer Section -->
    <v-row class="mt-16">
      <v-col cols="12" class="text-center">
        <v-divider class="mb-6"></v-divider>
        <div class="text-body-2 text-grey">
          <v-icon small class="mr-2">mdi-leaf</v-icon>
          Greenhouse Monitor System
          <v-icon small class="mx-2">mdi-circle-small</v-icon>
          {{ new Date().getFullYear() }}
        </div>
      </v-col>
    </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>