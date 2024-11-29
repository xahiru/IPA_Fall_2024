import { createRouter, createWebHistory } from 'vue-router';

const router = createRouter({
  history: createWebHistory('/'),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/HomeView.vue')
    },
    {
      path: '/logout',
      name: 'logout',
      component: () => import('../views/HomeView.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue')
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('../views/RegisterView.vue')
    },
    {
      path: '/dashboard',
      component: () => import('../views/DashboardLayout.vue'),
      meta: { requiresAuth: true },
      children: [
        {
          path: '',
          name: 'dashboard',
          component: () => import('../views/DashboardOverview.vue')
        },
        {
          path: 'metrics',
          name: 'metrics',
          component: () => import('../views/DashboardMetrics.vue')
        },
        {
          path: 'settings',
          name: 'settings',
          component: () => import('../views/DashboardSettings.vue')
        },
        
        {
          path: 'logs',
          name: 'logs',
          component: () => import('../views/DashboardLogs.vue')
        },
        {
          path: 'logout',
          name: 'logout',
          component: () => import('../views/HomeView.vue')
        }
      ]
    }
  ]
});

router.beforeEach((to, from, next) => {
  const isAuthenticated = !!localStorage.getItem('token');
  
  if (to.meta.requiresAuth && !isAuthenticated) {
    next('/login');
  } else {
    next();
  }
});

export default router;
