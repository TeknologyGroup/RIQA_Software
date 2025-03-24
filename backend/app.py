from flask import Flask, jsonify, request
from flask_socketio import SocketIO
from .database import init_db
from .data_fetcher import search_arxiv
from .simulation import compute_simulation
from .validation import validate_experiment

# Inizializza Flask e SocketIO
app = Flask(__name__)
socketio = SocketIO(app)

# Configurazione iniziale
init_db()  # Inizializza il database

# Route di esempio
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

# WebSocket
@socketio.on('connect')
def handle_connect():
    print("Client connesso via WebSocket")

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
