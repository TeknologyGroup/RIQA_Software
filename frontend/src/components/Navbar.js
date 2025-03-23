import React from 'react';
import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <nav style={{ padding: '10px', backgroundColor: '#333', color: '#fff' }}>
      <ul style={{ listStyle: 'none', display: 'flex', gap: '20px' }}>
        <li><Link to="/" style={{ color: '#fff', textDecoration: 'none' }}>Home</Link></li>
        <li><Link to="/simulations" style={{ color: '#fff', textDecoration: 'none' }}>Simulazioni</Link></li>
        <li><Link to="/visualizations" style={{ color: '#fff', textDecoration: 'none' }}>Visualizzazioni</Link></li>
        <li><Link to="/hardware" style={{ color: '#fff', textDecoration: 'none' }}>Hardware</Link></li>
        <li><Link to="/mobile-app" style={{ color: '#fff', textDecoration: 'none' }}>App Mobile</Link></li>
        <li><Link to="/docs" style={{ color: '#fff', textDecoration: 'none' }}>Documentazione</Link></li>
      </ul>
    </nav>
  );
}

export default Navbar;
