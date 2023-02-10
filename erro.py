import numpy as np
from math import factorial

rest = 0
sum = 0
n = 9;

for i in range(n):
    sum = (pow(8, i) / factorial(i)) + sum

for j in range(n,10):
    rest = (pow(8, j) / factorial(j)) + rest

print("sum = ", sum)
print("rest = ", rest)
print("error = ", abs(sum - rest))