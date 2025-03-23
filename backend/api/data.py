from flask import Blueprint, jsonify
import requests

data_bp = Blueprint('data', __name__)

@data_bp.route('/datasets', methods=['GET'])
def get_datasets():
    response = requests.get('<https://dataverse.org/api/datasets>')
    return jsonify(response.json())
