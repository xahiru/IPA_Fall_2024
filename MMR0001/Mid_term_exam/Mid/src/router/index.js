import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../components/HomePage.vue';
import Login from '../components/Login.vue';
import SignupPage from '../components/SignupPage.vue';
import Dashboard from '../components/Dashboard.vue';
import DataDisplay from '../components/DataDisplay.vue';

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
	    path: '/signup-page',
	    name: 'SignupPage',
	    component: SignupPage
	  },
	  { path: '/', name: 'HomePage', component: HomePage },
	  { path: '/login', name: 'Login', component: Login },
	  { path: '/signup-page', name: 'SignupPage', component: SignupPage },
	  {
		path: '/dashboard',
		name: 'Dashboard',
		component: Dashboard,
		meta: { requiresAuth: true }
	  },
	  {
	    path: '/data-display',
	    name: 'DataDisplay',
	    component: DataDisplay
	  },
	];

	const router = createRouter({
	  history: createWebHistory(),
	  routes
	});
	export default router;