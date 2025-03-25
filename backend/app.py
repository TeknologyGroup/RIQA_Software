from flask import Flask, request, jsonify
from ai.core import RIQAAI

app = Flask(__name__)
ai_system = RIQAAI()

@app.route('/ai/generate', methods=['POST'])
def generate_code():
    data = request.json
    code = ai_system.generate_code(data['prompt'])
    return jsonify({"code": code})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

@app.route('/ai/optimize', methods=['POST'])
def optimize_code():
    data = request.json
    optimized = ai_system.regenerator.optimize(data['code'])
    return jsonify({"optimized": optimized})

@app.route('/ai/save', methods=['POST'])
def save_file():
    data = request.json
    ai_system.file_manager.save(data['path'], data['content'])
    return jsonify({"status": "saved"})
