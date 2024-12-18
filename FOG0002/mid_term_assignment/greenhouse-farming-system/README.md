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
20. create a js file (api.js) to handle the functionalities
21. complete the signup functionality
21. create the login functionality
22. To ensure that the dashboard is only accessible to authenticated users, implementd navigation guards with Vue Router.
23. made the dashboard responsive
24. create a components for the overview
25. complete the logout functionality
26. delete the static code from template, use v-for to display dashboard page cards informations
27. created another database file for greenhouse data
28. fetch the data from dashboard 
29. created a components for setting page
30. remove the navbar from all the pages and make a component for navbar
31. create the setting page structure
32. write the setting page functionalities
33. create a component for charts(not used yet)
34. install vue-chartjs 
    1. npm install chart.js vue-chartjs
35. install zoom plugin
    1. npm install chartjs-plugin-zoom
36. complete the charts part