<script setup>
import { ref } from 'vue';
import { signup } from '../api/api';
import { useRouter } from 'vue-router';

const username = ref('');
const email = ref('');
const password = ref('');
const router = useRouter();

const signup_page = async () => {
    console.log("Attempting to sign up with:", username.value, email.value, password.value);

    const response = await signup(username.value, email.value, password.value);
    console.log("Response from signup:", response);
    if (response.success) {
        router.push({ name: 'Dashboard' });
    } else {
        alert("Signup failed: " + (response.error || "Unknown error"));
    }
};
</script>

<template>
    <div id="bdy">
        <div class="abstract-background"></div>
        <div class="signup-container">
            <header class="header">
                <h1 class="title">Greenhouse Farming System</h1>
                <p class="subtitle">Sign up to access your dashboard</p>
            </header>
            <form class="signup-form" @submit.prevent="signup_page">
              <input type="name" id="name" class="input-field" v-model="username" placeholder="Enter your name" required>
              <input type="email" id="email" class="input-field" v-model="email" placeholder="Enter your email" required>
                <input
                    type="password"
                    class="input-field"
                    v-model="password"
                    placeholder="Enter your password"
                    required
                />
                <button type="submit" class="button signup-button">Sign Up</button>
                <p class="signup-prompt">
                    Already have an account?
                    <router-link class="login-link" to="/login">Login here</router-link>
                </p>
            </form>
        </div>
    </div>
</template>

<style>
#bdy {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100vh;
    position: relative;
    font-family: 'Roboto', sans-serif;
    display: flex;
    align-items: center;
    justify-content: center;
}

.abstract-background {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, #ff8a00, #e52e71, #8921aa);
    z-index: -1;
    overflow: hidden;
}

.abstract-background::before,
.abstract-background::after {
    content: '';
    position: absolute;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 50%;
    pointer-events: none;
}

.abstract-background::before {
    width: 400px;
    height: 400px;
    top: -50px;
    left: -100px;
}

.abstract-background::after {
    width: 300px;
    height: 300px;
    bottom: -50px;
    right: -100px;
}

.signup-container {
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

.signup-form {
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

.login-link {
    color: #e52e71;
    font-weight: bold;
    text-decoration: none;
}

.login-link:hover {
    text-decoration: underline;
}
</style>
