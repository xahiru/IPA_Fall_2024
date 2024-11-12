import { createRouter, createWebHistory } from "vue-router";
import Home from "./views/Home.vue";
import Login from "./views/Login.vue";
import Signup from "./views/Signup.vue";
import Dashboard from "./views/Dashboard.vue";

const routes = [
    {path: '/', component: Home},
    {path: '/login', component: Login},
    {path: '/signup', component: Signup},
    {path: '/dashboard', component: Dashboard, meta: {reqiresAuth: true} },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

router.beforeEach((to, _from, next) => {
    const isAuthenticated = localStorage.getItem('auth');
    if (to.meta.reqiresAuth && !isAuthenticated) next('/login');
    else next();
});
