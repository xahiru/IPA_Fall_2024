import { createRouter, createWebHistory } from "vue-router";
import Login from '../src/pages/Login.vue';
import Signup from '../src/pages/Signup.vue';
import Home from '../src/pages/Home.vue';
import Home from '../src/pages/Home.vue';
import DashBoard from '../src/pages/DashBoard.vue';

const routes = [
    {
        path: '/login',
        component: Login,
      },
      {
        path: '/signup',
        component: Signup,
      },

      { path: "/", name: "Home", component: Home },
      { path: "/dashboard", name: "Dashboard", component: Dashboard },
    ];


const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
