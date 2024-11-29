<template>
    <div class="signup-page">
        <h2>Create an account</h2>
        <from @submit.prevent="handleSignup">
            <div class="from-group">
                <label for="email">Email</label>
                <input v-model="email" id="email" type="email" placeholder="Enter your email" required/>
            </div>

            <div class="from-group">
                <label for="password">Password</label>
                <input v-model="password" id="password" type="password" placeholder="Enter your password" required/>
            </div>

            <div class="from-group">
                <label for="confirmPassword">Confrom Password</label>
                <input v-model="confirmPassword" id="confirmPassword" type="password" placeholder="Confirm your password" required/>
            </div>

            <button type="submit" class="btn">Sign Up</button>
        </from>
        <p>
            Already have an account? <router-link to="/login" class="login-link">Login here</router-link>
        </p>
    </div>
</template>

<script> 
export default {
    name: "SignupPage",
    data() {
        return {
            email: "",
            password: "",
            confirmPassword: ""
        };
    },
    
    methods: {
        handleSignup() {
            // check if passwords match
            if (this.password !== this.confirmPassword){
                alert("Password do not match");
                return;
            }

            // Mock signup logic (replace with API call if needed)
            if(this.email && this.password){
                localStorage.setItem("auth", JSON.stringify({ email: this.email}));
                this.$router.push("/dashboard"); //redirect to dashboard
            } else {
                alert("Please fill in all fields");
            }
        }
    }
};
</script>


<style scoped>
.signup-page {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    text-align: center;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    background-color: rgba(154, 40, 221, 0.801);
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

.btn {
    width: 100%;
    padding: 10px;
    background-color: rgba(140, 0, 255, 0.948);
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

.btn:hover {
    background-color: #8e1bd5;
}

.login-link {
    color: #8e1bd5;
    text-decoration: none;
}

.login-link:hover {
    text-decoration: underline;
}
</style>