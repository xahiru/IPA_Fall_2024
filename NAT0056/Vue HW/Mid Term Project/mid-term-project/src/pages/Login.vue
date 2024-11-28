<template>
    <div class="row">
        <div class="row col-md-6 0ffset-md-3">
            <div>
        <div>
            <h3>Login</h3>
            <hr/>
        </div>
        <form>
            <div class="form-group">
                <lebel>Email</lebel>
                <input type="text" class="form-control"/>
            </div>
            <div class="form-group">
                <lebel>Password</lebel>
                <input type="password" class="form-control"/>
            </div>
            <div class="my-3">
                <button type="submit" class="btn btn-primary">
                    Login
                </button>
            </div>
        </form>
    </div>
        </div>
    </div>
   
  </template>
  
  <script>
  export default {
    name: 'UserLogin',
  };
  </script>

  <style scoped>
  .login-container {
    max-width: 400px;
    margin: 0 auto;
    padding: 2rem;
    background-color: #752222; /* Light grey background */
    border-radius: 8px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  }
  
  .login-form {
    display: flex;
    flex-direction: column;
  }
  
  .form-group {
    margin-bottom: 1.5rem;
  }
  
  .form-group label {
    display: block;
    font-size: 1.1rem;
    color: #b3a5a5;
    margin-bottom: 0.5rem;
  }
  
  .form-control {
    width: 100%;
    padding: 0.75rem;
    font-size: 1rem;
    border: 1px solid #862727;
    border-radius: 4px;
    box-sizing: border-box;
    background-color: #fff; /* White background for inputs */
    color: #333; /* Dark text color */
  }
  
  /* Input field focus state */
  .form-control:focus {
    border-color: #007bff; /* Blue border on focus */
    outline: none;
  }
  
  /* Button styling */
  .btn {
    padding: 0.75rem 1.25rem;
    background-color: #7516ce; /* Blue button */
    color: rgb(211, 184, 184);
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 1rem;
    width: 100%;
  }
  
  .btn:hover {
    background-color: #475e76; /* Darker blue on hover */
  }
  
  /* Space between elements */
  .my-3 {
    margin-top: 1.5rem;
  }
  </style>
  