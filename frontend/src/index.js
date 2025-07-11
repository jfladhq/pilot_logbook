import React from 'react';
import { createRoot } from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './services/reportWebVitals';
import setupAxios from './services/setupAxios';
import { ToastContainer } from 'react-toastify';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'react-toastify/dist/ReactToastify.css';

setupAxios();

const container = document.getElementById('root');
const root = createRoot(container);
root.render(
    <React.StrictMode>
      <ToastContainer
        position='bottom-right'
        autoClose={5000}
        hideProgressBar={false}
        closeOnClick={true}
        pauseOnHover={true}
        draggable={true}
      />
      <App />
    </React.StrictMode>,
);
// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
