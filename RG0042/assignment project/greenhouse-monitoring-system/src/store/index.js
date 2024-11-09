

export const useMainStore = defineStore ({
    id: 'main',
    state: () => ({
        isAuthenticated: false,
        user: null,
    }),

    actions: {
        async login(email, password) {
            if(email === 'user@example.com' && password === 'password'){
                this.isAuthenticated = true;
                this.user = { email };
            } else {
                throw new Error('Invalid User');
            }
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