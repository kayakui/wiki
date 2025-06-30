import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import '/home/kayaki/web/node_modules/bootstrap/dist/css/bootstrap.css'
import "/src/App.css";
import App from './App.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
