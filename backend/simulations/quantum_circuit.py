from qiskit import QuantumCircuit, Aer, execute
qc = QuantumCircuit(3)
qc.h(range(3))
qc.rx(np.pi/4, range(3))
qc.measure_all()
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, simulator, shots=1024).result()
print("Risultati circuito quantistico:", result.get_counts())