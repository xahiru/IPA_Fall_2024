# Vue 3 + Vite
###Work for Greenhouse Farming System

created the vue app

npm create vite@latest mid

npm install

router
npm install vue-router@4
npm install vue-router

npm install chart.js

created a component for HomePage.

write the structure and style for HomePage

created a component for Login

write the structure and style for Login

created a component for SignupPage

write the structure and style for SignupPage

write the basic structure of router import { createRouter, createWebHistory } from 'vue-router';

const routes = [

];

const router = createRouter({ history: createWebHistory(), routes }); export default router;

import and create route for login,homepage and signuppage 

import HomePage from '../components/HomePage.vue'; import Login from '../components/Login.vue'; import SignupPage from '../components/SignupPage.vue';

const routes = [ { path: '/', name: 'HomePage', component: HomePage }, { path: '/login', name: 'Login', component: Login },{path:'/signup-page', name: 'SignupPagge', component: SignupPage }

];

linked the router to the app.vue

linked the router to the homepage page Login

linked the router to the homepage signup