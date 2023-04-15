import numpy as np
import sympy as sp

def lagrange(x, y):
    n = len(x)
    var = sp.Symbol('x')
    L_x = []


    for i in range(0, n):
        numerador = 1
        denominador = 1
        for j in range(0, n):
            if i != j:
                numerador = numerador * (var - x[j])
                denominador = denominador * (x[i] - x[j])

        poly = (numerador / denominador) * y[i]
        L_x.append(poly) 
    # print("L(x) = ", L_x)

    p_x = sp.simplify(sum(L_x))

    return p_x

print("\nInterpolação por Lagrange\n")
x = np.array([3, 7, 10])
y = np.array([5, 9, 11])
Poly = lagrange(x, y)
print("P(x) = ", Poly)

# x = np.array([0, 1, 2])
# y = np.array([sp.sin(0), sp.sin(1), sp.sin(2)])
# Poly = lagrange(x, y)
# print("P(x) = ", Poly)