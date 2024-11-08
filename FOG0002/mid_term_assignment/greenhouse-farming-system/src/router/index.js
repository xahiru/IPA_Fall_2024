import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../components/HomePage.vue';
import Login from '../components/Login.vue';
import Signup from '../components/Signup.vue';
import Dashboard from '../components/Dashboard.vue';
	const routes = [
	  {
	    path: '/',
	    name: 'HomePage',
	    component: HomePage
	  },
	  {
	    path: '/login',
	    name: 'Login',
	    component: Login
	  },
	  {
	    path: '/sign-up',
	    name: 'Signup',
	    component: Signup
	  },
	  {
	    path: '/dashboard',
	    name: 'Dashboard',
	    component: Dashboard
	  },
	  
	];

	const router = createRouter({
	  history: createWebHistory(),
	  routes
	});
	export default router;