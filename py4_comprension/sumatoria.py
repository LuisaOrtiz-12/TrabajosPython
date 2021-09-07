A = [4,6,8]
B = [2,2,2]
C = [1,2,3]

i = -1
n = len(A)

resultado = sum((A[i] * B[i]) + C[i] for i in range(n))  + pow(n, 2)

print(resultado)