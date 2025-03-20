import numpy as np
rho = np.diag([1/np.log(p) if p > 1 else 0 for p in range(1, 11)])
rho = rho / np.trace(rho)
entropy = -np.trace(rho @ np.log(rho + np.eye(10) * 1e-10))  # Evita log(0)
print("Entropia buchi neri:", entropy)