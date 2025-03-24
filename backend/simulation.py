import numpy as np
from scipy.integrate import odeint

def compute_simulation(input_data):
    return np.array(input_data) ** 2  # Esempio di simulazione

def simulate_trajectory(params):
    initial_position = params.get('initial_position', [0.0, 0.0])
    initial_velocity = params.get('initial_velocity', [10.0, 10.0])
    t = np.linspace(0, 10, 100)
    
    def motion_equations(state, t):
        x, y, vx, vy = state
        return [vx, vy, 0, -9.81]  # Gravità terrestre
    
    solution = odeint(motion_equations, initial_position + initial_velocity, t)
    return {'x': solution[:, 0].tolist(), 'y': solution[:, 1].tolist()}
