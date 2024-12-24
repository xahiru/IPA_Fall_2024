import { createRouter, createWebHistory } from "vue-router";
import Home from "./views/Home.vue";
import Login from "./views/Login.vue";
import Signup from "./views/Signup.vue";
import Dashboard from "./views/Dashboard.vue";
import SettingsPanel from "./components/SettingsPanel.vue";
import Charts from "./components/Charts.vue";
import NotFound from "./views/NotFound.vue";
import Logs from "./views/Logs.vue";

const routes = [
    {path: '/', component: Home},
    {path: '/login', component: Login},
    {path: '/signup', component: Signup},
    {path: '/dashboard', component: Dashboard, meta: {reqiresAuth: true} },
    {path: '/SettingsPanel', component: SettingsPanel, meta: {requiresAuth: true}},
    {path: '/charts', component: Charts, meta: { requiresAuth: true}},
    {path: '/logs', component: Logs, meta: { reqiresAuth: true}},
    {path: '/:pathMatch(.*)*', component: NotFound}
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

export default router;
