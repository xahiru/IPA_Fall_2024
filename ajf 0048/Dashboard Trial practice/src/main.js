import { createApp } from 'vue'
import { createPinia } from 'pinia'
import router from './router'
import { createVuetify } from 'vuetify'
import 'vuetify/styles'
import App from './App.vue'
import '@mdi/font/css/materialdesignicons.css'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const vuetify = createVuetify({
    components,
    directives,
    theme: {
    defaultTheme: 'light'
    }
})

const app = createApp(App)
app.use(createPinia())
app.use(router)
app.use(vuetify)
app.mount('#app')
