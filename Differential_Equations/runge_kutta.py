import sympy as sp

def runge_kutta(ordem, f, x_values, y_values, final_x, h=0.1):
    
    match ordem:
        case 2:
            print('-> Método de Runge-Kutta de ordem 2 (Euler Corrigido)')
            n = 0
            while x_values[-1] < final_x:
                next_y = y_values[n] + h*f.subs({x:x_values[n], y:y_values[n]})
                x_values.append(x_values[n] + h)

                aux1 = f.subs({x:x_values[n], y:y_values[n]})
                aux2 = f.subs({x:x_values[n+1], y:next_y})
                y_values.append(y_values[n] + h/2*(aux1 + aux2))
                n += 1
            return y_values[-1]
        
        case 3:
            print('-> Método de Runge-Kutta de ordem 3')
            n = 0
            while x_values[-1] < final_x:
                k1 = h*f.subs({x:x_values[n], y:y_values[n]})
                k2 = h*f.subs({x:x_values[n] + h/2, y:y_values[n] + k1/2})
                k3 = h*f.subs({x:x_values[n] + 3*h/4, y:y_values[n] + 3*k2/4})

                next_y = y_values[n] + 1/9*(2*k1 + 3*k2 + 4*k3)
                x_values.append(x_values[n] + h)
                y_values.append(next_y)
                n += 1
            return y_values[-1]
        
        case 4:
            print('-> Método de Runge-Kutta de ordem 4')
            n = 0
            while x_values[-1] < final_x:
                k1 = h*f.subs({x:x_values[n], y:y_values[n]})
                k2 = h*f.subs({x:x_values[n] + h/2, y:y_values[n] + k1/2})
                k3 = h*f.subs({x:x_values[n] + h/2, y:y_values[n] + k2/2})
                k4 = h*f.subs({x:x_values[n] + h, y:y_values[n] + k3})

                next_y = y_values[n] + 1/6*(k1 + 2*k2 + 2*k3 + k4)
                y_values.append(next_y)
                x_values.append(x_values[n] + h)
                n += 1
            return y_values[-1]
        
        case _:
            print('Ordem não implementada!!')
            exit()


## Informe a ordem do método, a equação diferencial na função f(x,y), além dos valores iniciais de x e y   
y = sp.Symbol('y')
x = sp.Symbol('x')
x_values = []
y_values = []

ordem = 2

f_xy = (2*y - 2) / x
x_values.append(1)
y_values.append(3)
h = 0.5
final_x = 2

final_y = runge_kutta(ordem, f_xy, x_values, y_values, final_x, h)
print('APROXIMADO: y({}) = {}'.format(final_x, final_y))
