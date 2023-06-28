import sympy as sp

def adams_bash(ordem, f, x_values, y_values, final_x, h=0.1):
    
    match ordem:

        case 2:
            print('-> Método de Adams-Bashforth de ordem 2')
            n = 0
            while x_values[-1] < final_x:
                if n < 1: # Usar Runge-Kutta de ordem 2 para gerar os 2 primeiros valores
                    next_y = y_values[n] + h*f.subs({x:x_values[n], y:y_values[n]})
                    x_values.append(x_values[n] + h)

                    aux1 = f.subs({x:x_values[n], y:y_values[n]})
                    aux2 = f.subs({x:x_values[n+1], y:next_y})
                    y_values.append(y_values[n] + h/2*(aux1 + aux2))
                    
                else:
                    f_n = f.subs({x:x_values[n], y:y_values[n]})
                    f_n1 = f.subs({x:x_values[n-1], y:y_values[n-1]})
                    next_y = y_values[n] + h/2*(3*f_n - f_n1)
                    # print(n, next_y)

                    x_values.append(x_values[n] + h)
                    y_values.append(next_y)
                n += 1
            
        case 4:
            print('-> Método de Adams-Bashforth de ordem 4')
            n = 0
            while x_values[-1] < final_x:
                if n < 3: # Usar Runge-Kutta de ordem 4 para gerar os 4 primeiros valores
                    k1 = h*f.subs({x:x_values[n], y:y_values[n]})
                    k2 = h*f.subs({x:x_values[n] + h/2, y:y_values[n] + k1/2})
                    k3 = h*f.subs({x:x_values[n] + h/2, y:y_values[n] + k2/2})
                    k4 = h*f.subs({x:x_values[n] + h, y:y_values[n] + k3})

                    next_y = y_values[n] + 1/6*(k1 + 2*k2 + 2*k3 + k4)
                    y_values.append(next_y)
                    x_values.append(x_values[n] + h)
                
                else:
                    f_n = f.subs({x:x_values[n], y:y_values[n]})
                    f_n1 = f.subs({x:x_values[n-1], y:y_values[n-1]})
                    f_n2 = f.subs({x:x_values[n-2], y:y_values[n-2]})
                    f_n3 = f.subs({x:x_values[n-3], y:y_values[n-3]})
                    next_y = y_values[n] + h/24*(55*f_n - 59*f_n1 + 37*f_n2 - 9*f_n3)
                    # print(n, next_y)
                    
                    x_values.append(x_values[n] + h)
                    y_values.append(next_y) 
                n += 1

    return y_values[-1]

y = sp.Symbol('y')
x = sp.Symbol('x')
x_values = []
y_values = []

ordem = 4

f_xy = -2*y 
x_values.append(0)
y_values.append(1)
h = 0.2
final_x = 1

final_y = adams_bash(ordem, f_xy, x_values, y_values, final_x, h)
print('APROXIMADO: y({}) = {}'.format(final_x, final_y))