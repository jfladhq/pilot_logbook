import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  build: { // to output your build into build dir the same as Webpack
    outDir: 'build',
    sourcemap: true,
  },
  resolve: {
    alias: [
      {
        find: '@',
        replacement: '/src',
      },
      {
        find: '@images',
        replacement: '/src/images',
      },
      {
        find: '@components',
        replacement: '/src/components',
      },
      {
        find: '@pages',
        replacement: '/src/pages',
      },
      {
        find: '@services',
        replacement: '/src/services',
      },
      {
        find: '@api',
        replacement: '/src/api',
      },

    ],
  },
  server: {
    open: true,
    port: 3000,
  },
})