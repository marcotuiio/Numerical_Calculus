from tabulate import tabulate

def func(x):
    return x**3 + 6*x**2 + 12*x - 11

def funcB(x):
    return x**5 - (10/9)*x**3 + (5/21)*x

def bissec(function):
    vetAB = []
    a = -1
    b = 1
    while function(a) * function(b) > 0:
        a = a - 1
        b = b + 1
    
    i = 0
    xm = (a + b) / 2 
    vetAB.append([a, function(a), b, function(b), xm, '-'])
    while i < 15:
        if function(a) * function(xm) < 0:
            b = xm
        else:
            a = xm;
        aux = xm
        xm = (a + b) / 2
        i = i + 1
        vetAB.append([a, function(a), b, function(b), xm, abs(function(xm) - function(aux))])
        if abs(function(xm) - function(aux)) < 0.0001 and i > 3:
            break

    return vetAB

# No caso de utilizar esse programa, alterar a função func(x)
ab = bissec(func)
print(tabulate(ab, headers=["a", "f(a)", "b", "f(b)", "xm", "erro"], tablefmt="grid"))

# teste = bissec(funcB)
# print(tabulate(teste, headers=["a", "f(a)", "b", "f(b)", "xm", "erro"], tablefmt="grid"))