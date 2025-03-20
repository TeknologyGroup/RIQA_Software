from flask import Flask, request, jsonify
from simulations.evolution import run_evolution_simulation

app = Flask(__name__)

@app.route('/simulate', methods=['POST'])
def simulate():
    data = request.json
    result = run_evolution_simulation(data['parameters'])
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
