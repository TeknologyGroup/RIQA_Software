from flask import Blueprint, jsonify
import requests

research_bp = Blueprint('research', __name__)

@research_bp.route('/publish', methods=['POST'])
def publish_results():
    data = request.json
    response = requests.post('<https://api.researchgate.net/publish>', json=data)
    return jsonify(response.json())
