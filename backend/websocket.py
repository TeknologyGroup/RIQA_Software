from flask_socketio import SocketIO
from .simulation import compute_simulation

socketio = SocketIO()

def handle_simulation(data):
    result = compute_simulation(data['input'])  # Chiamata a simulation.py
    socketio.emit('update', result)
