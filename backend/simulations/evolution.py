import numpy as np
from typing import Dict, List

def run_evolution_simulation(parameters: Dict[str, float]) -> Dict[str, List[float]]:
    """
    Esegue una simulazione evolutiva basata su parametri genetici.
    
    Args:
        parameters: Dizionario con chiavi 'mu', 's', 'N', 'm', 'p_migrante', 'p0', 't_max'.
    
    Returns:
        Dizionario con 'time' e 'frequency' come liste.
    
    Raises:
        ValueError: Se i parametri sono invalidi o mancanti.
    """
    required_params = ['mu', 's', 'N', 'm', 'p_migrante', 'p0', 't_max']
    for param in required_params:
        if param not in parameters:
            raise ValueError(f"Parametro richiesto mancante: {param}")

    # Estrazione parametri con validazione
    mu = float(parameters['mu'])  # Tasso di mutazione
    s = float(parameters['s'])    # Coefficiente di selezione
    N = int(parameters['N'])      # Dimensione popolazione
    m = float(parameters['m'])    # Tasso di migrazione
    p_migrante = float(parameters['p_migrante'])  # Frequenza allelica dei migranti
    p0 = float(parameters['p0'])  # Frequenza iniziale
    t_max = int(parameters['t_max'])  # Tempo massimo

    if not (0 <= p0 <= 1 and 0 <= p_migrante <= 1):
        raise ValueError("p0 e p_migrante devono essere tra 0 e 1")
    if N <= 0 or t_max <= 0:
        raise ValueError("N e t_max devono essere positivi")

    # Ottimizzazione: usa array NumPy pre-allocati
    t = np.linspace(0, t_max, 1000, dtype=np.float32)
    p = np.zeros_like(t, dtype=np.float32)
    p[0] = p0
    dt = t[1] - t[0]  # Passo temporale costante

    # Calcolo vettoriale per migliorare le prestazioni
    for i in range(1, len(t)):
        dp_dt = (mu * p[i-1] * (1 - p[i-1]) + 
                 s * p[i-1] * (1 - p[i-1]) - 
                 (p[i-1] * (1 - p[i-1])) / (2 * N) + 
                 m * (p_migrante - p[i-1]))
        p[i] = p[i-1] + dp_dt * dt

    return {'time': t.tolist(), 'frequency': p.tolist()}