<template>
    <div>
      <h1>GreenHouse Farming system</h1>
      <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Alias nobis assumenda repellat sequi ut sit reiciendis cum. Cupiditate temporibus saepe nihil dolorem esse ut adipisci nobis, veniam quod, officiis accusantium!</p>
      <router-link to="/login">
        <button>Login</button>
      </router-link>
      <router-link to="/signup">
        <button>Sign Up</button>
      </router-link>
    </div>
  </template>
  
  <script>
  export default {
    name: "Home",
  };
  </script>
  
  <style>
  button {
    margin: 10px;
    padding: 10px 20px;
    background-color: #42b983;
    color: white;
    border: none;
    cursor: pointer;
  }
  button:hover {
    background-color: #369970;
  }
  </style>
  