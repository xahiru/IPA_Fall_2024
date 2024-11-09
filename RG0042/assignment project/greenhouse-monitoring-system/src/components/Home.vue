<template>
    <div class="home-page">
        <h1> Welcome to the Greenhouse Monitoring System</h1>
        <p>Moritor and manage your greenhouse environment easily</p>
    <div class="auth-buttons">
        <router-link to="/login">
            <button>Login</button></router-link>
        <router-link to="/signup">
            <button>Register</button></router-link>
    </div>
    </div>
</template>

<script> 
export default {
    name: "Home",
};
</script>

<style scoped>
.home-page {
    display: flex;
    flex-direction: column;
    text-align: center;
    align-items: center;
    padding: 2rem;
}
h1 {
    font-size: 2em;
    margin-bottom: 30px;
}
p {
    font-size: 1.2em;
    margin-bottom: 30px;
}

.auth-buttons{
    margin-top: 1.5rem;
}

button {
    margin: 0.5rem;
    padding: 0.75rem 1.5rem;
    font-size: 1rem;
    cursor: pointer;
}
</style>