import numpy as np
from scipy.optimize import minimize
N = 10
primes_list = [2, 3, 5, 7, 11]
def potential(M, primes):
    V = np.trace(M @ M)
    for p in primes:
        V += (np.log(p) / p) * np.trace(np.linalg.matrix_power(M, p))
    return V
def objective(x):
    M = x.reshape((N, N))
    return potential(M, primes_list)
x0 = np.random.randn(N * N)
result = minimize(objective, x0, method='BFGS')
print("Matrice ottimale fusione:", result.x.reshape((N, N)))