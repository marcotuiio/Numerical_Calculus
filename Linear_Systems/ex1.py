import numpy as np

def seidel(mat, b):
    n = mat.shape[0]
    x = np.zeros(n) 
    erro = np.zeros(n)
    tol = 0.000001
    iteracoes = 0
    for k in range(0, 100):
        iteracoes = iteracoes + 1
        for i in range(0, n):
            soma = 0
            for j in range(0, n):
                if i != j:
                    soma = -mat[i, j] * x[j] + soma
            prov = x[i]
            x[i] = (b[i] + soma) / mat[i, i]
            erro[i] = abs(x[i] - prov)
        if max(erro) / max(x) < tol:
            return x, iteracoes, max(erro) / max(x)
        if np.linalg.norm(x[i] - prov) < tol:
            return x, iteracoes, np.linalg.norm(x[i] - prov)

    return x, iteracoes, max(erro) / max(x)

def jacobi(mat, b):
    n = mat.shape[0]
    x = np.zeros(n)
    aux = np.zeros(n)
    erro = np.zeros(n)
    tol = 0.000001
    iteracoes = 0
    for k in range(0, 100):
        iteracoes = iteracoes + 1
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
            return x, iteracoes, max(erro) / max(x)
        if np.linalg.norm(x[i] - x[i-1]) < tol:
            return x, iteracoes, np.linalg.norm(x[i] - x[i-1])
        
    return x, iteracoes, max(erro) / max(x)

def matriz_diagonalmente_dominante(mat):
    aux = 0
    current = 0
    for i in range (0, mat.shape[0]):
        sum = 0
        for j in range (0, mat.shape[1]):
            if i == j:
                current = mat[i, j]
            elif i != j:
                sum = sum + abs(mat[i, j])
            if (j == mat.shape[1]-1):
                if (current >= sum):
                    # print(current, sum)
                    aux += 1

    if (aux == mat.shape[0]):
        return True
    
sistemas = []
vetores = []    

s1 = np.asmatrix([[10., -2., 1.],
                [-2., 10., -2.],
                [-2., -5., 10.],])
b1 = np.array([9., 12., 18.])
sistemas.append(s1)
vetores.append(b1)

s2 = np.asmatrix([[4., -1., 0.],
                [1., 3., -1.],
                [1., 0., 2.],])
b2 = np.array([3., -4., 5.])
sistemas.append(s2)
vetores.append(b2)

s3 = np.asmatrix([[5., -1., 0.],
                [-1., 5., -1.],
                [-0., -1., 5.],])
b3 = np.array([9., 4., -6.])
sistemas.append(s3)
vetores.append(b3)

s4 = np.asmatrix([[8., 1., -1.],
                [1., 7., -2.],
                [2., 1., 9.],])
b4 = np.array([8., 4., 12.])
sistemas.append(s4)
vetores.append(b4)

s5 = np.asmatrix([[4., 1., 0.],
                [1., 4., -1.],
                [0., -1., 4.],])
b5 = np.array([3., 4., 5.])
sistemas.append(s5)
vetores.append(b5)

s6 = np.asmatrix([[-2., 1., 0., 0.],
                [1., -2., 1., 0.],
                [0., 1., -2., 1.],
                [0., 0., 1., -2.],])
b6 = np.array([-1., 0., 0., 0.])
sistemas.append(s6)
vetores.append(b6)

s7 = np.asmatrix([[5., 1., 0., 0.],
                [1., 5., 1., 0.],
                [0., 1., 5., 1.],
                [0., 0., 1., 5.],])
b7 = np.array([33., 26., 30., 15.])
sistemas.append(s7)
vetores.append(b7)

s8 = np.asmatrix([[1., 2., 0., 0.],
                [2., 6., 8., 0.],
                [0., 8., 35., 18.],
                [0., 0., 18., 112.],])
b8 = np.array([2., 6., -10., -112.])
sistemas.append(s8)
vetores.append(b8)

s9 = np.asmatrix([[4., 8., 0., 0.],
                [8., 18., 2., 0.],
                [0., 2., 5., 1.5],
                [0., 0., 1.5, 1.75],])
b9 = np.array([8., 18., 0.5, -1.75])
sistemas.append(s9)
vetores.append(b9)

s10 = np.asmatrix([[-2.90, 0.90, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.01],
                   [1.00, -2.90, 0.90, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.01],
                   [0.00, 1.00, -2.90, 0.90, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],
                   [0.00, 0.00, 1.00, -2.90, 0.90, 0.00, 0.00, 0.00, 0.00, 0.00],
                   [0.00, 0.01, 0.00, 0.00, 1.00, -2.90, 0.90, 0.00, 0.00, 0.00],
                   [0.00, 0.00, 0.00, 0.00, 1.00, -2.90, 0.90, 0.00, 0.00, 0.00],
                   [0.00, 0.00, 0.00, 0.00, 0.00, 1.00, -2.90, 0.90, 0.00, 0.00],
                   [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 1.00, -2.90, 0.90, 0.00],
                   [0.00, 0.01, 0.00, 0.00, 0.00, 0.00, 0.00, 1.00, -2.90, 0.90],
                   [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 1.00, -2.90]])
b10 = np.array([-0.14, -0.08, -0.15, -0.17, -0.18, -0.26, -0.29, -0.38, -0.35, -1.05])
sistemas.append(s10)
vetores.append(b10)

output = open("outputEx1MarcoBarros.txt", "a")

for i in range(len(sistemas)):
    s = sistemas[i]
    b = vetores[i]
    xj, itj, ej = jacobi(s, b)
    xs, its, es = seidel(s, b)
    output.write("Sistema " + str(i+1) + ":\n")
    
    output.write("\tJacobi:\n")
    output.write("\t\tx = " + str(xj) + "\n")
    output.write("\t\tIterações = " + str(itj) + "\n")
    output.write("\t\tErro = " + str(ej) + "\n")
    
    output.write("\tSeidel:\n")
    output.write("\t\tx = " + str(xs) + "\n")
    output.write("\t\tIterações = " + str(its) + "\n")
    output.write("\t\tErro = " + str(es) + "\n")
    
    output.write("\n\tConclusão sob iterações: ")
    if itj < its:
        output.write("Jacobi converge mais rapido nas iteracoes\n")
    else:
        output.write("Seidel converge mais rapido nas iteracoes\n")

    output.write("\tConclusão sob erro: ")
    if ej < es:
        output.write("Jacobi converge mais rapido no erro\n")
    else:
        output.write("Seidel converge mais rapido no erro\n")

    output.write("\n--------------------------------------------\n\n")

output.close()