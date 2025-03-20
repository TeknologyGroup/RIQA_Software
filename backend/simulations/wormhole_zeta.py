import numpy as np
from mpmath import zetazero
from flask import jsonify

class WormholeZetaSimulation:
    def __init__(self, zero_index=1, r_range=10, points=100):
        self.zero_index = zero_index  # Indice dello zero non banale (1 = primo zero)
        self.r_range = r_range        # Intervallo radiale oltre b0
        self.points = points          # Numero di punti per il calcolo
        
        # Calcola lo zero non banale
        self.t_n = float(zetazero(zero_index).imag)
        self.b0 = self.t_n  # Raggio della gola basato su t_n
    
    def calculate_metric(self):
        """Calcola la metrica del wormhole."""
        r = np.linspace(self.b0, self.b0 + self.r_range, self.points)
        b_r = self.b0 * np.ones_like(r)  # Funzione di forma costante
        Phi_r = -self.b0 / r             # Potenziale di redshift semplificato
        g_rr = 1 / (1 - b_r / r)        # Componente radiale della metrica
        
        return {
            'r': r.tolist(),
            'b_r': b_r.tolist(),
            'Phi_r': Phi_r.tolist(),
            'g_rr': g_rr.tolist(),
            'b0': self.b0,
            't_n': self.t_n
        }

def run_wormhole_simulation(params):
    """Esegue la simulazione per l'API Flask."""
    try:
        zero_index = int(params.get('zero_index', 1))
        r_range = float(params.get('r_range', 10))
        points = int(params.get('points', 100))
        
        sim = WormholeZetaSimulation(zero_index, r_range, points)
        result = sim.calculate_metric()
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Aggiungi al main.py
from flask import Flask, request
app = Flask(__name__)

@app.route('/simulate/wormhole', methods=['POST'])
def simulate_wormhole():
    data = request.get_json()
    return run_wormhole_simulation(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)