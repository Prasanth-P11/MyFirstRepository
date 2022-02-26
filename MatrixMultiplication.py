N = 2
A=[]
B=[]
C=[]
for i in range(N):
    a = []
    for j in range(N):
        a.append(int(input("enter the value")))
    A.append(a)
print("Matrix1")
for k in range(N):
    for l in range(N):
        print(A[k][l], end=" ")
    print()
for i in range(N):
    b = []
    for j in range(N):
        b.append(int(input("enter the value")))
    B.append(b)
print("Matrix2")
for k in range(N):
    for l in range(N):
        print(B[k][l], end=" ")
    print()
for i in range(N):
    d = []
    for j in range(N):
        d.append(0)
    C.append(d)
print("Matrix addition")
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            C[i][j]+=A[i][k]*B[k][j]
for i in range(N):
    for j in range(N):
        print(C[i][j], end=" ")
    print()
