import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '@/components/HomePage.vue';
import LoginPage from '@/components/LoginPage.vue';
import RegisterPage from '@/components/RegisterPage.vue';
import Dashboard from '@/components/Dashboard.vue';

const routes = [
  { path: '/', component: HomePage },
  { path: '/login', component: LoginPage },
  { path: '/register', component: RegisterPage },
  { path: '/dashboard', component: Dashboard, meta: { requiresAuth: true } },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Basic auth guard
router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth && !localStorage.getItem('authenticated')) {
    next('/login');
  } else {
    next();
  }
});

export default router;
