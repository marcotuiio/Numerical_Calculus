import sympy as sp 
import numpy as np
from tabulate import tabulate

### Lembrar que no método de Newton-Cotes N = intervalos já no método de Gauss N = qntd de pontos
 
def trapezio(f, a, b, n, X):
    integral_aprox = 0
    h = (b - a) / n
    ini = a
    for i in range(n):
        integral_aprox = integral_aprox + (f.subs(X, ini) + f.subs(X, ini+h))
        ini = ini + h
    integral_aprox = h/2 * integral_aprox
    # print('Trapezio: ', integral_aprox.round(9))
    return integral_aprox.round(9)

def simpson(f, a, b, n, X):
    h = (b - a) / n
    xi = np.zeros(n+1)
    for i in range(n+1):
        xi[i] = a + i*h

    integral_aprox = f.subs(X, xi[0]) + f.subs(X, xi[n])
    mult = 4
    for i in range(1, n):
        integral_aprox = mult * f.subs(X, xi[i]) + integral_aprox
        if mult == 4:
            mult = 2
        else:
            mult = 4

    integral_aprox = h/3 * integral_aprox
    return integral_aprox.round(9)

def simpson38(f, a, b, n, X):
    integral_aprox = 0
    h = (b - a) / n
    ini = a
    fin = h
    # if n % 3 != 0: # Se não for divisível por 3, não é possível aplicar o método
    #     return 9999999

    for i in range(n//3):
        integral_aprox = integral_aprox + (f.subs(X, ini) + 3*f.subs(X, (2*ini+fin)/3) + 3*f.subs(X, (ini+2*fin)/3) + f.subs(X, fin)) 
        ini = fin
        fin = ini + h
    integral_aprox = 3*h/8 * integral_aprox
    # print('Simpson 3/8: ', integral_aprox.round(9))
    return integral_aprox.round(9)

def gauss_legendre(f, a, b, n, X):
    # Definindo as raizes e Ci padrões do intervalo [-1, 1] 
    raizes_padroes = [np.array([-np.sqrt(3)/3, np.sqrt(3)/3]), 
                    np.array([-np.sqrt(15)/5, 0, np.sqrt(15)/5]), 
                    np.array([-np.sqrt(525+70*np.sqrt(30))/35, -np.sqrt(525-70*np.sqrt(30))/35, np.sqrt(525-70*np.sqrt(30))/35, np.sqrt(525+70*np.sqrt(30))/35]), 
                    np.array([-np.sqrt(245+14*np.sqrt(70))/21, -np.sqrt(245-14*np.sqrt(70))/21, 0, np.sqrt(245-14*np.sqrt(70))/21, np.sqrt(245+14*np.sqrt(70))/21])] 
    Ci_padroes = [np.array([1, 1]), 
                np.array([5/9, 8/9, 5/9]), 
                np.array([(18-np.sqrt(30))/36, (18+np.sqrt(30))/36, (18+np.sqrt(30))/36, (18-np.sqrt(30))/36]), 
                np.array([(322-13*np.sqrt(70))/900, (322+13*np.sqrt(70))/900, 128/225, (322+13*np.sqrt(70))/900, (322-13*np.sqrt(70))/900])] 
    
    # 1 calcular os n xi dependendo do intervalo: 
    vet_x = np.zeros(n) 
    for i in range(n): 
        vet_x[i] = ((b - a)*raizes_padroes[n-2][i] + a + b) / 2 

    aprox = 0 
    for i in range(0, n): 
        aprox = Ci_padroes[n-2][i] * f.subs(X, vet_x[i]) + aprox 

    aprox = aprox * (b - a) / 2 
    # print('Gauss Legendre: ', aprox.round(9))
    return aprox.round(9)

def calcular_erro(aprox, exato, output, n):
    erro = abs(aprox - exato)
    menor = 9999
    for i in range(len(erro)):
        if erro[i] < menor:
            idx = i
            menor = erro[i]

    output.write('\nMais eficiente para N = ' + str(n) + '\n')
    if idx == 0:
        output.write('Trapezio, com erro: ' + str(erro[idx]))
    elif idx == 1:
        output.write('Simpson, com erro: ' + str(erro[idx]))
    elif idx == 2:
        output.write('Simpson 3/8, com erro: ' + str(erro[idx]))
    elif idx == 3:
        output.write('Gauss Legendre, com erro: ' + str(erro[idx]))
    return erro
  
X = sp.Symbol('x') 
Funcoes = []
Intervalos = []

f1 = sp.sqrt((X**2 - 4))
intervalo1 = np.array([3, 2])
Funcoes .append(f1)
Intervalos.append(intervalo1)

f2 = 1 / sp.sqrt((X**3 + 1))
intervalo2 =intervalo1 = np.array([3, 0])
Funcoes .append(f2)
Intervalos.append(intervalo2)

f3 = sp.log(X**3 + 1)
intervalo3 = np.array([2, 0])
Funcoes .append(f3)
Intervalos.append(intervalo3)

f4 = X * sp.sin(sp.rad(sp.pi * X))
intervalo4 = np.array([1, 0])
Funcoes .append(f4)
Intervalos.append(intervalo4)

f5 = 1 / (1 + X)
intervalo5= np.array([2, 1])
Funcoes .append(f5)
Intervalos.append(intervalo5)

f6 =(1 + X) / (1 + X**3)
intervalo6 = np.array([1, 0])
Funcoes .append(f6)
Intervalos.append(intervalo6)

valores_exatos = np.array([1.429254665, 1.65267369, 1.664454348, 0.01827155946, 0.4054651084, 1.209199577])

output = open("atividadeIntegracao_MarcoBarros.txt", "w")
for i in range(len(Funcoes)):
    n2 = []
    n3 = []
    n4 = []
    for n in range (2, 5):
        trap = trapezio(Funcoes[i], Intervalos[i][1], Intervalos[i][0], n, X)
        simp = simpson(Funcoes[i], Intervalos[i][1], Intervalos[i][0], n, X)
        simp38 = simpson38(Funcoes[i], Intervalos[i][1], Intervalos[i][0], n, X)
        gauss = gauss_legendre(Funcoes[i], Intervalos[i][1], Intervalos[i][0], n, X)

        if n == 2:
            n2.append(trap); n2.append(simp); n2.append(simp38); n2.append(gauss)
        elif n == 3:
            n3.append(trap); n3.append(simp); n3.append(simp38); n3.append(gauss)
        elif n == 4:
            n4.append(trap); n4.append(simp); n4.append(simp38); n4.append(gauss)

    output.write('\n--> Função: ' + str(Funcoes[i]))
    output.write('\nValor exato da integral: ' + str(valores_exatos[i]) + '\n')
    output.write(tabulate([['N = 2', n2[0], n2[1], n2[2], n2[3]], ['N = 3', n3[0], n3[1], n3[2], n3[3]], ['N = 4', n4[0], n4[1], n4[2], n4[3]]], 
                          headers=['', 'Trapezio', 'Simpson', 'Simpson 3/8', 'Gauss Legendre'], tablefmt='fancy_grid'))
    
    calcular_erro(n2, valores_exatos[i], output, 2)
    output.write('\n')
    calcular_erro(n3, valores_exatos[i], output, 3)
    output.write('\n')
    calcular_erro(n4, valores_exatos[i], output, 4)

    output.write('\n\n')


    print('\nN = 2: ' + str(n2))
    print('N = 3: ' + str(n3))
    print('N = 4: ' + str(n4))

output.close()