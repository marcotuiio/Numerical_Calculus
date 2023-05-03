import numpy as np
import sympy as sp

def simpson(f, a, b, n, X):
    h = (b - a) / n
    xi = np.zeros(n+1)
    for i in range(n+1):
        xi[i] = a + i*h

    integral_aprox = f.subs(X, xi[0]) + f.subs(X, xi[n])
    mult = 4
    for i in range(1, n):
        integral_aprox = mult * f.subs(X, xi[i]) + integral_aprox
        if mult == 4:
            mult = 2
        else:
            mult = 4

    integral_aprox = h/3 * integral_aprox
    print('Simpson: ', integral_aprox.round(9))

X = sp.Symbol('x')
f = sp.sqrt(X);
n = 4
a = 0
b= 8
simpson(f, a, b, n, X)