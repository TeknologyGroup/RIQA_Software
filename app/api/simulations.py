app/api/simulations.py
from marshmallow import Schema, fields, ValidationError

class SimulationParametersSchema(Schema):
    mu = fields.Float(required=True)
    s = fields.Float(required=True)
    N = fields.Int(required=True)
    m = fields.Float(required=True)
    p_migrante = fields.Float(required=True)
    p0 = fields.Float(required=True)
    t_max = fields.Int(required=True)

@simulations_bp.route('/simulate', methods=['POST'])
def simulate():
    try:
        parameters = SimulationParametersSchema().load(request.json['parameters'])
    except ValidationError as err:
        return jsonify({'error': 'Invalid parameters', 'messages': err.messages}), 400

    result = run_evolution_simulation(parameters)
    return jsonify(result)
