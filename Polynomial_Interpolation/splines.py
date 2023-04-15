import numpy as np  
import sympy as sp
import matplotlib.pyplot as plt

def splines(x, y, deriv, var):
    n = len(x)
    ini = deriv.subs(var, x[0])
    fim = deriv.subs(var, x[n-1])

    a = np.zeros(n)
    for i in range(0, n):
        a[i] = y[i]

    h = np.zeros(n - 1)
    for i in range(0, n - 1):
        h[i] = x[i + 1] - x[i]

    matA = np.asmatrix(np.zeros((n, n)))
    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                if i == 0:
                    matA[i, j] = 2 * h[i]
                elif i == n - 1:
                    matA[i, j] = 2 * h[i-1]
                else:
                    matA[i, j] = 2 * (h[i-1] + h[i])
            elif abs(i - j) == 1:
                matA[i, j] = h[max(i, j) - 1]

    matB = np.zeros(n)
    for i in range(0, n):
        if i == 0:
            matB[i] = 3 * (a[i + 1] - a[i]) / h[i] - 3 * ini
        elif i == n - 1:
            matB[i] = 3 * fim - 3 * (a[i] - a[i - 1]) / h[i - 1]
        else:
            matB[i] = (3 * (a[i + 1] - a[i]) / h[i]) - (3 * (a[i] - a[i - 1]) / h[i - 1])

    c = seidel(matA, matB)

    b = np.zeros(n-1)

    for i in range(0, n-1): 
        b[i] = ((a[i+1] - a[i]) / h[i] - h[i] * (c[i+1] + 2 * c[i]) / 3).round(4)

    d = np.zeros(n-1)

    for i in range(0, n-1):
        d[i] = (c[i+1] - c[i]) / (3 * h[i])

    for i in range(0, n-1):
        d[i] = d[i].round(4)

    # print("\na: ", a)
    # print("b: ", b)
    # print("c: ", c)
    # print("d: ", d)

    # montar as equações dos splines
    spline_list = []
    for i in range(0, n-1):
        spline = (a[i] + b[i] * (var - x[i]) + c[i] * (var - x[i])**2 + d[i] * (var - x[i])**3).evalf(n=4)
        spline_list.append(spline)

    return spline_list

def plot_graph(x, y, function, splines_list, identificador):
    var = sp.Symbol('x')
    f = sp.lambdify(var, function, "numpy")
    x_vals = np.linspace(x[0], x[len(x)-1], 50)
    y_vals = f(x_vals)
    plt.plot(x_vals, y_vals, label='Função') # Plotar a função

    for i in range(0, len(splines_list)):
        f = sp.lambdify(var, splines_list[i], "numpy")
        y_vals = f(x_vals)
        plt.plot(x_vals, y_vals, label='Spline ' + str(i)) # Plotar as splines

    plt.xlabel('x') # Definir o rótulo do eixo x
    plt.ylabel('y') # Definir o rótulo do eixo y
    plt.grid(True) # Adicionar uma grade ao gráfico
    plt.legend() # Adicionar uma legenda ao gráfico
    plt.savefig('splines_teste_'+identificador+'.png') # Salvar o gráfico em um arquivo PNG
    # plt.show() # Mostrar o gráfico

def seidel(mat, b):
    n = mat.shape[0]
    x = np.zeros(n) 
    erro = np.zeros(n)
    tol = 0.000001
    for k in range(0, 100):
        # print("Iteração:", k, "- X:", x)
        for i in range(0, n):
            soma = 0
            for j in range(0, n):
                if i != j:
                    soma = -mat[i, j] * x[j] + soma
            prov = x[i]
            x[i] = ((b[i] + soma) / mat[i, i]).round(4)
            erro[i] = abs(x[i] - prov)
        if max(erro) / max(x) < tol:
            return x

    return x

var_x = sp.Symbol('x')

# print(" --- Teste 1")
# x = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3])
# y = np.array([4, 0, -2, 0, 1, 0, -0.5])
# function = 2**(2 - var_x) * sp.cos(sp.pi * var_x)
# deriv = sp.diff(function, var_x)

# splines_list = splines(x, y, deriv, var_x)
# for i in range(0, len(splines_list)):
#     print("Spline", i, ":", splines_list[i])
# plot_graph(x, y, function, splines_list, '1')

# print("\n\n --- Teste 2")
# x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# y = np.array([2, 0, 0.6667, 0, 0.4, 0, 0.2857, 0, 0.2222, 0, 0.1818])
# function = (1 + sp.cos(sp.pi * var_x)) / 1 + var_x
# deriv = sp.diff(function, var_x)

# splines_list = splines(x, y, deriv, var_x)
# for i in range(0, len(splines_list)):
#     print("Spline", i, ":", splines_list[i])
# plot_graph(x, y, function, splines_list, '2')

# print("\n\n --- Teste 3")
# x = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3])
# y = np.array([-0.3333, -0.2703, -0.2, -0.1333, -0.0769, -0.0328, 0])
# function = (var_x - 3) / (var_x**2 + 9)
# deriv = sp.diff(function, var_x)

# splines_list = splines(x, y, deriv, var_x)
# for i in range(0, len(splines_list)):
#     print("Spline", i, ":", splines_list[i])
# plot_graph(x, y, function, splines_list, '3')

print("\n\n --- Teste 4")
x = np.array([0, 1, 2, 3, 4, 5, 6])
y = np.array([-0.33, -0.2, -0.08, 0, 0.04, 0.06, 0.07])
function = (var_x - 3) / (var_x**2 + 9)
deriv = sp.diff(function, var_x)

splines_list = splines(x, y, deriv, var_x)
for i in range(0, len(splines_list)):
    print("Spline", i, ":", splines_list[i])
plot_graph(x, y, function, splines_list, '4')