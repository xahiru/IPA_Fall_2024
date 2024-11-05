<template>
  <div id="app">
    <LoginForm />
    <EventDemo />
  </div>
</template>

<script>
import LoginForm from './components/LoginForm.vue'
import EventDemo from './components/EventDemo.vue'

export default {
  name: 'App',
  components: {
    LoginForm,
    EventDemo
  }
}
</script>