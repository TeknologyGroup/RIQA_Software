import React from 'react';
import Wormhole3D from '../components/Wormhole3D';

function Visualizations({ simulationData }) {
  return (
    <div style={{ padding: '20px' }}>
      <h1>Visualizzazioni</h1>
      {simulationData ? (
        <Wormhole3D simulationData={simulationData} />
      ) : (
        <p>Nessun dato di simulazione disponibile. Esegui una simulazione dalla pagina "Simulazioni".</p>
      )}
    </div>
  );
}

export default Visualizations;
