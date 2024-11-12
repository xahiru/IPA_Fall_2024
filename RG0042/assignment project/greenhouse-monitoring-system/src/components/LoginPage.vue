<template>
    <div class="login-page">
        <h2>Login to Greenhouse Dashboard</h2>
        <from @submit.prevent ="handelLogin">
            <div class="from-group">
                <label for="email">Email</label>
                <input v-model="email" id="email" type="email" placeholder="Enter your email" required/>
            </div>

            <div class="form-group">Password
                <label for="password">Password</label>
                <input v-model="password" id="password" type="password" placeholder="Enter your password" required/>
            </div>

            <button type="submit" class="btn">Login</button>
        </from>
        <p>
            Don't have an account? <router-link to="/signup" class="sihnup-link">Sign up here</router-link>
        </p>
    </div>
</template>

<script>
export default {
    name: "LoginPage",
    data () {
        return{
            email: "",
            password: ""
        };
    },
    methods: {
        handelLogin() {
            // Mock login logic (replace with api call if needed)
            if (this.email && this.password){
                localStorage.setItem("auth", JSON.stringify({ email: this.email }));
                this.$router.push("/dashboard"); // redirect to dashboard
            } else {
                alert("Please enter valid information");
            }
        }
    }
};
</script>

<style  scoped>
.login-page {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    text-align: center;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    background-color: #f9f9f9;
}
h2 {
    font-size: 1.8em;
    margin-bottom: 20px;
}

.from-group {
    margin-bottom: 15px;
    text-align: left;
}
label {
    display: block;
    font-weight: bold;
    margin-bottom: 5px;
}
input {
    width: 100%;
    padding: 10px;
    border-radius: 4px;
    border: 1px solid #ccc;
}

.bta {
    width: 100%;
    padding: 10px;
    background-color: #634caf;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

.btn:hover {
    background-color: #4726a4;
}

.signup-link {
    color: #4726a4;
    text-decoration: none;
}

.signup-link:hover {
    text-decoration: underline;
}
</style>