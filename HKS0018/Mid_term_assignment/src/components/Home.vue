<template>
  <div class="home">
    <div class="header">
      <h1>GreenHouse Farming System</h1>
      <div class="auth-buttons">
        <router-link to="/login">
          <button>Login</button>
        </router-link>
        <router-link to="/signup">
          <button>Sign Up</button>
        </router-link>
      </div>
    </div>
    <div class="content">
      <p>
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias nobis
        assumenda repellat sequi ut sit reiciendis cum. Cupiditate temporibus
        saepe nihil dolorem esse ut adipisci nobis, veniam quod, officiis
        accusantium!
      </p>
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
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f4f4f4;
  padding: 0 20px;
  font-family: 'Roboto', sans-serif;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  max-width: 1200px;
  margin-bottom: 40px;
}

.header h1 {
  font-size: 3rem;
  color: #42b983;
  font-weight: bold;
  margin: 0;
  letter-spacing: 2px;
  text-transform: uppercase;
}

.auth-buttons {
  display: flex;
  gap: 20px;
}

button {
  padding: 12px 25px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 30px;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.3s ease;
}

button:hover {
  background-color: #369970;
  transform: translateY(-3px);
}

button:active {
  transform: translateY(1px);
}

.content {
  background: #ffffff;
  border-radius: 10px;
  padding: 30px;
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.1);
  max-width: 800px;
  width: 100%;
  text-align: center;
}

p {
  font-size: 1.2rem;
  color: #555;
  line-height: 1.6;
  margin-top: 20px;
}

@media (max-width: 768px) {
  .header {
    flex-direction: column;
    align-items: center;
    text-align: center;
  }

  .auth-buttons {
    margin-top: 20px;
    flex-direction: column;
    gap: 15px;
  }

  h1 {
    font-size: 2.5rem;
  }

  .content {
    padding: 20px;
  }

  p {
    font-size: 1rem;
  }
}
</style>
