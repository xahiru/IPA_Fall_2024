# Vue 3 + Vite
###Greenhouse Farming System

1: created the vue app

2: npm create vite@latest mid

3: npm install

4: install the dependencies

npm install

#installed all the dependences i need in future

5: router
    npm install vue-router@4

#axios
   npm install axios

6: npm install chart.js

7: created a component for HomePage.

8: write the structure and style for HomePage

9: created a component for Login

10: write the structure and style for Login

11: created a component for SignupPage

12: write the structure and style for SignupPage

13: write the basic structure of router import { createRouter, createWebHistory } from 'vue-router';

const routes = [

];

const router = createRouter({ history: createWebHistory(), routes }); export default router;

14: import and create route for login,homepage and signuppage 

 import HomePage from '../components/HomePage.vue'; import Login from '../components/Login.vue'; import SignupPage from '../components/SignupPage.vue';

const routes = [ { path: '/', name: 'HomePage', component: HomePage }, { path: '/login', name: 'Login', component: Login },{path:'/signup-page', name: 'SignupPagge', component: SignupPage }

];

15: linked the router to the app.vue

16: linked the router to the homepage page Login

17: created the signup page

18: linked the router to the homepage signup

19: connect the signup page with the login page using router

20: connect the login with signup also 

21: create another components for Dashboard

22: complete the structure and styling

23: installed json server globally.(commands are for windows)

npm install -g json-server

24: create a database file by the name of db.json, run the database server

json-server --watch db.json

25: create a js file (api.js) to handle the functionalities

26: complete the signup functionality

27: create the login functionality

To ensure that the dashboard is only accessible to authenticated users, implementd navigation guards with Vue Router.

28: made the dashboard responsive

29: create a components for the overview

30: complete the logout functionality

31: created a components for setting page

32: created another database file for greenhouse data