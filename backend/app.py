from flask import Flask, request, jsonify
from ai.core import RIQAAI

app = Flask(__name__)
ai_engine = RIQAAI()  # Istanza della tua AI

@app.route('/ai/process', methods=['POST'])
def process_ai():
    data = request.json
    result = ai_engine.process(data['input'])
    return jsonify({"result": result})
    
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/process', methods=['POST'])
def api_process():
    return jsonify(ai.process(request.json['text']))

@socketio.on('process_input')
def handle_input(data):
    result = ai.process(data['text'])
    socketio.emit('ai_response', {'result': result})

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)

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
