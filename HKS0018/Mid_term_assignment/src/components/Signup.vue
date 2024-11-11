<template>
  <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="handleSignUp">
      <div>
        <label for="username">Username:<br></label>
        <input
          type="text"
          id="username"
          v-model="username"
          placeholder="Enter your username"
          required
        />
      </div>

      <div>
        <label for="email">Email:<br></label>
        <input
          type="email"
          id="email"
          v-model="email"
          placeholder="Enter your email"
          required
        />
      </div>

      <div>
        <label for="password">Password:<br></label>
        <input
          type="password"
          id="password"
          v-model="password"
          placeholder="Enter your password"
          required
        />
      </div>

      <div>
        <label for="confirmPassword">Confirm Password:</label>
        <input
          type="password"
          id="confirmPassword"
          v-model="confirmPassword"
          placeholder="Confirm your password"
          required
        />
      </div>

      <button type="submit">Sign Up</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "SignUp",
  data() {
    return {
      username: "",
      email: "",
      password: "",
      confirmPassword: "",
    };
  },
  methods: {
    handleSignUp() {
      if (this.username && this.email && this.password && this.confirmPassword) {
        if (this.password === this.confirmPassword) {
          alert(`Signing up with Username: ${this.username}, Email: ${this.email}`);

          this.username = "";
          this.email = "";
          this.password = "";
          this.confirmPassword = "";

          this.$router.push({ name: 'Login' });
        } else {
          alert("Passwords do not match.");
        }
      } else {
        alert("Please fill in all fields.");
      }
    },
  },
};
</script>

<style>
form {
  background-color: #369970;
  display: flex;
  flex-direction: column;
  width: 300px;
  margin: 20px auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 5px;
}
label {
  margin-top: 10px;
  font-weight: bold;
}
input {
  margin: 5px 0 15px;
  padding: 8px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
}
button {
  padding: 10px;
  background-color: #42b983;
  color: white;
  font-weight: bold;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
button:hover {
  background-color: #369970;
}
</style>
