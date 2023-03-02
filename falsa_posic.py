from tabulate import tabulate

def func(x):
    return x**3 + 6*x**2 + 12*x - 11

def calc_x(a, b, function):
    return (a * function(b) - b * function(a)) / (function(b) - function(a))

def falsa_posic(function):
    vetAB = []
    a = -1
    b = 1
    while function(a) * function(b) > 0:
        a = a - 1
        b = b + 1

    i = 0
    xm = calc_x(a, b, function)
    vetAB.append([a, function(a), b, function(b), xm, '-'])
    while i < 10 or abs(function(xm)) >= 0.0001:
        vetAB.append([a, function(a), b, function(b), xm, abs(function(xm))])
        if function(a) * function(xm) < 0:
            b = xm
        else:
            a = xm;
        xm = calc_x(a, b, function)
        i = i + 1

    return vetAB

# No caso de utilizar esse programa, alterar a função func(x) 
ab = falsa_posic(func)
print(tabulate(ab, headers=["a", "f(a)", "b", "f(b)", "xm", "erro"], tablefmt="grid"))
