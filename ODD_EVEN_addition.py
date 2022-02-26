a=int(input("enter the value:"))
arr=[]
c=0
d=0
for i in range(a):
    b=int(input("enter:"))
    arr.append(b)
for j in arr:
    if(j%2==0):
        c=c+j
    if(j%2!=0):
        d=d+j
k=d-c
print(k)

