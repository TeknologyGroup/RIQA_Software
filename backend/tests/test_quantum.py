# backend/tests/test_quantum.py
def test_quantum_simulation():
    result = run_quantum_simulation(["h 0"])
    assert "00" in result or "11" in result