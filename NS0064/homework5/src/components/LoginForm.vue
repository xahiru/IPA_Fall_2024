<script setup>
import { ref } from 'vue';
import EventDemo from './EventDemo.vue';

const name = ref('');
const password = ref('');
const loginView = ref(true);
const homeViews = ref(false);
const seeOtherPage = ref(false);

const handleSubmit = () => {
    alert(name.value);
    loginView.value = false;
    homeViews.value = true;
}

const handlePage = () => {
    seeOtherPage.value = true;
    homeViews.value = false;
}
</script>

<template>
    <div class="app-container">
        <div v-if="loginView" class="login-view">
            <div class="login-container">
                <form @submit.prevent="handleSubmit" class="login-form">
                    <h2>Login</h2>
                    <div class="form-group">
                        <label for="username">Username</label>
                        <input type="text" id="username" v-model="name" required placeholder="Enter your username">
                    </div>
                    <div class="form-group">
                        <label for="password">Password</label>
                        <input type="password" id="password" v-model="password" required placeholder="Enter your password">
                    </div>
                    <button type="submit" class="submit-btn">Login</button>
                </form>
            </div>
        </div>

        <div v-if="homeViews" class="home-view">
            <h1>Welcome, {{ name }}</h1>
            <button @click="handlePage" class="home-btn">Go to 2nd Homework</button>
        </div>

        <div v-if="seeOtherPage" class="other-page">
            <EventDemo />
        </div>
    </div>
</template>

<style scoped>
.app-container {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #f0f0f0;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px;
}

.login-view {
    width: 100%;
    max-width: 400px;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
    padding: 30px;
}

.login-container {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.login-form h2 {
    font-size: 24px;
    color: #333;
    margin-bottom: 20px;
}

.form-group {
    width: 100%;
    margin-bottom: 15px;
}

label {
    font-size: 14px;
    color: #666;
    margin-bottom: 5px;
    display: block;
}

input {
    width: 100%;
    padding: 12px;
    margin: 8px 0;
    border: 2px solid #ccc;
    border-radius: 8px;
    font-size: 16px;
    box-sizing: border-box;
}

input:focus {
    outline: none;
    border-color: #4CAF50;
}

.submit-btn {
    width: 100%;
    padding: 14px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.submit-btn:hover {
    background-color: #45a049;
}

.home-view h1 {
    font-size: 28px;
    color: #333;
    margin-bottom: 20px;
}

.home-btn {
    padding: 12px 20px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.home-btn:hover {
    background-color: #0056b3;
}

.other-page {
    margin-top: 30px;
    padding: 20px;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
    width: 100%;
    max-width: 600px;
    text-align: center;
}
</style>
