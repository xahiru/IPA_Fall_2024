<template>
    <v-navigation-drawer permanent>
      <v-list-item
        prepend-avatar="https://randomuser.me/api/portraits/men/78.jpg"
        title="Greenhouse Admin"
      ></v-list-item>
  
      <v-divider></v-divider>
  
      <v-list density="compact" nav>
        <v-list-item
          to="/dashboard"
          prepend-icon="mdi-view-dashboard"
          title="Dashboard"
          value="dashboard"
        ></v-list-item>
        <v-list-item
          to="/settings"
          prepend-icon="mdi-cog"
          title="Settings"
          value="settings"
       
        ></v-list-item>
      </v-list>
    </v-navigation-drawer>
  </template>