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