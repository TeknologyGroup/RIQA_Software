@app.route('/submit_equation', methods=['POST'])
def submit_equation():
    equation = request.json.get('equation')
    save_experiment({'type': 'user_equation', 'input': equation}, None)
    return jsonify({'message': 'Equazione salvata'})
