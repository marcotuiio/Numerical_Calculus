import numpy as np

def seidel(mat, b):
    n = mat.shape[0]
    x = np.zeros(n) 
    erro = np.zeros(n)
    tol = 0.000001
    print("Erro tolerado: %lf\n" % (tol))
    for k in range(0, 10):
        print("Iteração:", k, "- X:", x)
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
mat = np.asmatrix([[10., 1.],
                [1., 8.]])
b = np.array([23., 26.]) 

x = seidel(mat, b)
print("\nVetor resultado aproximado X:\n", x)