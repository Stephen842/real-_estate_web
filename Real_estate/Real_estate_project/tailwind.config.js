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
        'darkBlue': '#1E3A8A',
        'darkRed': '#8B0000',
      },
      fontFamily: {
        'magnolia': ['Magnolia Script', 'cursive'],
      },
    },
  },
  plugins: [],
}