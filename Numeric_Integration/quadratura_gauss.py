import numpy as np
import sympy as sp

### Informe abaixo a função f(x), o intervalo [a, b] e o número de pontos n

def quadr_gauss(a, b, n, f, X):
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

    print('\nPontos xi =', vet_x)
    aprox = 0
    for i in range(0, n):
        aprox = Ci_padroes[n-2][i] * f.subs(X, vet_x[i]) + aprox

    print('\nFunção f(x) =', f)
    aprox = aprox * (b - a) / 2
    print('\nIntegral aproximada para n =', n, 'no intervalo [', a, ',', b, '] =', aprox.round(6), '\n')

X = sp.Symbol('x')
n = 4
a = -3
b = 2
f = sp.exp(-X)*sp.cos(sp.rad(X))

quadr_gauss(a, b, n, f, X)
