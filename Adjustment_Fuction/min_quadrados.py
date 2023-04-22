import sympy as sp
import numpy as np

def for_line(x, y):
    m = len(x)
    # Somatorios
    x_sum = sum(x)
    y_sum = sum(y)
    x2_sum = sum(x**2)
    xy_sum = sum(x*y)

    # Aplicação das fórmulas
    a_0 = ((x2_sum*y_sum - xy_sum*x_sum) / (m*x2_sum - x_sum**2)).round(3)
    a_1 = ((m*xy_sum - x_sum*y_sum) / (m*x2_sum - x_sum**2)).round(3)

    # Criação da reta
    X = sp.Symbol('x')
    line = a_0 + a_1*X
    print("\nReta: \n", line)

def for_poly(x, y, n):
    m = len(x)

    # Criação das matrizes
    matX = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            for k in range(m):
                matX[i, j] = x[k]**(i+j) + matX[i, j]

    vetY = np.zeros(n)
    for i in range(n):
        for k in range(m):
            vetY[i] = y[k]*x[k]**i + vetY[i]

    # print("matX: \n", matX.round(4))
    # print("vetY: \n", vetY.round(4))

    vetA = seidel(matX, vetY)
    # print("A.i: \n", vetA.round(1))

    # Criação do polinômio
    X = sp.Symbol('x')
    pol = 0
    for i in range(n):
        pol = ((vetA[i]).round(4))*X**i + pol

    print("\nPolinômio: \n", pol)

def seidel(mat, b):
    n = mat.shape[0]
    x = np.zeros(n) 
    erro = np.zeros(n)
    tol = 0.000001
    for k in range(0, 100):
        for i in range(0, n):
            soma = 0
            for j in range(0, n):
                if i != j:
                    soma = -mat[i, j] * x[j] + soma
            prov = x[i]
            x[i] = (b[i] + soma) / mat[i, i]
            erro[i] = abs(x[i] - prov)
        if max(erro) / max(x) < tol:
            return x
    return x

def for_non_linear(x, y):
    m = len(x)
    # Linearização
    x_sum = sum(x)
    Yzao = np.log(y)
    Y_sum = sum(Yzao)
    x2_sum = sum(x**2)
    xY_sum = sum(x*Yzao)

    # Aplicação das fórmulas
    a = ((m*xY_sum - x_sum*Y_sum) / (m*x2_sum - x_sum**2)).round(4)
    B = (x2_sum*Y_sum - xY_sum*x_sum) / (m*x2_sum - x_sum**2)

    b = (sp.exp(B)).round(4)

    # Criação da função
    X = sp.Symbol('x')
    f = b*sp.exp(a*X)    
    print("\nFunção: \n", f)

# x = np.array([0, .25, .5, .75, 1])
# y = np.array([1, 1.2840, 1.6487, 2.1170, 2.7183])
# n = 3

x = np.array([-3, -2, -1, 1, 2, -3])
y = np.array([26, 17, 10, 2, 1, 26])
n = 3

print("---> Mínimos Quadrados para Polinômios")
for_poly(x, y, n)

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([1.3, 3.5, 4.2, 5, 7, 8.8, 10.1, 12.5, 13, 15.6])

# x = np.array([1., 2., 3., 4.])
# y = np.array([3., 5., 6., 8.])

print("\n\n---> Mínimos Quadrados para Reta")
for_line(x, y)  

x = np.array([1, 1.25, 1.5, 1.75, 2])
y = np.array([5.1, 5.79, 6.53, 7.45, 8.46])

print("\n\n---> Mínimos Quadrados para Equações Não Lineares")
for_non_linear(x, y)
