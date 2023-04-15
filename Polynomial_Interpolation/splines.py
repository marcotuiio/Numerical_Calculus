import numpy as np  
import sympy as sp

def splines(x, y, var):
    n = len(x)
    # ini = deriv(x[0])
    # fim = deriv(x[n-1])

    ini = -2.29
    fim = 2.78

    a = np.zeros(n)
    for i in range(0, n):
        a[i] = y[i]

    h = np.zeros(n - 1)
    for i in range(0, n - 1):
        h[i] = x[i + 1] - x[i]

    matA = np.asmatrix(np.zeros((n, n)))
    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                if i == 0:
                    matA[i, j] = 2 * h[i]
                elif i == n - 1:
                    matA[i, j] = 2 * h[i-1]
                else:
                    matA[i, j] = 2 * (h[i-1] + h[i])
            elif abs(i - j) == 1:
                matA[i, j] = h[max(i, j) - 1]

    matB = np.zeros(n)
    for i in range(0, n):
        if i == 0:
            matB[i] = 3 * (a[i + 1] - a[i]) / h[i] - 3 * ini
        elif i == n - 1:
            matB[i] = 3 * fim - 3 * (a[i] - a[i - 1]) / h[i - 1]
        else:
            matB[i] = (3 * (a[i + 1] - a[i]) / h[i]) - (3 * (a[i] - a[i - 1]) / h[i - 1])

    c = seidel(matA, matB)

    b = np.zeros(n-1)

    for i in range(0, n-1): 
        b[i] = ((a[i+1] - a[i]) / h[i] - h[i] * (c[i+1] + 2 * c[i]) / 3).round(4)

    d = np.zeros(n-1)

    for i in range(0, n-1):
        d[i] = (c[i+1] - c[i]) / (3 * h[i])

    for i in range(0, n-1):
        d[i] = d[i].round(4)

    print("\na: ", a)
    print("b: ", b)
    print("c: ", c)
    print("d: ", d)


    # montar as equações dos splines
    splines = []
    for i in range(0, n-1):
        spline = (a[i] + b[i] * (var - x[i]) + c[i] * (var - x[i])**2 + d[i] * (var - x[i])**3).evalf(n=4)
        splines.append(spline)

    return splines

def seidel(mat, b):
    n = mat.shape[0]
    x = np.zeros(n) 
    erro = np.zeros(n)
    tol = 0.000001
    for k in range(0, 100):
        # print("Iteração:", k, "- X:", x)
        for i in range(0, n):
            soma = 0
            for j in range(0, n):
                if i != j:
                    soma = -mat[i, j] * x[j] + soma
            prov = x[i]
            x[i] = ((b[i] + soma) / mat[i, i]).round(4)
            erro[i] = abs(x[i] - prov)
        if max(erro) / max(x) < tol:
            return x

    return x

x = np.array([0.6, 1.3, 2.5, 3.3])
y = np.array([1.49, 0.897, 1.33, 2.68])

var_x = sp.Symbol('x')
# funtion = 2**(2 - var_x) * sp.cos(sp.pi * var_x)
# deriv = funtion.diff(var_x)
splines = splines(x, y, var_x)

for i in range(0, len(splines)):
    print("\n Spline", i, ":", splines[i])
    