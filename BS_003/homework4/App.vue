<template>
  <div id="app">
    <h1>Vue 3 Homework - Combined Tasks</h1>
    
    <ToggleVisibility />
    <LoginForm />
    <EventDemo />
    <ExpressionDemo />
  </div>
</template>

<script>
import ToggleVisibility from './components/ToggleVisibility.vue';
import LoginForm from './components/LoginForm.vue';
import EventDemo from './components/EventDemo.vue';
import ExpressionDemo from './components/ExpressionDemo.vue';

export default {
  name: 'App',
  components: {
    ToggleVisibility,
    LoginForm,
    EventDemo,
    ExpressionDemo
  }
};
</script>
