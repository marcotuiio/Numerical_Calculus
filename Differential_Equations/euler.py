import numpy as np
import sympy as sp

def euler(f, x_values, y_values, final_x, h=0.01):
    n = 0
    while x_values[-1] < final_x:
        y_values.append((y_values[n] + h*f.subs({x:x_values[n], y:y_values[n]})))
        x_values.append(x_values[n] + h)
        n += 1

    print('Xn: ', x_values)
    print('Yn: ', y_values)

## Insira a equação diferencial na função f(x,y), além dos valores iniciais de x e y
y = sp.Symbol('y')
x = sp.Symbol('x')
x_values = []
y_values = []

f_xy = (2*y - 2) / x
x_values.append(1)
y_values.append(3)
h = 0.5
final_x = 2

euler(f_xy, x_values, y_values, final_x, h)
