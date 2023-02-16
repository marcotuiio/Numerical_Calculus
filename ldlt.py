import numpy as np

def ldl(U, L, b):
    n = U.shape[0]
    d = np.zeros((n, n))

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

    # Montando matriz D
    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                d[i, j] = U[i, j]

    # Resolver os sistemas
    # {L * y = b
    # {D * z = y
    # {L^t * x = z
    lt = np.transpose(L)
    x = np.ones(n)
    y = np.ones(n)
    z = np.ones(n)

    # Substituição progressiva
    for i in range(0, n):
        y[i] = b[i]
        for j in range(0, i):
            y[i] = y[i] - L[i, j] * y[j]
        y[i] = y[i] / L[i, i]

    # Fórmula para z[n]
    for i in range(0, n):
        z[i] = y[i] / d[i, i];
    
    # Retrosubstituição
    for i in range(n - 1, -1, -1):
        x[i] = z[i]
        for j in range(i + 1, n):
            x[i] = x[i] - lt[i, j] * x[j]
        x[i] = x[i] / lt[i, i]

    return U, L, d, x

A = np.asmatrix([[4., -1., 1.],
                 [-1., 4.25, 2.75],
                 [1., 2.75, 3.5]])
                
b = np.asmatrix([[1.],
                [0.],
                [0.]])

I = np.asmatrix([[1., 0., 0.],
                 [0., 1., 0.],
                 [0., 0., 1.]])

u, l, d, x = ldl(A, I, b)

print('\nMatriz A:\n', A.round(2))
print('\nMatriz L:\n', l.round(2))
print('\nMatriz D:\n', d.round(2))
print('\nMatriz L^T:\n', np.transpose(l).round(2))
print('\nVetor x:\n', x.round(2))