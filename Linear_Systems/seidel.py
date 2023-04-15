import numpy as np

def seidel(mat, b):
    n = mat.shape[0]
    x = np.zeros(n) 
    erro = np.zeros(n)
    tol = 0.000001
    print("Erro tolerado: %lf\n" % (tol))
    for k in range(0, 100):
        # print("Iteração:", k, "- X:", x)
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


#### Definir o erro tolerado na função
#### Se não for possivel encerrar via erro tolerado, a função deve encerrar após 15 iterações
print("Método de Seidel")
mat = np.asmatrix([[10., 5., -2.],
                   [3., 12., 4.],
                    [-5., -6., 15.]])
b = np.array([13., 19., 4.]) 

# mat = np.asmatrix([[-2., 1., 0., 0.],
#                 [1., -2., 1., 0.],
#                 [0., 1., -2., 1.],
#                 [0., 0., 1., -2.],])
# b = np.array([-1., 0., 0., 0.])

x = seidel(mat, b)
print("Vetor resultado aproximado X:\n", x)