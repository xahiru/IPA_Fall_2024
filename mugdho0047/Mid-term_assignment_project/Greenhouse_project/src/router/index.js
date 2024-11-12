import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../components/HomePage.vue';
import Login from '../components/Login.vue';
import Signup from '../components/Signup.vue';

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
	    path: '/Signup',
	    name: 'Signup',
	    component: Signup
	  },
	  
	];

	const router = createRouter({
	  history: createWebHistory(),
	  routes
	});
	export default router;