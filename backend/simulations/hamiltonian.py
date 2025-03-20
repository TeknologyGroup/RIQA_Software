import numpy as np
from scipy.linalg import eigvalsh
N = 100
a_n = [1/np.log(p) if p > 1 else 0 for p in range(1, N+1)]
X = np.diag(np.arange(N))
P = np.diag(np.sqrt(np.arange(1, N+1)), k=1) + np.diag(np.sqrt(np.arange(1, N)), k=-1)
H = X @ X + P @ P + sum(a_n[i] * (X ** (i+1)) for i in range(len(a_n)))
eigenvalues = eigvalsh(H)
print("Autovalori hamiltoniano gravitazionale:", eigenvalues)