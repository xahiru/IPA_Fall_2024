<template>
    <div class="home-page">      
        <div class="content-page">
    <header>
      <h1>Welcome to the Greenhouse Monitoring System</h1>
      <p>Monitor and manage your Greenhouse environment easily</p>
    </header>

    <section>
      <div class="auth-buttons">
      <router-link to="/login">
        <button>Login</button></router-link>
      <router-link to="/signup">
        <button>Sign Up</button></router-link>
        </div>
    </section> 
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
    background-image: url("src/assets/home-background.png");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    height: 100vh;
    
    display: flex;
    flex-direction: column;
    text-align: center;
    align-items: center;
}

.content-page {
    background: rgba(222, 230, 224, 0.077);
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    text-align: center;
    width: 100%;
    max-width: 350px;
}
h1 {
    text-align: center;
    color: white;
    font-family: 'Times New Roman', Times, serif;
}
p {
    text-align: center;
    color: black;
}
.auth-buttons{
    padding: 0.5rem 1.5rem;
    color: white;
    border-radius: 8px;
    text-decoration: none;
    font-size: 1rem;
    transition: background-color 0.3s;
    justify-content: center;
    gap: 1rem;
}

button {
    margin: 0.5rem;
    padding: 0.75rem 1.5rem;
    font-size: 1rem;
    cursor: pointer;
    align-items: center;
    text-align: center;
    color: rgb(251, 248, 255);
    background-color: rgb(117, 212, 141);
    border-radius: 5px;
}

button:hover {
    background-color: rgb(87, 162, 105);;
}

@media (max-width: 768px) {
    .content-page{
        padding: 15px;
    }
    h1 {
        font-size: 1.5rem;
    }
    p {
        font-size: 1rem;
    }

    .auth-buttons {
        flex-direction: column;
        gap: 1rem;
        width: 100%;
    }
    button {
        width: 100%;
        padding: 1rem;
        font-size: 1.2rem;
    }
}

@media (max-width: 480px) {
    h1 {
        font-size: 1.2rem;
    }
    p {
       font-size: 0.9rem; 
    }

    .auth-buttons {
        gap: 0.8rem;
    }
    button {
        font-size: 1rem;
    }
}
</style>