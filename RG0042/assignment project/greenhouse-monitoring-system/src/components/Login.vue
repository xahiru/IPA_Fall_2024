<template>
    <div class="login-page">
        <h2>Login to Greenhouse Dashboard</h2>
        <from @submit.prevent ="handelLogin">
            <div class="from-group">
                <label for="email">Email</label>
                <input v-model="email" type="email" required />
            </div>

            <div class="from-group">
                <label for="password">Password</label>
                <input v-model="password" type="password" required/>
            </div>

            <button type="submit">Login</button>
        </from>
        <p>
            Don't have an account? <router-link to="/signup">Sign up here</router-link>
        </p>
    </div>
</template>

<script>
import { useMainStore } from '../store';

export default {
    name: 'Login',
    data () {
        return{
            email: '',
            password: '',
        };
    },
    methods: {
        async handelLogin() {
            const store = useMainStore();
            try {
                await store.login(this.email, this.password);
                this.$router.push('/dashboard');
            } catch (error) {
                alert('Login failed: ' + error.message);
            }
        },
    },
};
</script>


<style  scoped>
.login-page {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    background-color: #f0f4f8;
    padding: 1rem;
}
h2 {
    margin-bottom: 1.5rem;
    color: #333;
}

form {
    display: flex;
    flex-direction: column;
    width: 100%;
    max-width: 400px;
    padding: 2rem;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
}

.from-group {
    margin-bottom: 15px;
    text-align: left;
}
label {
    display: block;
    font-weight: bold;
    margin-bottom: 0.25rem;
    color: #333;
}
input {
    width: 100%;
    padding: 0.75rem;
    border-radius: 4px;
    border: 1px solid #ccc;
    font-size: 1rem;
}

button {
    margin-top: 1rem;
    padding: 0.75rem;
    font-size: 1rem;
    color: #fff;
    background-color: #007bff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

button:hover {
    background-color: #0056b3;
}

p {
    margin-top: 1rem;
    color: #333;
}
a {
    color: #007bff;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}
</style>