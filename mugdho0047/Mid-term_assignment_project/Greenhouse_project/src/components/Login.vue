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
        <div class="abstract-background"></div>
        <div class="login-container">
            <header class="header">
                <h1 class="title">Greenhouse Farming System</h1>
                <p class="subtitle">Login to access your dashboard</p>
            </header>
            <form class="login-form" @submit.prevent="login_page">
              <input type="email" id="email" class="input-field" placeholder="Enter your email" required>
                <input
                    type="password"
                    v-model="password"
                    class="input-field"
                    placeholder="Enter your password"
                    required
                />
                <button type="submit" class="button login-button">Login</button>
                <p class="signup-prompt">
                    Don't have an account?
                    <a href="/signup" class="signup-link">Sign up here</a>
                </p>
            </form>
        </div>
    </div>
</template>

<style>
#bdy {
    position: relative;
  background-color: #f4f7fc;
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
}

.login-container {
    text-align: center;
    background: rgba(255, 255, 255, 0.9);
    padding: 40px;
    border-radius: 15px;
    box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.2);
    max-width: 400px;
    width: 90%;
}

.header .title {
    font-size: 2rem;
    font-weight: bold;
    color: #333;
}

.header .subtitle {
    font-size: 1rem;
    color: #666;
    margin-top: 10px;
}

.login-form {
    margin-top: 20px;
    display: flex;
    flex-direction: column;
    gap: 20px;
}

.input-field {
    padding: 12px 15px;
    font-size: 1rem;
    border: 1px solid #ccc;
    border-radius: 8px;
    outline: none;
    transition: all 0.3s ease;
}

.input-field:focus {
    border-color: #e52e71;
    box-shadow: 0px 0px 5px rgba(229, 46, 113, 0.5);
}

.button {
    padding: 12px 20px;
    font-size: 1rem;
    font-weight: 600;
    color: #fff;
    background: #e52e71;
    border: none;
    cursor: pointer;
    border-radius: 8px;
    transition: background 0.3s ease;
}

.button:hover {
    background: #ff8a00;
}

.signup-prompt {
    margin-top: 15px;
    font-size: 0.9rem;
    color: #555;
}

.signup-link {
    color: #106cc8;
    font-weight: bold;
    text-decoration: none;
}

.signup-link:hover {
    text-decoration: underline;
}
</style>