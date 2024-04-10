import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'

import { ThemeProvider } from "@material-tailwind/react";
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";

import Registration from './components/auth/Register.jsx';
import LogIn from './components/auth/Login.jsx';
import Categories from './components/categories/Categories.jsx';
import Dashboard from './components/dashboard/Dashboard.jsx';
import Expenses from './components/expenses/Expenses.jsx';
import Analytics from './components/contents/Analytics.jsx';
import Logout from './components/auth/Logout.jsx';


const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
  },
  {
    path: "signup",
    element: <Registration />,
  },
  {
    path: "login",
    element: <LogIn />,
  },
  {
    path: "dashboard",
    element: <Dashboard />
  },
  {
    path: "categories",
    element: <Categories />
  },
  {
    path: "expenses",
    element: <Expenses />
  },
  {
    path: "analytics",
    element: <Analytics />
  },
  {
    path: "logout",
    element: <Logout />
  }
]);


ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <ThemeProvider>
      <RouterProvider router={router} />
    </ThemeProvider>
  </React.StrictMode>,
)
