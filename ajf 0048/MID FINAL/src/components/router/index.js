import { createRouter, createWebHistory } from 'vue-router'

const routes = [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/public/HomeView.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/public/LoginView.vue')
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('../views/public/RegisterView.vue')
    },
        {
          path: '/dashboard',
          name: 'dashboard',
          component: () => import('../../components/views/dashboard/DashboardView.vue')
        },
    {
      path: '/settings',
      name: 'settings',
      component: () => import('../views/Dashboard/SettingsView.vue')
        },
        {
          path: '/:pathMatch(.*)*',
          name: 'NotFound',
          component: () => import('../views/public/404.vue')
        }
      ]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router