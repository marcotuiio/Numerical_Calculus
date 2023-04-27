import numpy as np
import sympy as sp

def quadr_gauss(a, b, n, f):
    # Definindo as raizes e Ci padrões do intervalo [-1, 1]
    raizes_padroes = [np.array([-1.3*np.sqrt(3), 1.3*np.sqrt(3)]),
                    np.array([-np.sqrt(15)/5, 0, np.sqrt(15)/5]),
                    np.array([-np.sqrt(525+70*np.sqrt(30))/35, -np.sqrt(525-70*np.sqrt(30))/35, np.sqrt(525-70*np.sqrt(30))/35, np.sqrt(525+70*np.sqrt(30))/35]),
                    np.array([-np.sqrt(245+14*np.sqrt(70))/21, -np.sqrt(245-14*np.sqrt(70))/21, 0, np.sqrt(245-14*np.sqrt(70))/21, np.sqrt(245+14*np.sqrt(70))/21])]
    Ci_padroes = [np.array([1, 1]),
                np.array([5/9, 8/9, 5/9]),
                np.array([(18-np.sqrt(30))/36, (18+np.sqrt(30))/36, (18+np.sqrt(30))/36, (18-np.sqrt(30))/36]),
                np.array([(322-13*np.sqrt(70))/900, (322+13*np.sqrt(70))/900, 128/225, (322+13*np.sqrt(70))/900, (322-13*np.sqrt(70))/900])]
    
    vet_x = np.zeros(n)
    # 1 calcular os n xi dependendo do intervalo:
    for i in range(n):
        vet_x[i] = ((b - a)*raizes_padroes[n-2][i] + a + b) / 2

    aprox = 0
    for i in range(n):
        aprox = Ci_padroes[n-2][i] * f(vet_x[i]) + aprox
    
    aprox = aprox * (b - a) / 2
    print("Aproximação: ", aprox)

X = sp.Symbol('x')
n = 2
a = -3
b = 2
f = sp.exp(-X)*sp.cos(X)

quadr_gauss(a, b, n, f)

