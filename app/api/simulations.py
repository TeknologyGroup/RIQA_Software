# app/api/simulations.py
from flask import Blueprint, request, jsonify
from flask_caching import Cache
from app.services.evolution import run_evolution_simulation
from app.utils.cache import cache

simulations_bp = Blueprint('simulations', __name__)

@simulations_bp.route('/simulate', methods=['POST'])
@cache.cached(timeout=300, key_prefix=lambda: request.json['parameters'])
def simulate():
    parameters = request.json['parameters']
    result = run_evolution_simulation(parameters)
    return jsonify(result)
