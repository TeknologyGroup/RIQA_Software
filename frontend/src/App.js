import React, { Suspense, lazy } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

// Lazy loading delle pagine
const Home = lazy(() => import('./pages/Home'));
const Simulations = lazy(() => import('./pages/Simulations'));
const Visualizations = lazy(() => import('./pages/Visualizations'));

// Componente di fallback per il caricamento
const LoadingFallback = () => <div>Caricamento...</div>;

// Componente base per il layout
const Layout = ({ children }) => (
  <div className="app-container">
    <header>RIQA Software</header>
    <main>{children}</main>
    <footer>&copy; 2025 xAI</footer>
  </div>
);

function App() {
  return (
    <Router>
      <Suspense fallback={<LoadingFallback />}>
        <Layout>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/simulations" element={<Simulations />} />
            <Route path="/visualizations" element={<Visualizations />} />
            <Route path="*" element={<div>404 - Pagina non trovata</div>} />
          </Routes>
        </Layout>
      </Suspense>
    </Router>
  );
}

export default App;