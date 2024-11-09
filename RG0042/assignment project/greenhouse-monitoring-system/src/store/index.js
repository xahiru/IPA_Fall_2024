import { createApp } from 'vuex';

export default createStore ({
    state: {
        isAuthenticated: !!localStorage.getItem("auth"),
        user: JSON.parse(localStorage.getItem("auth")) || null,
    },

    mutations: {
        login(state, userData) {
            state.isAuthenticated = true;
            state.user = userData;
            localStorage.setItem("auth", JSON.stringify(userData));
        },
        logout(state) {
            state.isAuthenticated = false;
            state.user = null;
            localStorage.removeItem("auth");
        },
    },

    actions: {
        login({ commit }, userData) {
            commit('login', userData);
        },
        logout({ commit }) {
            commit('logout');
        },
    },

    getters: {
        isAuthenticated: (state) => state.isAuthenticated,
        getUser: (state) => state.user,
    },
});