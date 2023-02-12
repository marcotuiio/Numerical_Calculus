import numpy as np

def decomp_lu(U, L, b):
    n = U.shape[0]
    # Decomposição LU
    for j in range(0, n-1):
        for i in range(j+1, n):
            L[i, j] = U[i, j] / U[j, j]  # multiplicador de linha
            for k in range(j+1, n):
                U[i, k] = U[i, k] - L[i, j] * U[j, k]  # combinação linear
            U[i, j] = 0

    # Substituição progressiva
    Z = np.ones(n)
    for i in range(0, n):
        Z[i] = b[i]
        for j in range(0, i):
            Z[i] = Z[i] - L[i, j] * Z[j]
        Z[i] = Z[i] / L[i, i]

    # Retrosubstituição
    X = np.ones(n)
    for i in range(n - 1, -1, -1):
        X[i] = Z[i]
        for j in range(i + 1, n):
            X[i] = X[i] - U[i, j] * X[j]
        X[i] = X[i] / U[i, i]

    return U, L, X

A = np.asmatrix([[1., 1., 1.],
                 [2., 1., -1.],
                 [2., -1., 1.]])

I = np.asmatrix([[1., 0., 0.],
                 [0., 1., 0.],
                 [0., 0., 1.]])
                
b = np.asmatrix([[-2.],
                [1.],
                [3.]])

u, l, x = decomp_lu(A, I, b)

print('Matriz U:\n', u)
print('\nMatriz L:\n', l)
print('\nVetor solução:\n', x)