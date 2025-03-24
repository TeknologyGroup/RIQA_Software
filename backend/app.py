from flask import Flask, jsonify, request
from flask_socketio import SocketIO
from database import save_experiment
from simulation import simulate_trajectory, simulate_weather
from quantum_interface import run_quantum_simulation

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/submit_equation', methods=['POST'])
def submit_equation():
    equation = request.json.get('equation')
    save_experiment({'type': 'user_equation', 'input': equation}, None)
    return jsonify({'message': 'Equazione salvata'})

@app.route('/simulate', methods=['POST'])
def run_simulation():
    data = request.json
    sim_type = data.get('type')
    input_data = data.get('input')
    
    if sim_type == 'quantum':
        result = run_quantum_simulation(input_data)
    elif sim_type == 'trajectory':
        result = simulate_trajectory(input_data)
    else:
        result = {"error": "Tipo di simulazione non supportato"}
    
    return jsonify(result)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)