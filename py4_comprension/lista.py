A = [4,6,8,2]
B = [2,1,0,-1]

n = len(A)//2

C = [pow(A[i+1], 2) * B[2*i] + B[n+i] for i in range(n)]

print(C)