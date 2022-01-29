N = 4
A=[]
B=[]
for i in range(N):
    a = []
    for j in range(N):
        a.append(int(input("enter the value")))
    A.append(a)
print("Matrix")
for k in range(N):
    for l in range(N):
        print(A[k][l], end=" ")
    print()
for i in range(N):
    b = []
    for j in range(N):
        b.append(0)
    B.append(b)
print("transpose matrix")
for i in range(N):
    for j in range(N):
        B[i][j]=A[j][i]
for i in range(N):
    for j in range(N):
        print(B[i][j], end=" ")
    print()





