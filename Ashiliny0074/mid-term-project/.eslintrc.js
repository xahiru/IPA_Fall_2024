module.exports = {
  root: true,
  env: {
    node: true,
  },
  extends: [
    "plugin:vue/vue3-essential",
    "eslint:recommended",
    "@vue/typescript/recommended",
  ],
  parserOptions: {
    ecmaVersion: 2020,
  },
  rules: {
    "no-console": process.env.NODE_ENV === "production" ? "warn" : "off",
    "no-debugger": process.env.NODE_ENV === "production" ? "warn" : "off",
    "prettier/prettier": "off", // Disable Prettier formatting
    "vue/multi-word-component-names": "off", // Disable component naming rule
    "@typescript-eslint/no-unused-vars": "off", // Disable unused variables warning
    "@typescript-eslint/no-explicit-any": "off", // Disable explicit any warning
    "@typescript-eslint/no-empty-function": "off", // Disable empty function warning
  },
};