def sumatoria(A,B,C):
 i = -1
 n = len(A)
 acumulador = 0
 for i in range(n):
   d = A[i] * B[i]
   e = d + C[i]
   acumulador = acumulador + e

 resultado = acumulador + pow(n, 2)
 return resultado

A = [4,6,8]
B = [2,2,2]
C = [1,2,3]
print(sumatoria(A,B,C))