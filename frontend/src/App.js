import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import Simulations from './pages/Simulations';
import Visualizations from './pages/Visualizations';
import HardwareIntegration from './pages/HardwareIntegration';
import MobileApp from './pages/MobileApp';
import Documentation from './pages/Documentation';
import Navbar from './components/Navbar';
import Footer from './components/Footer';

function App() {
  const [simulationData, setSimulationData] = useState(null); // Stato per i dati della simulazione

  return (
    <Router>
      <div className="app-container">
        <Navbar /> {/* Barra di navigazione */}
        <Routes>
          {/* Pagina principale */}
          <Route path="/" element={<Home />} />

          {/* Pagina delle simulazioni */}
          <Route
            path="/simulations"
            element={<Simulations setSimulationData={setSimulationData} />}
          />

          {/* Pagina delle visualizzazioni */}
          <Route
            path="/visualizations"
            element={<Visualizations simulationData={simulationData} />}
          />

          {/* Pagina di integrazione hardware */}
          <Route path="/hardware" element={<HardwareIntegration />} />

          {/* Pagina dell'app mobile */}
          <Route path="/mobile-app" element={<MobileApp />} />

          {/* Pagina della documentazione */}
          <Route path="/docs" element={<Documentation />} />
        </Routes>
        <Footer /> {/* Footer */}
      </div>
    </Router>
  );
}

export default App;
