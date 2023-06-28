import sympy as sp

def euler(f, x_values, y_values, final_x, h=0.1):
    n = 0
    while x_values[-1] < final_x:
        y_values.append((y_values[n] + h*f.subs({x:x_values[n], y:y_values[n]})))
        x_values.append(x_values[n] + h)
        n += 1

    # print('Xn: ', x_values)
    # print('Yn: ', y_values)
    return y_values[-1]

## Insira a equação diferencial na função f(x,y), além dos valores iniciais de x e y
y = sp.Symbol('y')
x = sp.Symbol('x')
x_values = []
y_values = []

f_xy = (2*y - 2) / x
x_values.append(1)
y_values.append(3)
h = 0.1
final_x = 2

final_y = euler(f_xy, x_values, y_values, final_x, h)
print('APROXIMADO: y({}) = {}'.format(final_x, final_y))
