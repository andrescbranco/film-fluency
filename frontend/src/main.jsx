import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import Home from './Home.jsx'
import Login from './Login.jsx'
import UserProfile from './UserProfile.jsx'
import CreateProfile from './CreateProfile.jsx'
import Vocabulary from './Vocabulary.jsx'
import Grammar from './Grammar.jsx'
import SelectLanguage from './SelectLanguage.jsx'
import Listening from './Listening.jsx'

import { createBrowserRouter, RouterProvider } from "react-router-dom";



const routes = createBrowserRouter([
    {
      path: "/",
      element: <App />,
      errorElement: <h1>Something went wrong!</h1>,
      children: [
        {
          path: "/",
          element: <SelectLanguage />,
        },
        {
          path: "/login",
          element: <Login />
        },
        {
          path:"/user",
          element: <UserProfile />
        },
        {
          path: "/createprofile",
          element: <CreateProfile />
        },
        {
          path:"/home",
          element:<Home/>
        },
        {
          path:'/vocabulary',
          element:<Vocabulary/>
        },
        {
          path:'/grammar',
          element:<Grammar/>
        },
        {
          path:'/select-language',
          element:<SelectLanguage/>
        },
        {
          path:'/listening',
          element:<Listening/>
        }

      ]
    }]);

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
     <RouterProvider router={routes} />
  </React.StrictMode>,
)
