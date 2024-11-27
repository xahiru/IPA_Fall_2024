import { createApp } from 'vue'
import App from './App.vue'
import router from './components/router'
import vuetify from './plugins/vuetify'
import '@mdi/font/css/materialdesignicons.css'
import './assets/styles/buttons.css'

const app = createApp(App)
app.use(router)
app.use(vuetify)
app.mount('#app')