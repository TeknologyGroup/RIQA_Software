import React, { useState } from 'react';
import SimulationForm from '../components/SimulationForm';

function Simulations({ setSimulationData }) {
  const [result, setResult] = useState(null);

  const handleSimulationResult = (data) => {
    setResult(data);
    setSimulationData(data); // Passa i dati alla visualizzazione
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>Simulazioni</h1>
      <SimulationForm onResult={handleSimulationResult} />
      {result && (
        <div>
          <h2>Risultati della Simulazione</h2>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default Simulations;
