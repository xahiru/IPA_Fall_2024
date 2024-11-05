import { createRouter, createWebHistory } from 'vue-router';
import Login from '../components/Login.vue';
import ExpressionDemo from '../components/ExpressionDemo.vue';
import ToggleVisibility from '../components/ToggleVisibility.vue';

const routes = [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
        path: '/expression-demo',
        name: 'ExpressionDemo.',
        component: ExpressionDemo
      },
      {
        path: '/toggle-visibility',
        name: 'ToggleVisibility.',
        component: ToggleVisibility
      },
  ];

  const router = createRouter({
    history: createWebHistory(),
    routes
  });

  export default router;