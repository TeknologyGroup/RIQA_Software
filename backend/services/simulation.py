import numpy as np
from scipy.integrate import solve_ivp

def run_advanced_simulation(parameters):
    def model(t, y):
        return np.array([parameters['mu'] * y[0] * (1 - y[0])])

    result = solve_ivp(model, [0, parameters['t_max']], [parameters['p0']], t_eval=np.linspace(0, parameters['t_max'], 1000))
    return {'time': result.t.tolist(), 'frequency': result.y[0].tolist()}
