from qiskit import QuantumCircuit, execute, Aer

def run_quantum_simulation(data):

qc = QuantumCircuit(2)

qc.h(0)  # Porta Hadamard

qc.cx(0, 1)  # Porta CNOT

qc.measure_all()

result = execute(qc, Aer.get_backend('qasm_simulator')).result()

return result.get_counts()