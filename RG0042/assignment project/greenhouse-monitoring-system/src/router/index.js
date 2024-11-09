import { createRouter, createWebHistory } from 'vue-router';
import Home from'../components/Home.vue';
import LoginPage from '../components/LoginPage.vue';
import SignupPage from '../components/SignupPage.vue';



const routes = [
    {path: '/', name: 'Home', components: Home},
    {path: '/', name: 'LoginPage', components: LoginPage},
    {path: '/', name: 'SignupPage', components: SignupPage},
];


const router = createRouter({
    history: createWebHistory(),
    routes,
});


router.beforeEach((to, from, next) => {
    const loggedIn = localStorage.getItem('auth');
    if (to.matched.some(record => record.meta.requiresAuth) && !loggedIn) {
      next('/login');
    } else {
      next();
    }
  });
  
 
  export default router;