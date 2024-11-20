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
          <P v-if="errorMeassage" class="error-meassage">{{ errorMeassage }}</P>
      </div>
    </div>  
</template>
    
    
<script>
import axios from "axios";

export default {
  data() {
    return {
      username: "",
      password: "",
      errorMessage: "",
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.get('http://localhost:3001/users', {
          params: { username: this.username, password: this.password }
        });

        if (response.data.length === 1) {
          const user = response.data[0];
          localStorage.setItem('auth', true);
          localStorage.setItem('user', JSON.stringify(user));
          this.$router.push('/dashboard');
        } else {
        
          this.errorMessage = 'Invalid username or password';
        }
      } catch (error) {
        console.error('Login failed:', error);
        this.errorMessage = 'Something went wrong. Please try again.';
      }
    }
  }
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
  max-width: 325px;
  text-align: center;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

h1 {
  font-size: 6vw;
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