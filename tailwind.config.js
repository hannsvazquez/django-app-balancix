/** @type {import('@tailwindcss/cli').Config} */
export default {
  content: [
    "./templates/**/*.html",
    "./internships/templates/**/*.html",
    "./static/**/*.js",
  ],
  theme: {
    extend: {
      fontFamily: {
        'sans': ['Red Rose Variable', 'ui-sans-serif', 'system-ui', 'sans-serif'],
        'red-rose': ['Red Rose Variable', 'serif'],
      },
    },
  },
  plugins: [require('daisyui')],
  daisyui: {
    themes: ["night"],
  },
} 