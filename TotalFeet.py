a=int(input("enter the value:"))
arr=[]
c=0
for i in range(a):
    b=int(input("enter the value:"))
    arr.append(b)
for j in arr:
    d=j//12
    c=c+d
print(c)
