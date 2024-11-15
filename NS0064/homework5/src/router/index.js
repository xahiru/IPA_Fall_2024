import { createRouter, createWebHistory } from 'vue-router';
import LoginForm from '../components/LoginForm.vue'
import ExpressionDemo from '../components/ExpressionDemo.vue';
import ToggleVisibility from '../components/ToggleVisibility.vue';

const routes = [
    {
      path: '/',
      name: 'LoginForm',
      component: LoginForm
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