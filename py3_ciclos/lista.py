def lista(A,B):
 n = len(A)//2
 C = []
 for i in range(n+1):
   d = pow(A[i+1], 2)
   e = d * B[2*i]
   f = e + B[n+i]
   C.append(f)

 print(C)

A = [4,6,8,2]
B = [2,1,0,-1]
lista(A,B)