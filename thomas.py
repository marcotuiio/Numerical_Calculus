import numpy as np

def alg_thomas(mat, d):

    n = mat.shape[0]

    a = np.array(np.zeros((n)))
    b = np.array(np.zeros((n)))
    c = np.array(np.zeros((n)))
    x = np.array(np.ones((n)))

    for i in range(0, n):
        for j in range(0, n):
            if (i == j):
                b[i] = mat[i, j]
            elif (i-1 == j):
                c[j] = mat[i, j] # 01, 12, 23    
            elif (j-1 == i):
                a[i+1] = mat[i, j] # 10, 21, 32

    gama = np.array(np.zeros((n-1)))
    beta = np.array(np.zeros((n)))

    gama[0] = c[0] / b[0]
    for i in range(1, n-1):
        gama[i] = c[i] / (b[i] -a[i] * gama[i-1])

    beta[0] = d[0] / b[0]
    for i in range(1, n):
        beta[i] = (d[i] - a[i] * beta[i-1]) / (b[i-1] - a[i] * gama[i-1])

    # Retrosubstituição    
    x[n-1] = beta[n-1]
    for k in range(n-2, -1, -1): # 2, 1, 0
        x[k] = beta[k] - gama[k] * x[k+1]

    return gama, beta, x

mat = np.asmatrix([[4, -1, 0, 0],
                [-1, 4, -1, 0],
                [0, -1, 4, -1],
                [0, 0, -1, 4]])
d = np.array([23, -15, -6, 6]) 

gama, beta, x = alg_thomas(mat, d)
 
print("gama: ", gama.round(2))
print("beta: ", beta.round(2))
print("x: ", x.round(2))