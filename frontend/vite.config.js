/* eslint-disable no-undef */
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react-swc';
import path from 'path';

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: [
      {
        find: '@images',
        replacement: path.resolve(__dirname, './src/images'),
      },
      {
        find: '@components',
        replacement: path.resolve(__dirname, './src/components'),
      },
      {
        find: '@pages',
        replacement: path.resolve(__dirname, './src/pages'),
      },
      {
        find: '@services',
        replacement: path.resolve(__dirname, './src/services'),
      },
      {
        find: '@api',
        replacement: path.resolve(__dirname, './src/api'),
      },

    ],
  },
  preview: {
    port: 9004,
    strictPort: true,
  },
  server: {
    port: 9004,
    strictPort: true,
    host: true,
    origin: 'http://localhost:9004',
  },
  base: '/',
})