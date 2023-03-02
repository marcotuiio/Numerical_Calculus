import numpy as np

def elim_gauss(A, b):
    # Triangularização
    Ab = np.concatenate((A, b), 1)  # 1 = concatena pela coluna
    n = np.shape(Ab)[0]
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            # Pivotamento
            if Ab[i, i] == 0:
                for k in range(i + 1, n):
                    if Ab[k, i] != 0:
                        Ab[[i, k]] = Ab[[k, i]] # troca linhas
                        break
            pivot = Ab[i, i]
            m = Ab[j, i] / pivot
            for k in range(0, n + 1):
                Ab[j, k] = Ab[j, k] - m * Ab[i, k]

    # Retrosubstituição
    X = np.ones(n)
    for i in range(n - 1, -1, -1):
        X[i] = Ab[i, n]
        for j in range(i + 1, n):
            X[i] = X[i] - Ab[i, j] * X[j]
        X[i] = X[i] / Ab[i, i]

    return Ab, X

# Exemplo que precisa de pivotamento
A = np.array([[0, 2, 2],
              [1, 2, 1],
              [1, 1, 1]], dtype='double')

b = np.array([8, 9, 6]).reshape(-1, 1)

# A = np.array([[10, 1, -1, 2],
#               [4, 9, -1, 3],
#               [2, -2, 12, 5],
#               [1, -3, 5, 15]], dtype='double')

# b = np.array([-33, 8, 11, -11]).reshape(-1, 1)

ab, x = elim_gauss(A, b)

print("Matriz A|b Triangularizada: \n", ab.round(2))
print("\nVetor solução:\n", x)
