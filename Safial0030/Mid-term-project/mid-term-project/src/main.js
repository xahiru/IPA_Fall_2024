import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap'; // Include Bootstrap's JavaScript for navbar toggling
// Optional: Import your CSS styles

// Create the Vue app
const app = createApp(App);


// Use the router
app.use(router);

// Mount the app
app.mount('#app');