import numpy as np

def run_evolution_simulation(parameters):
    mu = parameters['mu']
    s = parameters['s']
    N = parameters['N']
    m = parameters['m']
    p_migrante = parameters['p_migrante']
    p0 = parameters['p0']
    t_max = parameters['t_max']

    t = np.linspace(0, t_max, 1000)
    p = np.zeros_like(t)
    p[0] = p0

    for i in range(1, len(t)):
        p[i] = p[i-1] + (mu * p[i-1] * (1 - p[i-1]) +
                        s * p[i-1] * (1 - p[i-1]) -
                        (p[i-1] * (1 - p[i-1])) / (2 * N) +
                        m * (p_migrante - p[i-1])) * (t[i] - t[i-1])

    return {'time': t.tolist(), 'frequency': p.tolist()}
