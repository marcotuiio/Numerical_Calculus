import numpy as np

def elim_gauss(A, b):
    # Triangularização
    Ab = np.concatenate((A, b), 1)  # 1 = concatena pela coluna
    n = np.shape(Ab)[0]
    for i in range(0, n - 1):
        for j in range(i + 1, n):
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


# Matriz do exemplo que está no slide
A = np.array([[8, -2, 5],
              [4, 8, 5],
              [2, -2, 10]], dtype='double')

b = np.array([-1, 15, -12]).reshape(-1, 1)

# Matriz do exercício do slide
# A = np.array([[10, 1, -1, 2],
#               [4, 9, -1, 3],
#               [2, -2, 12, 5],
#               [1, -3, 5, 15]], dtype='double')
#
# b = np.array([-33, -8, 11, -11]).reshape(-1, 1)

ab, x = elim_gauss(A, b)

print("Matriz A|b Triangularizada: \n", ab)
print("\nVetor solução:\n", x)
