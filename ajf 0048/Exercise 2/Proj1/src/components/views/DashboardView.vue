<template>
    <v-container fluid>
      <v-row>
        <v-col cols="12">
          <h1 class="text-h4 mb-6">
            <v-icon size="36" color="primary" class="mr-2">mdi-view-dashboard</v-icon>
            Greenhouse Dashboard
          </h1>
        </v-col>
      </v-row>
  
      <v-row>
        <!-- Temperature Card -->
        <v-col cols="12" sm="6" md="4">
          <v-card class="metric-card">
            <v-card-text class="d-flex flex-column align-center">
              <v-icon size="48" color="error" class="mb-2">mdi-thermometer</v-icon>
              <div class="text-h4 mb-2">25°C</div>
              <div class="text-subtitle-1">Temperature</div>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </template>