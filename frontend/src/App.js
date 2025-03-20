import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import Simulations from './pages/Simulations';
import Visualizations from './pages/Visualizations';

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/simulations" element={<Simulations />} />
                <Route path="/visualizations" element={<Visualizations />} />
            </Routes>
        </Router>
    );
}

export default App;
