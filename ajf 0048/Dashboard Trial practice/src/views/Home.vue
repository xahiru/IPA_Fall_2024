<template>
    <v-container class="fill-height">
      <v-row justify="center" align="center">
        <v-col cols="12" md="10" class="text-center">
          <v-card class="pa-6" elevation="8" rounded="1g">
          <h1 class="text-h3 mb-6 text-primary font-weight-bold">Welcome to Greenhouse Dashboard</h1>
          <v-card-text>
            <p class="text-h6 mb 6 text-grey-darken-1">Monitor and control your greenhouse environment with real-time data</p>

            <v-row class="mt-6" justify="center">
              <v-col cols="12" sm="6" md="4">
                <V-hover v-slot="{ isHovering, props}">
                  <v-card
                  v-bind="props"
                  :elevation="isHovering ? 12 : 2"
                  :class="{'on-hover': isHovering} "
                  class="transition-swing pa-4"
                  >
                  <v-icon size="48" color="info" class="mt-4">mdi-water</v-icon>
                    <v-card-title>Humidity Monitoring</v-card-title>
                    <v-card-text>Track and maintain optimal humidity levels</v-card-text>
                    </v-card>
                </V-hover>
              </v-col>

              <v-col cols="12" sm="6" md="4">
                <v-hover v-slot="{ isHovering, props }">
                  <v-card
                    v-bind="props"
                    :elevation="isHovering ? 12 : 2"
                    :class="{ 'on-hover': isHovering }"
                    class="transition-swing pa-4"
                  >
                    <v-icon size="48" color="warning" class="mt-4">mdi-white-balance-sunny</v-icon>
                    <v-card-title>Light Management</v-card-title>
                    <v-card-text>Optimize light conditions for plant growth</v-card-text>
                    </v-card>
                    </v-hover>
              </v-col>
            </v-row>
          </v-card-text>

          <v-card-actions class="justify-center mt-4">
            <v-btn
              color="primary"
              size="x-large"
              to="/dashboard"
              variant="elevated"
              class="px-8"
            >
              <v-icon start>mdi-view-dashboard</v-icon>
              Go to Dashboard
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
<style scoped>
.transition-swing {
  transition: 0.3s cubic-bezier(0.25, 0.8, 0.5, 1);
}

.on-hover {
  transform: translateY(-5px);
}</style>