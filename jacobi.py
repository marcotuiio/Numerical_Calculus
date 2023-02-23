import numpy as np

def jacobi(mat, b):
    n = mat.shape[0]
    x = np.zeros(n)
    aux = np.zeros(n)
    erro = np.zeros(n)
    tol = 0.000001
    print("Erro tolerado: %f\n" % (tol))
    for k in range(0, 15):
        print("Iteração:", k, "- X:", x)
        for i in range(0, n):
            soma = 0
            for j in range(0, n):
                if i != j:
                    soma = -mat[i, j] * x[j] + soma
            aux[i] = (b[i] + soma) / mat[i, i]
            erro[i] = abs(aux[i] - x[i])
        for t in range(0, n):
            x[t] = aux[t]
        if max(erro) / max(x) < tol:
            return x

    return x

#### Definir o erro tolerado na função
#### Se não for possivel encerrar via erro tolerado, a função deve encerrar após 15 iterações
print("Método de Jacobi")
mat = np.asmatrix([[10., 1.],
                [1., 8.]])
b = np.array([23., 26.]) 

x = jacobi(mat, b)
print("\nVetor resultado aproximado X:\n", x)