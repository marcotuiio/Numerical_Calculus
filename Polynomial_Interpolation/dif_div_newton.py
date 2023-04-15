import numpy as np
import sympy as sp

def dif_div_newton(x, y):
    n = len(x)
    d = np.zeros(n)
    list_f_x = []
    
    # ordem 1
    f_x = np.zeros(n)
    for i in range(n):
        f_x[i] = y[i]
    list_f_x.append(f_x)
    d[0] = f_x[0] 
    
    # ordem 2->n
    posic = 1
    for i in range(0, n - 1):
        f_x = np.zeros(n - i - 1)
        f_anterior = list_f_x[i]
        for j in range(0, n - i - 1):
            numerador = f_anterior[j + 1] - f_anterior[j]
            denominador = x[posic + j] - x[j]
            f_x[j] = numerador / denominador
        d[i + 1] = f_x[0].round(3)
        list_f_x.append(f_x)
        posic += 1

    print("d = ", d)

    # polinomio interpolador
    p_x = 0
    var = sp.Symbol('x')    
    for i in range(0, n):
        mult = 1
        for j in range(i):
            mult = mult * (var - x[j])
        p_x = p_x + d[i] * mult

    p_x = sp.simplify(p_x)
    return p_x

# x = np.array([-1, 0, 2])
# y = np.array([4, 1, -1])
# Poly = dif_div_newton(x, y)
# print("P(x) = ", Poly)

# x = np.array([-1, 0, 1, 3])
# y = np.array([3, 1, 3, 43])
# Poly = dif_div_newton(x, y)
# print("P(x) = ", Poly)

x = np.array([-3, -1, 2, 3])
y = np.array([-83, 1, 7, 1])
Poly = dif_div_newton(x, y)
print("P(x) = ", Poly)
