import { createRouter, createWebHistory } from 'vue-router';
import Home from'../components/Home.vue';
import Login from '../components/Login.vue';
import Signup from '../components/Signup.vue';



const routes = [
    {path: '/', name: 'Home', components: Home},
    {path: '/', name: 'Login', components: Login},
    {path: '/', name: 'Signup', components: Signup},
];


const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

 
 
  export default router;