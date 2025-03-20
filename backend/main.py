from flask import Flask, request, jsonify
from flask_cors import CORS
from simulations.evolution import run_evolution_simulation

app = Flask(__name__)
CORS(app)  # Per consentire richieste dal frontend

@app.route('/simulate', methods=['POST'])
def simulate():
    data = request.json
    result = run_evolution_simulation(data['parameters'])
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
