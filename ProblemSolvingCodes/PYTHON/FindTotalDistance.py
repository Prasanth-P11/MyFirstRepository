a=int(input("enter the value:"))
arr=[]
c=0
for i in range(a):
    b=int(input("enter the value:"))
    arr.append(b)
for j in range(len(arr)-1):
    d=abs(arr[j]-arr[j+1])
    c=c+d
print(c)

