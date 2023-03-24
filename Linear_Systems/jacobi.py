import numpy as np

def jacobi(mat, b):
    n = mat.shape[0]
    x = np.zeros(n)
    aux = np.zeros(n)
    erro = np.zeros(n)
    tol = 0.000001
    print("Erro tolerado: %f\n" % (tol))
    for k in range(0, 100):
        # print("\nIteração:", k, "- X:", x)
        for i in range(0, n):
            soma = 0
            for j in range(0, n):
                if i != j:
                    soma = -mat[i, j] * x[j] + soma
            aux[i] = (b[i] + soma) / mat[i, i]
            erro[i] = abs(aux[i] - x[i])
            # print("Erro máximo: %f" % (max(erro) / max(x)))
        for t in range(0, n):
            x[t] = aux[t]
        if max(erro) / max(x) < tol:
            return x

    return x

#### Definir o erro tolerado na função
#### Se não for possivel encerrar via erro tolerado, a função deve encerrar após 15 iterações
print("Método de Jacobi")
mat = np.asmatrix([[10., 5., -2.],
                   [3., 12., 4.],
                    [-5., -6., 15.]])
b = np.array([13., 19., 4.]) 

# mat = np.asmatrix([[-2.90, 0.90, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.01],
#                    [1.00, -2.90, 0.90, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.01],
#                    [0.00, 1.00, -2.90, 0.90, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],
#                    [0.00, 0.00, 1.00, -2.90, 0.90, 0.00, 0.00, 0.00, 0.00, 0.00],
#                    [0.00, 0.01, 0.00, 0.00, 1.00, -2.90, 0.90, 0.00, 0.00, 0.00],
#                    [0.00, 0.00, 0.00, 0.00, 1.00, -2.90, 0.90, 0.00, 0.00, 0.00],
#                    [0.00, 0.00, 0.00, 0.00, 0.00, 1.00, -2.90, 0.90, 0.00, 0.00],
#                    [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 1.00, -2.90, 0.90, 0.00],
#                    [0.00, 0.01, 0.00, 0.00, 0.00, 0.00, 0.00, 1.00, -2.90, 0.90],
#                    [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 1.00, -2.90]])
# b = np.array([-0.14, -0.08, -0.15, -0.17, -0.18, -0.26, -0.29, -0.38, -0.35, -1.05])

# mat = np.asmatrix([[-2., 1., 0., 0.],
#                 [1., -2., 1., 0.],
#                 [0., 1., -2., 1.],
#                 [0., 0., 1., -2.],])
# b = np.array([-1., 0., 0., 0.])

x = jacobi(mat, b)
print("Vetor resultado aproximado X:\n", x)