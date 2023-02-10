import numpy as np

m = np.asmatrix([[1, 0, 0],
                [10, 9, 0],
                [1, 1, 1]])

# a) matriz triangular superior
aux = 0
for i in range (0, m.shape[0]):
    for j in range (0, m.shape[1]):
        if (i > j and m[i, j] != 0):
            aux += 1
            break

if aux == 0:
    print('É matriz triangular superior')
else:
    print('Não é matriz triangular superior')
print(m, '\n')
        
# b) matriz triangular inferior
aux = 0
for i in range (0, m.shape[0]):
    for j in range (0, m.shape[1]):
        if (j > i and m[i, j] != 0):
            aux += 1
            break

if aux == 0:
    print('É matriz triangular inferior')
else:
    print('Não é matriz triangular inferior')
print(m, '\n')
        
# c) matriz diagonal
aux1 = 0
aux2 = 0
for e in range (0, i):
    for f in range (0, j):
        if (e == f and m[e, f] != 0):
            aux1 += 1
        elif (e != f and m[e, f] == 0):
            aux2 += 1
    
if (aux1 == i and aux2 == i*i-i):
    print('É matriz diagonal')
else:
    print('Não é matriz diagonal')
print(m, '\n')

# d) matriz identidade 
aux1 = 0
aux2 = 0
for e in range (0, i):
    for f in range (0, j):
        if (e == f and m[e, f] == 1):
            aux1 += 1
        elif (e != f and m[e, f] == 0):
            aux2 += 1
    
if (aux1 == i and aux2 == i*i-i):
    print('É matriz identidade')
else:
    print('Não é matriz identidade')
print(m, '\n')

n = np.asmatrix([[1, 2, 0, 0],
                [3, 8, 4, 0],
                [0, 1, 1, 9],
                [0, 0, 1, 1]])

# e) matriz tridiagonal
aux = 0
for i in range (0, n.shape[0]):
    for j in range (0, n.shape[1]):
        if (abs(i - j) > 1 and n[i, j] != 0):
            aux += 1
            break

if aux == 0:
    print('É matriz tridiagonal')
else:
    print('Não é matriz tridiagonal')
print(n, '\n')

# f) matriz pentadiagonal
aux = 0
for i in range (0, n.shape[0]):
    for j in range (0, n.shape[1]):
        if (abs(i - j) > 2 and n[i, j] != 0):
            aux += 1
            break

if aux == 0:
    print('É matriz pentadiagonal')
else:
    print('Não é matriz pentadiagonal')
print(n, '\n')

esp = np.asmatrix([[1, 0, 0, 0, 0,],
                [0, 2, 1, 0, 0],
                [0, 0, 4, 0, 0],
                [0, 0, 0, 6, 0],
                [-2, 0, 0, 0, -7]])

# g) matriz esparsa
count = 0
for i in range (0, esp.shape[0]):
    for j in range (0, esp.shape[1]):
        if esp[i, j] != 0:
            count += 1

if count <= esp.size * 0.3:
    print('É matriz esparsa')
else:
    print('Não é matriz esparsa')
print(esp, '\n')

k = np.asmatrix([[15, 3, 6, 6],
                [-6, 12, 1, 2],
                [1, 1, 13, 5],
                [2, 3, 4, 11]])

# h) matriz diagonalmente dominante
aux = 0
current = 0
for i in range (0, k.shape[0]):
    sum = 0
    for j in range (0, k.shape[1]):
        if i == j:
            current = k[i, j]
        elif i != j:
            sum = sum + abs(k[i, j])
        if (j == k.shape[1]-1):
            if (current >= sum):
                # print(current, sum)
                aux += 1

if (aux == k.shape[0]):
    print('É matriz diagonalmente dominante')
else:
    print('Não é matriz diagonalmente dominante')
print(k, '\n')

            