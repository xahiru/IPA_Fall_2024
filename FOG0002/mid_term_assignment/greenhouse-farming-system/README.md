###Workflow for Greenhouse Farming System Project Setup
(All commands are for ubuntu24)
1. created the vue app
    1. npm create vite@latest greenhouse-farming-system
2. install the dependencies 
    1. npm install
3. installed all the dependences i need in future
    1. router
        1. npm install vue-router@4
    2. axios
        1. npm install axios
    3. tailwind css (not necessary)
        1.
    4. preline (not necessary)
        1. 
4. disable tailwind and preline for now
5. created a component for HomePage. 
6. write the structure and style for HomePage
7. created a component for Login
8. write the structure and style for Login
9. write the basic structure of router
    import { createRouter, createWebHistory } from 'vue-router';

	const routes = [
        
	  
	];

	const router = createRouter({
	  history: createWebHistory(),
	  routes
	});
	export default router;
10. import and create route for login and homepage

    import HomePage from '../components/HomePage.vue';
    import Login from '../components/Login.vue';

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
	  
	];


11. linked the router to the app.vue
    <router-view></router-view>
12. linked the routes to the homepage page
    <router-link to="/login">Login</router-link>
13. created the signup page
14. connect the signup page with the login page using router
    <router-link to="/sign-up"> Sign up here</router-link> 
15. connect the login with signup also
    <router-link to="/login"> Login here</router-link>
16. create another components for Dashboard
17. complete the structure and styling
18. installed json server globally.(commands are for ubuntu)
    1. sudo npm install -g json-server
19. create a database file by the name of db.json, run the database server
    1. json-server --watch db.json
20. 
