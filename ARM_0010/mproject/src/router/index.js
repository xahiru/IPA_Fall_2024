import { createRouter, createWebHistory } from 'vue-router';
import UserLogin from '../components/Auth/UserLogin.vue';
import UserRegister from '../components/Auth/UserRegister.vue';
import AppDashboard from '../views/AppDashboard.vue';
import AppHome from '../views/AppHome.vue';

const routes = [
  { path: '/', name: 'Home', component: AppHome },
  { path: '/login', name: 'Login', component: UserLogin },
  { path: '/register', name: 'Register', component: UserRegister },
  { path: '/dashboard', name: 'Dashboard', component: AppDashboard },
  { path: '/:catchAll(.*)', name: 'NotFound', component: () => import('../views/NotFound.vue') },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
