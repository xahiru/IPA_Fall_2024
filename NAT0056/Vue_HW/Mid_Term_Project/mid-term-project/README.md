 
 Description of workflow for Greenhouse Farming System Project Setup (All commands are for ubuntu24)


 created the vue app

 npm create vite@latest Mid-term-project
install the dependencies

npm install
installed all the dependences i need in future

router
npm install vue-router@4
axios
npm install axios
tailwind css (not necessary) 1.
preline (not necessary) 1.
disable tailwind and preline for now

created a structure for HomePage.

write the style by css for HomePage

created a structure for Login

write the style by css for Login

write the basic structure of router import { createRouter, createWebHistory } from 'vue-router';

const routes = [

];

const router = createRouter({ history: createWebHistory(), routes }); export default router;

import and create route for login and homepage

import HomePage from '../components/HomePage.vue'; import Login from '../components/Login.vue';

const routes = [ { path: '/', name: 'HomePage', component: HomePage }, { path: '/login', name: 'Login', component: Login },

];

linked the router to the app.vue

linked the routes to the homepage page Login

installed json server globally.(commands are for ubuntu)

sudo npm install -g json-server
create a database file by the name of db.json, run the database server

json-server --watch db.json
create a js file (api.js) to handle the functionalities

complete the signup functionality

create the login functionality

To ensure that the dashboard is only accessible to authenticated users, implementd navigation guards with Vue Router.

made the dashboard responsive

create a components for the overview

c omplete the logout functionality

 delete the static code from template, use v-for to display dashboard page cards informations

 created another database file for greenhouse data

 fetch the data from dashboard

 created a components for setting page

 remove the navbar from all the pages and make a component for navbar

 create the setting page structure

 write the setting page functionalities

 create a component for charts(not used yet)

 install vue-chartjs

 npm install chart.js vue-chartjs
