<template>
    <div class="home">
        <h1> Welcome to the Greenhouse Monitoring System</h1>
        <p>Moritor and manage your greenhouse environment sfficiently</p>
    <div class="navigation-link">
        <router-link to="/login" class="btn">Login</router-link>
        <router-link to="/signup" class="btn">signup</router-link>
    </div>
    </div>
</template>

<script> 
export default {
    name: "Home",
};
</script>

<style scoped>
.home {
    text-align: center;
    margin-top: 50px;
}
h1 {
    font-size: 2em;
    margin-bottom: 30px;
}
p {
    font-size: 1.2em;
    margin-bottom: 30px;
}

.navigation-linkn.btn {
    margin: 0 10px;
    padding: 10px 20px;
    background-color: white;
    text-decoration: none;
    border-radius: 5px;
}
.navigation-linkn.btn:hover {
    background-color: #330588;
}
</style>