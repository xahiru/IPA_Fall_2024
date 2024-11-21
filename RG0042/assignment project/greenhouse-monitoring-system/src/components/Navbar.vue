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

    methods: {
        logout() {
        localStorage.removeItem('isAuthenticated');
        this.$router.push('/login');    
    },
  }
};
</script>

<style scoped>
.navbar {
    display: flex;
    justify-content: space-between;
    align-content: center;
    padding: 1rem;
    background-color: #3b82f6;
    color: white;
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