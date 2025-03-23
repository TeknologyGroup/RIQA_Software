import pytest
from app.services.evolution import run_evolution_simulation

def test_run_evolution_simulation():
    parameters = {
        'mu': 0.1,
        's': 0.2,
        'N': 100,
        'm': 0.05,
        'p_migrante': 0.5,
        'p0': 0.1,
        't_max': 100
    }
    result = run_evolution_simulation(parameters)
    assert 'time' in result
    assert 'frequency' in result
    assert len(result['time']) == len(result['frequency'])
