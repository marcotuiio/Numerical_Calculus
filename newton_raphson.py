from tabulate import tabulate
import numpy as np

def newton_raphson(expression, initial):
    vetX = []
    derivative = expression.deriv()
    i = 0
    x1 = initial
    while i < 10:
        x2 = x1 - (expression(x1) / derivative(x1))
        vetX.append([x1, expression(x1), derivative(x1), x2, abs(x2 - x1)])
        if abs(x2 - x1) < 0.00001:
            break
        x1 = x2
        i = i + 1
    return vetX

# no caso de utilizar esse programa, alterar a função func(x) e o valor inicial x0
exp = np.poly1d([1, 6, 12, -11]) # x^3 + 6*x^2 + 12^x - 11
x = newton_raphson(exp, 1)
print(tabulate(x, headers=["x", "f(x)", "f'(x)", "x'", "erro"], tablefmt="grid"))