<script setup>
import { ref } from 'vue';
// import FormDemo from './components/FormDemo.vue';
// import LoginForm from './components/LoginForm.vue';
// import ReactivityDemo from './components/ReactivityDemo.vue';
// import ExpressionDemo from './components/ExpressionDemo.vue';
// import EventDemo from './components/EventDemo.vue';
// import ToggleVisibility from './components/ToggleVisibility.vue'

const message = ref('Hello, Vue 3!');

// for raw HTML
const rawHtml = ref('<h1>This is bold text rendered as HTML</h1>');

// for attribute bindings
const imageUrl = ref('https://vuejs.org/images/logo.png');
const imageAlt = ref('Vue.js Logo');
const linkUrl = ref('https://vuejs.org');

// for conditional rendering (directives)
const isChecked = ref(true);
const isVisible = ref(false);
const showText = ref(false);

// for javascript expressions
const number = ref(5);
const a = ref(3);
const b = ref(7);

// for list rendering
const items = ref(['Item 1', 'Item 2', 'Item 3']);

// for dynamically binding multiple attributes
const buttonAttributes = ref({
  id: 'dynamic-button',
  class: 'btn btn-primary',
  disabled: true
});


// for event handling
const handleClick = () => {
  alert('Button clicked!');
};

</script>

<template>
  <main>

    <!-- Text Interpolation -->
    <h1>{{ message }}</h1>
    
    <!-- Raw HTML -->
    <div v-html="rawHtml"></div>
    
    <!-- Attribute Bindings -->
    <img :src="imageUrl" :alt="imageAlt" />

    <!-- Shorthand Attribute Bindings (v-bind) -->
    <a :href="linkUrl" target="_blank">Go to Vue.js</a>
    <!-- Same name shorthand (v-bind) -->
    <button @click="handleClick">Click Me</button>

    <!-- Boolean Attributes -->
    <input type="checkbox" v-bind:checked="isChecked" />

    <!-- Dynamically Binding Multiple Attributes with v-bind -->
    <button v-bind="buttonAttributes">Dynamically Bound Button</button>

    <!-- Using JavaScript Expressions -->
    <p>{{ number }} squared is {{ number * number }}</p>
    <p>The sum of {{ a }} + {{ b }} is {{ a + b }}</p>
    
    <!-- Directives Example: v-if, v-for, v-show -->
    <div v-if="isVisible">This content is conditionally visible.</div>
    <ul>
      <li v-for="(item, index) in items" :key="index">{{ item }}</li>
    </ul>
    <p v-show="showText">This text can be shown or hidden.</p>

    <!-- <FormDemo /> -->
    <!-- <ReactivityDemo /> -->
    <!-- <LoginForm /> -->
    <!-- <ExpressionDemo /> -->
    <!-- <EventDemo /> -->
    <!-- <ToggleVisibility/> -->

  </main>
</template>

<style scoped>
main {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  min-height: 100vh; /* Ensures the main content is centered vertically */
}

h1 {
  color: #42b983;
}

.btn {
  padding: 0.5em 1em;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.btn-primary {
  background-color: #35495e;
}

ul {
  list-style-type: disc;
  margin-left: 20px;
  padding: 0;
}

a, img, button, p, input, ul {
  margin: 10px 0;
}
</style>
