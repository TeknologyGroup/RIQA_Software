from flask import Flask, render_template
from flask_socketio import SocketIO
from ai_engine import AIEngine

app = Flask(__name__)
socketio = SocketIO(app)
ai = AIEngine()

@app.route('/')
def home():
    return render_template('index.html')

@socketio.on('process_input')
def handle_input(data):
    result = ai.process(data['text'])
    socketio.emit('ai_response', {'result': result})

if __name__ == '__main__':
    socketio.run(app, debug=True)
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

@app.route('/validate')
def validate():
    return validate_experiment({})

@socketio.on('connect')
def handle_connect():
    print("Client connesso via WebSocket")

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
