import { createRouter, createWebHistory } from "vue-router";
import Home from "../components/Home.vue";
import Login from "../components/Login.vue";
import Signup from "../components/Signup.vue";
import Dashboard from "../components/Dashboard.vue"


const routes = [
  { path: "/", 
    name: "Home", 
    component: Home },
  { path: "/login", 
    name: "Login", 
    component: Login },
  { path: "/signup", 
    name: "Signup", 
    component: Signup },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: Dashboard,
  },
  

];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
