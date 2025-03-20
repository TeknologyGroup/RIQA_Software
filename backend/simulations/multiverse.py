import numpy as np
H_p = [np.diag([1/np.log(p) for _ in range(10)]) for p in range(2, 11)]
H_A = np.kron(H_p[0], H_p[1])  # Semplificato per due universi
print("Hamiltoniano adelico:", H_A)