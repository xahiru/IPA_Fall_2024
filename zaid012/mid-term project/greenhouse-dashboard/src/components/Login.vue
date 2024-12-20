<script setup>
import { ref } from 'vue';
import { login } from '../api/api';

const email = ref('');
const password = ref('');

const login_page = async () => {
    const response = await login(email.value, password.value);
    if (response.success) {
        window.location.href = '/dashboard';
    } else {
        alert("Login failed: " + (response.error || "Unknown error"));
    }
};
</script>

<template>
    <div id="bdy">
        <div class="login-page">
            <header class="header">
                <h1 class="title">Greenhouse Farming System</h1>
                <p class="subtitle">Login to see your dashboard</p>
            </header>

            <form class="login-form" @submit.prevent="login_page">
                <label for="email">Email</label>
                <input type="email" id="email" class="input-field" v-model="email" placeholder="Enter your email" required />

                <label for="password">Password</label>
                <input type="password" id="password" class="input-field" v-model="password" placeholder="Enter your password" required />

                <button type="submit" class="button login-button">Login</button>

                <p class="signup-prompt">
                    Don't have an account?
                    <router-link class="signup-link" to="/signup">Sign up here</router-link>
                </p>
            </form>
        </div>
    </div>
</template>

<style>
#bdy {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, #00cec4, #083ab7);
    font-family: 'Poppins', sans-serif;
}

.login-page {
    max-width: 400px;
    width: 100%;
    text-align: center;
    background: rgba(0, 210, 56, 0.2);
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
}

.header {
    margin-bottom: 20px;
}

.title {
    font-size: 2rem;
    font-weight: bold;
    color: #474747;
    text-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
}

.subtitle {
    font-size: 1rem;
    color: #d1cfe2;
    margin-top: 5px;
}

.login-form {
    display: flex;
    flex-direction: column;
    gap: 15px;
}

.input-field {
    padding: 12px 15px;
    font-size: 1rem;
    border: 1px solid #d1cfe2;
    border-radius: 8px;
    outline: none;
    background: rgba(255, 255, 255, 0.9);
    transition: border-color 0.3s;
}

.input-field:focus {
    border-color: #006adb;
    background: #ffffff;
}

.button {
    padding: 12px 20px;
    font-size: 1rem;
    font-weight: 600;
    color: white;
    background: linear-gradient(90deg, #00b3ff, #00ffee);
    border: none;
    cursor: pointer;
    border-radius: 8px;
    transition: transform 0.2s, background-color 0.3s;
}

.button:hover {
    transform: scale(1.05);
    background: linear-gradient(90deg, #0077ff, #2d009f);
}

.signup-prompt {
    font-size: 0.9rem;
    color: #d1cfe2;
    margin-top: 20px;
}

.signup-link {
    color: #ffffff;
    font-weight: 600;
    text-decoration: underline;
    transition: color 0.3s;
}

.signup-link:hover {
    color: #00ffdd;
}
</style>