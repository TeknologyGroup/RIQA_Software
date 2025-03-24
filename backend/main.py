from flask import Flask, request, jsonify
from simulations.evolution import run_evolution_simulation
from dotenv import load_dotenv
import os
from ai.file_manager import observer

if __name__ == "__main__":
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# Carica variabili d'ambiente
load_dotenv()
app = Flask(__name__)

# Configurazione
DEBUG = os.getenv('FLASK_DEBUG', 'True') == 'True'
PORT = int(os.getenv('FLASK_PORT', 5000))

@app.route('/simulate', methods=['POST'])
def simulate():
    try:
        data = request.get_json()
        if not data or 'parameters' not in data:
            return jsonify({'error': 'Parametri mancanti'}), 400
        
        parameters = data['parameters']
        result = run_evolution_simulation(parameters)
        return jsonify(result), 200
    
    except KeyError as e:
        return jsonify({'error': f'Chiave mancante: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': f'Errore interno: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT, host='0.0.0.0')