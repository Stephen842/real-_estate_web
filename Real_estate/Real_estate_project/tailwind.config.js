/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './estates/templates/pages/*.html',
  ],
  theme: {
    extend: {
      colors: {
        'light-grey': '#cccfd1',
        'coral-pink': '#ff7474',
      },
      fontFamily: {
        'magnolia': ['Magnolia Script', 'cursive'],
      },
    },
  },
  plugins: [],
}