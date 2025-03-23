import pytest
from app.models.simulation import SimulationResult
from database.base import Session

def test_save_simulation_result():
    session = Session()
    result = SimulationResult(
        simulation_type='test',
        parameters='{"mu": 0.1}',
        results='{"time": [1, 2, 3], "frequency": [0.1, 0.2, 0.3]}'
    )
    session.add(result)
    session.commit()
    assert result.id is not None
    session.close()
