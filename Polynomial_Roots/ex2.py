import numpy as np
from tabulate import tabulate

def funcA(x):
    return 2*x**5 - 15*x**4 + 13*x**3 - 9*x**2 - 8*x + 12

def funcB(x):
    return x**5 - (10/9)*x**3 + (5/21)*x

def funcC(x):
    return x**3 - 0.25*x**2 + 0.75*x - 2

def funcD(x):
    return 0.2*x**3 - 3.006*x**2 + 15.06*x - 25.15

def funcE(x):
    return (1/100) * x**5 + x**4 + 3*x + 1

def funcF(x):
    return x**3 - 7.5*x**2 + 12*x + 3

def funcG(x):
    return 0.25*x**4 + 2*x**3 - 7.5*x**2 + 3

def bissec(function):
    vetAB = []
    a = -1
    b = 1
    while function(a) * function(b) > 0:
        a = a - 1
        b = b + 1
    
    i = 0
    xm = (a + b) / 2 
    vetAB.append([i, xm, '-'])
    while i < 15 or abs(function(xm)) >= 0.00001:
        vetAB.append([i, xm, abs(function(xm))])
        if function(a) * function(xm) < 0:
            b = xm
        else:
            a = xm;
        xm = (a + b) / 2
        i = i + 1

    return vetAB

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
    vetAB.append([i, xm, '-'])
    while i < 15 or abs(function(xm)) >= 0.00001:
        vetAB.append([i, xm, abs(function(xm))])
        if function(a) * function(xm) < 0:
            b = xm
        else:
            a = xm;
        xm = calc_x(a, b, function)
        i = i + 1

    return vetAB

def secantes(function, x0, x1):
    vetX = []

    i = 0
    while i < 15:
        x2 = x1 - function(x1) * (x1 - x0) / (function(x1) - function(x0))
        vetX.append([i, x2, abs(x2 - x1)])
        x0 = x1
        x1 = x2
        if abs(x1 - x0) < 0.00001:
            break
        i += 1
    
    return vetX

def newton_raphson(expression, initial, output):
    vetX = []
    derivative = expression.deriv()
    i = 0
    x1 = initial
    while i < 15:
        if derivative(x1) == 0:
            output.write("Derivada nula na iteração %d, portanto não converge por esse método\n" % i)
            vetX.append([i, x1, -9999])
            break
        x2 = x1 - (expression(x1) / derivative(x1))
        vetX.append([i, x2, abs(x2 - x1)])
        if abs(x2 - x1) < 0.00001:
            break
        x1 = x2
        i = i + 1
    return vetX

polinomios = []
polinomios.append(funcA)
polinomios.append(funcB)
polinomios.append(funcC)
polinomios.append(funcD)
polinomios.append(funcE)
polinomios.append(funcF)
polinomios.append(funcG)

exps = []
exps.append(np.poly1d([2, -15, 13, -9, -8, 12]))
exps.append(np.poly1d([1, 0, -10/9, 0, 5/21, 0]))
exps.append(np.poly1d([1, -0.25, 0.75, -2]))
exps.append(np.poly1d([0.2, -3.006, 15.06, -25.15]))
exps.append(np.poly1d([0.01, 1, 0, 3, 0, 1]))
exps.append(np.poly1d([1, -7.5, 12, 3]))
exps.append(np.poly1d([0.25, 2, -7.5, 0, 3]))

output = open("outputEx2MarcoBarros.txt", "a")

for i in range(len(polinomios)):
    vet_bissec = bissec(polinomios[i])
    vet_falsa_posic = falsa_posic(polinomios[i])
    vet_secantes = secantes(polinomios[i], -1, 1)
    vet_newton_raphson = newton_raphson(exps[i], 0, output)

    output.write("Polinômio %d" % (i+1))

    output.write("\n\n Bissecção: \n")
    output.write(tabulate(vet_bissec, headers=["i", "xm", "erro"], tablefmt="fancy_grid"))
    output.write("\n\n Falsa Posição: \n")
    output.write(tabulate(vet_falsa_posic, headers=["i", "xm", "erro"], tablefmt="fancy_grid"))
    output.write("\n\n Secantes: \n")
    output.write(tabulate(vet_secantes, headers=["i", "xm", "erro"], tablefmt="fancy_grid"))
    output.write("\n\n Newton Raphson: \n")
    output.write(tabulate(vet_newton_raphson, headers=["i", "xm", "erro"], tablefmt="fancy_grid"))

    output.write("\n\nConclusão quanto as iterações: ")
    if len(vet_bissec) < len(vet_falsa_posic) and len(vet_bissec) < len(vet_secantes) and len(vet_bissec) < len(vet_newton_raphson):
        output.write("\n\t\tBissecção convergiu mais rápido")
    elif len(vet_falsa_posic) < len(vet_bissec) and len(vet_falsa_posic) < len(vet_secantes) and len(vet_falsa_posic) < len(vet_newton_raphson):
        output.write("\n\t\tFalsa Posição convergiu mais rápido")
    elif len(vet_secantes) < len(vet_bissec) and len(vet_secantes) < len(vet_falsa_posic) and len(vet_secantes) < len(vet_newton_raphson):
        output.write("\n\t\tSecantes convergiu mais rápido")
    elif len(vet_newton_raphson) < len(vet_bissec) and len(vet_newton_raphson) < len(vet_falsa_posic) and len(vet_newton_raphson) < len(vet_secantes):
        output.write("\n\t\tNewton Raphson convergiu mais rápido")
    else:
        output.write("\n\t\Mais de um método convergiu no mesmo número de iterações")

    output.write("\n\nConclusão quanto aos erros: ")
    if vet_bissec[len(vet_bissec)-1][2] < vet_falsa_posic[len(vet_falsa_posic)-1][2] and vet_bissec[len(vet_bissec)-1][2] < vet_secantes[len(vet_secantes)-1][2] and vet_bissec[len(vet_bissec)-1][2] < vet_newton_raphson[len(vet_newton_raphson)-1][2]:
        output.write("\n\t\tBissecção convergiu com menor erro")
    elif vet_falsa_posic[len(vet_falsa_posic)-1][2] < vet_bissec[len(vet_bissec)-1][2] and vet_falsa_posic[len(vet_falsa_posic)-1][2] < vet_secantes[len(vet_secantes)-1][2] and vet_falsa_posic[len(vet_falsa_posic)-1][2] < vet_newton_raphson[len(vet_newton_raphson)-1][2]:
        output.write("\n\t\tFalsa Posição convergiu com menor erro")
    elif vet_secantes[len(vet_secantes)-1][2] < vet_bissec[len(vet_bissec)-1][2] and vet_secantes[len(vet_secantes)-1][2] < vet_falsa_posic[len(vet_falsa_posic)-1][2] and vet_secantes[len(vet_secantes)-1][2] < vet_newton_raphson[len(vet_newton_raphson)-1][2]:
        output.write("\n\t\tSecantes convergiu com menor erro")
    elif vet_newton_raphson[len(vet_newton_raphson)-1][2] < vet_bissec[len(vet_bissec)-1][2] and vet_newton_raphson[len(vet_newton_raphson)-1][2] < vet_falsa_posic[len(vet_falsa_posic)-1][2] and vet_newton_raphson[len(vet_newton_raphson)-1][2] < vet_secantes[len(vet_secantes)-1][2]:
        output.write("\n\t\tNewton Raphson convergiu com menor erro")
    else:
        output.write("\n\t\Mais de um método convergiu com o mesmo erro")

    output.write("\n\n--------------------------------------------\n\n")
    
output.close()
    