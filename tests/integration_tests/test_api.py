import pytest
import requests

BASE_URL = '<http://localhost:5000>'

def test_simulate_endpoint():
    response = requests.post(f'{BASE_URL}/simulate', json={
        'parameters': {
            'mu': 0.1,
            's': 0.2,
            'N': 100,
            'm': 0.05,
            'p_migrante': 0.5,
            'p0': 0.1,
            't_max': 100
        }
    })
    assert response.status_code == 200
    data = response.json()
    assert 'time' in data
    assert 'frequency' in data