import pytest
from app.services.wormhole import calculate_wormhole_metric

def test_calculate_wormhole_metric():
    zero_index = 1
    result = calculate_wormhole_metric(zero_index)
    assert 'r' in result
    assert 'b_r' in result
    assert 'Phi_r' in result
    assert 'g_rr' in result
