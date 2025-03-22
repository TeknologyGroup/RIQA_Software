# Utilizza il frontend per inviare i dati dei sensori al backend#

import React, { useEffect, useState } from 'react';
import axios from 'axios';

function SensorData() {
    const [sensorData, setSensorData] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            const response = await axios.get('/api/sensor-data');
            setSensorData(response.data);
        };
        fetchData();
    }, []);

    return (
        <div>
            <h2>Dati Sensori</h2>
            <ul>
                {sensorData.map((data, index) => (
                    <li key={index}>{data.sensor_type}: {data.value}</li>
                ))}
            </ul>

                ### **4.2. Invio dei Dati dal Frontend**

#Utilizza il frontend per inviare i dati dei sensori al backend#

// frontend/src/components/SensorData.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

function SensorData() {
    const [sensorData, setSensorData] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            const response = await axios.get('/api/sensor-data');
            setSensorData(response.data);
        };
        fetchData();
    }, []);

    return (
        <div>
            <h2>Dati Sensori</h2>
            <ul>
                {sensorData.map((data, index) => (
                    <li key={index}>{data.sensor_type}: {data.value}</li>
                ))}
            </ul>
        </div>
    );
}

export default SensorData;

        </div>
    );
}

export default SensorData;
