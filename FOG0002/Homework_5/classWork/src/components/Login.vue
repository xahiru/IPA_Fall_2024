<script setup>
import {ref} from 'vue';
import EventDemo from './EventDemo.vue';

const name = ref('');
const password = ref('');
const loginView = ref(true);
const homeViews = ref(false);
const seeOtherPage = ref(false);

const handleSubmit=()=>{
    alert(name.value);
    loginView.value = false;
    homeViews.value=true;
}

const handlePage=()=>{
    seeOtherPage.value=true;
    homeViews.value = false;
}





</script>

<template>
    <div>
        <div id="from-body" v-if="loginView">
            <div class="login-container">
                <form @submit.prevent="handleSubmit"  class="login-form">
                  <h2>Login</h2>
                  <div class="form-group">
                    <label for="username">Username</label>
                    <input type="text" id="username" name="username" v-model="name" required>
                  </div>
                  <div class="form-group">
                    <label for="password">Password</label>
                    <input type="password" id="password" name="password" v-model="password" required>
                  </div>
                  <button type="submit">Login</button>
                </form>
              </div>          
        </div>


        <div>
            <div class="home-views" v-if="homeViews">
                <h1>Hello {{name}}, welcome</h1>
                <button @click="handlePage">Go to 2nd homework</button>
            </div>
            <div v-if="seeOtherPage">
                <EventDemo />
            </div>
        </div>
    </div>
    
    
</template>

<style scoped>

#from-body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 0;
  }
  
  .login-container {
    background-color: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    width: 300px;
  }
  
  .login-form h2 {
    text-align: center;
    margin-bottom: 20px;
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  label {
    display: block;
    margin-bottom: 5px;
  }
  
  input {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  button {
    width: 100%;
    padding: 10px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #218838;
  }
  
</style>
