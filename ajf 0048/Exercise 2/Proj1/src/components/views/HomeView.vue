<template>
    <v-container fluid class="fill-height bg-grey-lighten-4">
      <v-row align="center" justify="center">
        <v-col cols="12" md="8" lg="6" class="text-center">
          <h1 class="text-h2 mb-6">Smart Greenhouse Monitor</h1>
          <p class="text-subtitle-1 mb-6">Monitor and control your greenhouse environment</p >
          <v-row justify="center" class="mt-4">
            <v-col cols="auto">
              <v-btn
                to="/login"
                size="x-large"
                color="primary"
                class="mx-2"
              >
                <v-icon start>mdi-login</v-icon>
                Login
              </v-btn>
              <v-btn
                to="/register"
                size="x-large"
                variant="outlined"
                class="mx-2"
              >
                <v-icon start>mdi-account-plus</v-icon>
                Register
              </v-btn>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
  </template>