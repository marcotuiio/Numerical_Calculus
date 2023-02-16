import numpy as np
import math

def simetrica(A):
    n = A.shape[0]
    for i in range(0, n):
        for j in range(0, i):
            if A[i, j] != A[j, i]:
                return False
    return True

def decomp_cholesky(A, b):
    n = A.shape[0]
    G = np.asmatrix(np.zeros((n, n)))

    # Decomposição de Cholesky
    for i in range(0, n):
        for j in range(0, i+1):
            sum = 0.0
            if (i == j):
                for k in range(j):
                    sum += pow(G[j, k], 2)
                G[j, j] = np.sqrt(A[j, j] - sum)
            else:
                for k in range(j):
                    sum += G[i, k] * G[j, k]
                if (G[j, j] > 0):
                    G[i, j] = (A[i, j] - sum) / G[j, j]
    
    ## {G * y = b
    ## {G_t * x = y
    G_t = np.transpose(G)

    # Substituição progressiva
    y = np.ones(n, dtype=float)
    for i in range(0, n):
        y[i] = b[i]
        for j in range(0, i):
            y[i] = y[i] - G[i, j] * y[j]
        y[i] = y[i] / G[i, i]

    # Retrosubstituição
    X = np.ones(n, dtype=float)
    for i in range(n - 1, -1, -1):
        X[i] = y[i]
        for j in range(i + 1, n):
            X[i] = X[i] - G_t[i, j] * X[j]
        X[i] = X[i] / G_t[i, i]

    return G, X

A = np.asmatrix([[1., 1., 0.],
                [1., 2., -1.],
                [0., -1., 3.]])

b = np.asmatrix([[2.],
                 [1.],
                [5.]])

# A = np.asmatrix([[4., -1., 1.],
#                  [-1., 4.25, 2.75],
#                  [1., 2.75, 3.5]])

if simetrica(A):
    g, x = decomp_cholesky(A, b)
    print('Matriz G:\n', g.round(2))
    print('\nVetor solução:\n', x.round(2))
else:
    print('A matriz não é simétrica!')