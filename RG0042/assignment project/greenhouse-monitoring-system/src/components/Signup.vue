<template>
    <div class="signup-page">
        <h2>Create an account</h2>
        <from @submit.prevent="handleSignup">
            <div>
                <label for="name">Name</label>
                <input type="text" v-model="name" required />
            </div>
            <div>
                <label for="email">Email</label>
                <input type="email" v-model="email" required/>
            </div>

            <div>
                <label for="password">Password</label>
                <input type="password" v-model="password" required/>
            </div>


            <button type="submit">Register</button>
        </from>
        <p>
            Already have an account? <router-link to="/login">Login here</router-link>
        </p>
    </div>
</template>

<script> 
import { useMainStore } from '../store';

export default {
    name: "Signup",
    data() {
        return {
            name: '',
            email: '',
            password: '',
        };
    },
    
    methods: {
        async handleSignup() {
            const store = useMainStore();
            try {
                await store.register(this.name, this.email, this.password);
                this.$router.push('/login');
            } catch (error) {
                alert('Registration failed: ' + error.message);
            }
        },
    },
};
</script>


<style scoped>
.signup-page {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 2rem;        
}
h2 {
    font-size: 1.8em;
    color: #333;
    margin-bottom: 20px;
}

form {
    display: flex;
    flex-direction: column;
    width: 100%;
    max-width: 400px;
    background-color: #f9f9f9;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

form div {
    margin-bottom: 1rem
}

label {
    display: inline-block;
    font-weight: bold;
    margin-bottom: 0.25rem;
    color: #555;
}

input[type="text"],
input[type="email"],
input[type="password"] {
    width: 100%;
    padding: 0.75rem;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 1rem;
}

button {
    background-color: #8e1bd5;
    color: #fff;
    padding: 0.75rem;
    font-size: 1rem;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-weight: 600;
    transition: background-color 0.3s;
}

button:hover {
    background-color: #8e1bd5;
}

p {
    margin-top: 1rem;
    color: #666;
}
a {
    color: #007bff;
    text-decoration: none;
}
a:hover {
    text-decoration: underline;
}
</style>