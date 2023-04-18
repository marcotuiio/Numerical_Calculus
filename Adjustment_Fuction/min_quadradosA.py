import sympy as sp
import numpy as np

def for_poly(x, y, n):
    m = len(x)

    # Criação das matrizes
    matX = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            for k in range(m):
                matX[i, j] = x[k]**(i+j) + matX[i, j]

    vetY = np.zeros(n)
    for i in range(n):
        for k in range(m):
            vetY[i] = y[k]*x[k]**i + vetY[i]

    print("matX: \n", matX.round(4))
    print("vetY: \n", vetY.round(4))

    vetA = seidel(matX, vetY)
    print("A.i: \n", vetA.round(1))

    # Criação do polinômio
    X = sp.Symbol('x')
    pol = 0
    for i in range(n):
        pol = ((vetA[i]).round(4))*X**i + pol

    print("\nPolinômio: \n", pol)

def seidel(mat, b):
    n = mat.shape[0]
    x = np.zeros(n) 
    erro = np.zeros(n)
    tol = 0.000001
    for k in range(0, 100):
        for i in range(0, n):
            soma = 0
            for j in range(0, n):
                if i != j:
                    soma = -mat[i, j] * x[j] + soma
            prov = x[i]
            x[i] = (b[i] + soma) / mat[i, i]
            erro[i] = abs(x[i] - prov)
        if max(erro) / max(x) < tol:
            return x
    return x

# x = np.array([0, .25, .5, .75, 1])
# y = np.array([1, 1.2840, 1.6487, 2.1170, 2.7183])
# n = 3

x = np.array([-3, -2, -1, 1, 2, -3])
y = np.array([26, 17, 10, 2, 1, 26])
n = 3

for_poly(x, y, n)