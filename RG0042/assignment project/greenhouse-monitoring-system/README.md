##Workflow for Greenhouse-Monitoring-System Project Setup

1.Create the Vue App
  npm init vue@latest greenhouse-dashboard 
  cd greenhouse-dashboard

2.Install dependencies
  npm install
  npm install vite-plugin-vue-devtools --save-dev

3.Install this dependence in future
  A.Router
    npm install vue-router@4
  B.Tailwindcss
    npm install -D tailwindcss postcss autoprefixer
    npx tailwindcss init
  C.Axios
    npm install axios

4.Created Views Folder to add File 
  A. Home.vue
  B. Login.vue
  C. Signup.Vue
  D. Dashboard.vue

  {We Add This file Step-by-step and write the code, script & style}

5.Create router.js File
    A.Write Basic Structure 
      import { createRouter, createWebHistory } from 'vue-router';

      const routes = [

      ];

      const router = createRouter({ history: createWebHistory(), routes });
      export default router;

    B.import and create route for Views components.

6.create main.js file to import App.vue, router & tailwind.css

7.In App.vue We just link router-view

8.We want to install some necessary Files
 A.tailwind.config.js
 B.vite.config.js
 C.postcss.config.js

 Here is the commend to install this files:
   npm install -D tailwindcss postcss autoprefixer
   npx tailwindcss init
   npm install vite-plugin-vue-devtools --save-dev

9.In assets file:
   add some background images & basic css
   inside tailwind.config.js file we have theme section there we link our background images.
  
10.installed json server globally
   npm install -g json-server

11. installed Cors
   npm install cors
   then create server.js file & add code

12.create a database file by the name of db.json, run the database server
    json-server --watch db.json

    if you change port of you server then you mention you port end of the commande
    for example: json-server --watch db.json --port 3001

13.Created components Folder to add File
    A.DashboardContent.vue
    B.Navbar.vue
    {we add this 2 file before complete No: 10, 11, 12}

    C.DataCard.vue
    D.SettingsPanel
    