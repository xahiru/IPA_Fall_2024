<template>
    <nav class="navbar">
        <router-link to="/" class="logo">Greenhouse Dashboard</router-link>
        <div class="nav-links">
            <router-link to="/overview">Overview</router-link>
            <router-link to="/settings">Settings</router-link>
            <router-link to="/logs">Logs</router-link>
            <router-link to="/login">Logout</router-link>
        </div>
    </nav>
</template>

<script>
export default {
    name: "navbar",
}
</script>

<style scoped>
.navbar {
    display: flex;
    justify-content: space-between;
    align-content: center;
    padding: 1rem;
    background-color: white;
}

.logs {
    font-size: 1.5rem;
    font-weight: bold;
    color: white;
    text-decoration: none;

}

.nav-links {
    margin: 0 1rem;
    color: white;
    text-decoration: none;
}

.nav-links a:hover {
    text-decoration: underline;
}
</style>