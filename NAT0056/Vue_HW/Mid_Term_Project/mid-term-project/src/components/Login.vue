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
            <div class="welcome-message">
                <h3>Welcome Back!</h3>
            </div>
            <header class="header">
                <h2 class="title">Greenhouse Farming System</h2>
                <p class="subtitle">Login to access your Account</p>
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
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, #20c97a, #4c324f);
    font-family: 'Poppins', sans-serif;
}

.login-page {
    max-width: 350px;
    width: 100%;
    text-align: center;
    background: rgba(255, 255, 255, 0.2);
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
}
.welcome-message {
    text-align: center;
    margin-bottom: 20px;
}

.welcome-message h3 {
    font-size: 1.5rem;
    color: #a5d07c;
    font-weight: 600;
    margin-bottom: 10px;
    text-shadow: 0 2px 8px rgba(167, 57, 177, 0.293);
}

.header {
    margin-bottom: 20px;
}

.title {
    font-size: 2rem;
    font-weight: bold;
    color: #ffffff;
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
    border: 1px solid #f5f5eb;
    border-radius: 8px;
    outline: none;
    background: rgba(255, 255, 255, 0.9);
    transition: border-color 0.3s;
}

.input-field {
    padding: 12px 15px;
    font-size: 1rem;
    border: 1px solid #f5f5eb;
    border-radius: 8px;
    outline: none;
    background: rgba(255, 255, 255, 0.9);
    color: #333333; /* Text color inside the input fields */
    transition: border-color 0.3s, color 0.3s;
}

.input-field:focus {
    border-color: #6c63ff;
    background: #ffffff;
    color: #333333; /* Ensure text color remains the same when focused */
}


.button {
    padding: 12px 20px;
    font-size: 1rem;
    font-weight: 600;
    color: white;
    background: linear-gradient(90deg, #6c63ff, #a084dc);
    border: none;
    cursor: pointer;
    border-radius: 8px;
    transition: transform 0.2s, background-color 0.3s;
}

.button:hover {
    transform: scale(1.05);
    background: linear-gradient(90deg, #076322, #26a60d);
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
    color: #e68c66;
}
</style>