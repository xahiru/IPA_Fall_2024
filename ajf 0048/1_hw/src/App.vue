<template>
  <div id="app">
    <LoginForm />
    <EventDemo />
    <ExpressionDemo />
  </div>
</template>

<script>
import LoginForm from './components/LoginForm.vue'
import EventDemo from './components/EventDemo.vue'
import ExpressionDemo from './components/ExpressionDemo.Vue'
import ToggleVisibility from './components/ToggleVisibility.vue'

export default {
  name: 'App',
  components: {
    LoginForm,
    EventDemo,
    ExpressionDemo,
    ToggleVisibility
  }
}
</script>