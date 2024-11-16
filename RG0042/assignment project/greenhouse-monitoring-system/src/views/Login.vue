<template>
    <div class="login-page">
      <div class="content-page">
        <h1>Login to Greenhouse Dashboard</h1>
        <form @submit.prevent="login">
          <div class="auth-buttons">
          <input type="text" v-model="username" placeholder="Username" />
          <br><br>
          <input type="password" v-model="password" placeholder="Password" />
          <br><br>
          <button type="submit">Login</button>
          <br>
          </div>
        </form>
  
          <p class="signup-prompt">Don't have an account? <a href="/signup" class="signup-link">Sign up here</a></p>
      </div>
    </div>  
</template>
    
    
<script>
    export default {
      data() {
        return { username: '', password: '' };
      },
      methods: {
        login() {
          // Mock login, store user in localStorage
          localStorage.setItem('auth', true);
          this.$router.push('/dashboard');
        },
      },
    };
</script>
    
  
<style scoped>
.login-page {
  background-image: url("src/assets/login-background.jpg");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.content-page {
  background: rgba(222, 230, 224, 0.2);
  padding: 2rem;
  border-radius: 12px;
  width: 100%;
  max-width: 400px;
  text-align: center;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

h1 {
  font-size: 6vw; /* Scales with screen size */
  margin-bottom: 20px;
  color: white;
}

.auth-buttons {
  margin-top: 1rem;
}

input {
  width: 100%;
  padding: 1rem;
  font-size: 1rem;
  margin: 0.5rem 0;
  border-radius: 8px;
  border: 1px solid #ccc;
  box-sizing: border-box;
}

button {
  width: 100%;
  margin: 0.5rem 0;
  padding: 0.75rem;
  font-size: 1rem;
  cursor: pointer;
  background-color: #3b82f6;
  color: white;
  border: none;
  border-radius: 8px;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #2563eb;
}

.signup-prompt {
  font-size: 1rem;
  color: white;
  margin-top: 1rem;
}

.signup-link {
  color: #3b82f6;
  text-decoration: underline;
}

@media (min-width: 768px) {
  .content-page {
    padding: 3rem;
  }
  h1 {
    font-size: 2.4rem;
  }
}

@media (max-width: 480px) {
  .content-page {
    padding: 1.5rem;
  }
  input,
  button {
    padding: 0.75rem;
  }
  h1 {
    font-size: 5vw;
  }
}
</style>