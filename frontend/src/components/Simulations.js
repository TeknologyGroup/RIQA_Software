import React, { useState } from 'react';
import SimulationForm from '../components/SimulationForm';
import Wormhole3D from '../components/Wormhole3D';

function Simulations() {
  const [simulationData, setSimulationData] = useState(null);

  const handleSimulationResult = (data) => {
    setSimulationData(data);
  };

  return (
    <div>
      <h1>Simulazioni Wormhole</h1>
      <SimulationForm onResult={handleSimulationResult} />
      {simulationData && (
        <div>
          <h2>Visualizzazione 3D</h2>
          <Wormhole3D simulationData={simulationData} />
        </div>
      )}
    </div>
  );
}

export default Simulations;