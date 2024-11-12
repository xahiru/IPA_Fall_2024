import { createRouter, createWebHistory } from 'vue-router';
import Home from '../components/Home.vue';
import Login from '../components/Login.vue';
import Signup from '../components/Signup.vue';

	const routes = [
	  {
	    path: '/',
	    name: 'Home',
	    component: Home
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
	  }
	  
	];

	const router = createRouter({
	  history: createWebHistory(),
	  routes
	});
	export default router;