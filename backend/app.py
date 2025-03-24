from flask import Flask, jsonify, request
from flask_socketio import SocketIO
from database import init_db  # Cambiato da .database a database
from data_fetcher import search_arxiv  # Cambiato da .data_fetcher
from simulation import compute_simulation  # Cambiato da .simulation
from validation import validate_experiment  # Cambiato da .validation

app = Flask(__name__)
socketio = SocketIO(app)

# Configurazione iniziale
init_db()

@app.route('/')
def home():
    return "Backend RIQA attivo!"

@app.route('/search')
def search():
    return search_arxiv("quantum physics")

@app.route('/simulate', methods=['POST'])
def simulate():
    data = request.json
    result = compute_simulation(data.get('input', []))
    return jsonify(result)

@socketio.on('connect')
def handle_connect():
    print("Client connesso via WebSocket")

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
