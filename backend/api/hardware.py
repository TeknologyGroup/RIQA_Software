from flask import Blueprint, request, jsonify
from database.models.simulation_results import SimulationResult
from database.base import Session

hardware_bp = Blueprint('hardware', __name__)

@hardware_bp.route('/sensor-data', methods=['POST'])
def receive_sensor_data():
    data = request.json
    sensor_type = data.get('sensor_type')
    value = data.get('value')

    if not sensor_type or not value:
        return jsonify({'error': 'Dati mancanti'}), 400

    session = Session()
    result = SimulationResult(
        simulation_type='sensor_data',
        parameters=sensor_type,
        results=str(value)
    )
    session.add(result)
    session.commit()
    session.close()

    return jsonify({'message': 'Dati ricevuti e salvati'}), 200
