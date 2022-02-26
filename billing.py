a=int(input("enter the value:"))
arr=[]
c=0
for i in range(a):
    b=int(input("enter the value:"))
    arr.append(b)
for j in arr:
    if(j>1000):
        d=(j-1000)//10
        c=c+d
print(c)
