import numpy as np

def decomp_lu(U, L, b):
    n = U.shape[0]
    # Decomposição LU
    for j in range(0, n-1):
        for i in range(j+1, n):
            # Pivotamento
            if U[j, j] == 0:
                for k in range(j + 1, n):
                    if U[k, j] != 0:
                        U[[j, k]] = U[[k, j]]
                        break
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

# Exemplo que precisa de pivotamento
A = np.asmatrix([[3., -4., 1.],
                 [1., 2., 2.],
                 [4., 0., -3.]])
                
b = np.asmatrix([[9.],
                [3.],
                [-2.]])

I = np.asmatrix([[1., 0., 0.],
                 [0., 1., 0.],
                 [0., 0., 1.]])

# A = np.asmatrix([[12., -6., 3., 1.],
#                  [4., 13., -5., 4.],
#                  [6., 1., 10., -2.],
#                  [4., 1., -1., 9.]])
                
# b = np.asmatrix([[-61.],
#                 [53.],
#                 [-28.],
#                 [11.]])

# I = np.asmatrix([[1., 0., 0., 0.],
#                  [0., 1., 0., 0.],
#                  [0., 0., 1., 0.],
#                  [0., 0., 0., 1.]])

u, l, x = decomp_lu(A, I, b)

print('Matriz U:\n', u.round(2))
print('\nMatriz L:\n', l.round(2))
print('\nVetor solução:\n', x.round(2))