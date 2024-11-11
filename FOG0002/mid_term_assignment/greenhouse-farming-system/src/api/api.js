import axios from 'axios';

export const signup = async (username, email, password) => {
    try {
        const result = await axios.post("http://localhost:3000/user", {
            username, email, password
        });

        if (result.status === 201) {
            localStorage.setItem("user", JSON.stringify(result.data));
            return { success: true };
        } else {
            return { success: false };
        }
    } catch (error) {
        console.error("Sign-up Error: ", error.response ? error.response.data : error.message);
        return { success: false, error: error.response ? error.response.data : error.message };
    }
};
