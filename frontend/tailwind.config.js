/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.{js,ts}",
    "./plugins/**/*.{js,ts}",
    "./nuxt.config.{js,ts}",
    "./app.{js,ts,vue}",
    "./formkit.theme.ts"],
  darkMode: 'class',
  theme: {
    extend: {},
  },
  plugins: [],
}

