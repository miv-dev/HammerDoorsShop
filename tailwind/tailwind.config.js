/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    '../templates/**/*.html',
    './node_modules/flowbite/**/*.js'

  ],
  theme: {
    extend: {},
    colors: {
      'black': '#030303',
      'primary': '#3164F4',
      'primary-900': '#042684',
      'accent': '#FFB51A',
      'white': "#fff",
      'gray': "#EDEDED"
    },
  },
  plugins: [
    require('flowbite/plugin')

  ],
}

