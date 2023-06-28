import sympy as sp

### Altere o valor n, o intervalo [a,b] e a função f(x) que deseja integrar por aproximação

def newton_cotes(f, a, b, n):
    print("\nMétodo de Newton-Cotes\n")
    
    integral_aprox = 0;
    h = (b - a) / n
    if n == 1: # regra do trapézio
        integral_aprox = (h/2) * (f.subs(X, a) + f.subs(X, b))
    elif n == 2: # regra de Simpson
        integral_aprox = (h/3) * (f.subs(X, a) + 4*f.subs(X, (a+b)/2) + f.subs(X, b))
    elif n == 3: # regra de 3/8 de Simpson
        integral_aprox = (3*h/8) * (f.subs(X, a) + 3*f.subs(X, (2*a+b)/3) + 3*f.subs(X, (a+2*b)/3) + f.subs(X, b))
    elif n == 4: # regra de newton-cotes generalizada  
        integral_aprox = (2*h/45) * (7*f.subs(X, a) + 32*f.subs(X, (3*a+b)/4) + 12*f.subs(X, (a+b)/2) + 32*f.subs(X, (a+3*b)/4) + 7*f.subs(X, b))
    else:
        print("Não é possível calcular a integral com o número de pontos informado.")
        return

    print('Função f(x) =', f)
    print('Aproximação: ', integral_aprox)
    print('Integral aproximada para n =', n)
    print('No intervalo [', a, ',', b, '] =')
    print('---> ', (integral_aprox.evalf()).round(6))

X = sp.Symbol('x')
# n = 3
# a = 0
# b = sp.pi / 4
# f = sp.sin(X)

# f = sp.sqrt((X**2 - 4))
# n = 3
# a = 2
# b = 3

f = 1 / (1 + X)
n = 3
a = 1
b = 2
newton_cotes(f, a, b, n)
