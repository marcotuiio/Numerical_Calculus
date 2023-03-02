from tabulate import tabulate

def func(x):
    return x**3 + 6*x**2 + 12*x - 11

def secantes(function, x0, x1):
    vetX = []

    i = 0
    while i < 10:
        x2 = x1 - function(x1) * (x1 - x0) / (function(x1) - function(x0))
        vetX.append([x0, function(x0), x1, function(x1), x2, abs(x2 - x1)])
        x0 = x1
        x1 = x2
        if abs(x1 - x0) < 0.00001:
            break
        i += 1
    
    return vetX

## no caso de utilizar esse programa, alterar a função func(x) e os valores iniciais x0 e x1
x = secantes(func, -1, 0)
print(tabulate(x, headers=["x0", "f(x0)", "x1", "f(x1)", "x2", "erro"], tablefmt="grid"))