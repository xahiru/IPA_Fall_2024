import { createRouter, createWebHistory } from 'vue-router';
import Home from '../components/Home.vue';
import Login from '../components/Login.vue';
import Signup from '../components/Signup.vue';
import Dashboard from '../components/Dashboard.vue';
import Overview from '../components/Overview.vue';
import Setting from '../components/Setting.vue';
import Charts from '../components/Charts.vue';

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
	  },
      {
	    path: '/dashboard',
	    name: 'Dashboard',
	    component: Dashboard,
		meta: { requiresAuth: true }
	  },
      {
	    path: '/overview',
	    name: 'Overview',
	    component: Overview,
		meta: { requiresAuth: true }
	  },
      {
	    path: '/settings',
	    name: 'Setting',
	    component: Setting,
		meta: { requiresAuth: true }
	  },
      {
	    path: '/charts',
	    name: 'Charts',
	    component: Charts,
		meta: { requiresAuth: true }
	  }
	  
	];

	const router = createRouter({
	  history: createWebHistory(),
	  routes
	});



	router.beforeEach((to, from, next) => {
		if (to.matched.some(record => record.meta.requiresAuth)) {
			const user = localStorage.getItem("user");
			
			if (!user) {
				next({ name: 'Login' });
			} else {
				next();
			}
		} else {
			next();
		}
	});

	export default router;