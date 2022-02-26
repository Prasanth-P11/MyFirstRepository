a=[2,4,6]
b=[1,5]
d=[]
for i in a:
    d.append(i)
for j in b:
    d.append(j)
for k in range(len(d)):
    for l in range(k+1,len(d)):
        if d[k]>d[l]:
            temp=d[k]
            d[k]=d[l]
            d[l]=temp
print(d)
