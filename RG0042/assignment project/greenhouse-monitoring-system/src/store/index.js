import { defineStore } from 'pinia';

export const useMainStore = defineStore ({
    id: 'main',
    state: () => ({
        isAuthenticated: false,
        user: null,
    }),

    actions: {
        login(userData) {
                this.isAuthenticated = true;
                this.user = userData;
        },
        logout() {
            this.isAuthenticated = false;
            this.user = null;
        },
    },    
});

 ({
    actions: {
        async register(name, email, password) {
            if(email && password) {
                console.log('User registered with name: ${name}, email: {email},');
            } else {
                throw new Error('invalid registration details');
            }
        },
    },
});