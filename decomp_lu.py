import numpy as np

def decomp_lu(U, L):
    n = U.shape[0]
    # Decomposição LU
    for j in range(0, n-1):
        for i in range(j+1, n):
            L[i, j] = U[i, j] / U[j, j]  # multiplicador de linha
            for k in range(j+1, n):
                U[i, k] = U[i, k] - L[i, j] * U[j, k]  # combinação linear
            U[i, j] = 0

    return U, L


A = np.asmatrix([[25., 5., 1.],
                 [64., 8., 1.],
                 [144., 12., 1.]])

I = np.asmatrix([[1., 0., 0.],
                 [0., 1., 0.],
                 [0., 0., 1.]])

u, l = decomp_lu(A, I)

print('Matriz U:\n', u)
print('Matriz L:\n', l)
