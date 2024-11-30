<template>
    <div class="row">
      <div class="col-md-6 offset-md-3">
        <div>
          <div>
            <h3>Signup</h3>
            <hr />
          </div>
          <div class="alert alert-danger" v-if="error">
            {{ error }}
          </div>
          <form @submit.prevent="onSignup()">
            <div class="form-group">
              <label>Email</label>
              <input type="text" class="form-control" v-model.trim="email" />
              <div class="error" v-if="errors.email">{{ errors.email }}</div>
            </div>
            <div class="form-group">
              <label>Password</label>
              <input type="password" class="form-control" v-model.trim="password" />
              <div class="error" v-if="errors.password">{{ errors.password }}</div>
            </div>
  
            <div class="my-3">
              <button type="submit" class="btn btn-primary">Signup</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'UserLogin',  // Updated name to multi-word
    data() {
      return {
        email: '',
        password: '',
        errors: [],
        error: '',
      };
    },
    methods: {
      onLogin() {
        // login logic
      },
    },
  };
  </script>
  