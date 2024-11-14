module.exports = {
  content: [
    './index.html',
    './src/**/*.{vue,js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {},
    backgroundImage: {
      'home-bg': "url('@/assets/home-background.png')",
      'login-bg': "url('@/assets/login-background.jpg')",
      'signup-bg': "url('@/assets/signup-background.jpg')",
    }
  },
  plugins: [],
};

