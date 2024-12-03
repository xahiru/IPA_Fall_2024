import axios from 'axios';

const API_URL = "http://localhost:5173/user"; 


//for signup funtionality
export const signup = async (username, email, password) => {
  try {
    if (!username || !email || !password) {
      return { success: false, error: "All fields are required." };
    }

    const response = await axios.post(API_URL, { username, email, password });

    if (response.status === 201) {
      localStorage.setItem("user", JSON.stringify(response.data));
      return { success: true };
    } else {
      return { success: false, error: "Signup failed. Please try again." };
    }
  } catch (error) {
    console.error("Signup Error: ", error);
    return {
      success: false,
      error: error.response?.data?.message || "Network Error. Please try later.",
    };
  }
};

//for login functionality
export const login = async (email, password) => {
  try {
    if (!email || !password) {
      return { success: false, error: "Email and password are required." };
    }

    const response = await axios.get(API_URL, {
      params: { email, password },
    });

    if (response.data.length > 0) {
      localStorage.setItem("user", JSON.stringify(response.data[0]));
      return { success: true };
    } else {
      return { success: false, error: "Invalid email or password." };
    }
  } catch (error) {
    console.error("Login Error: ", error);
    return {
      success: false,
      error: error.response?.data?.message || "Network Error. Please try later.",
    };
  }
};
