import React, { useState } from 'react';

import SimulationForm from '../components/SimulationForm';

import Wormhole3D from '../components/Wormhole3D';

function Simulations() {

const [simulationData, setSimulationData] = useState(null);

const handleSimulationResult = (data) => {

setSimulationData(data);

};

return (