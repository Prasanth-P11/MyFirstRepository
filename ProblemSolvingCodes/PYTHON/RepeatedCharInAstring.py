a="beautiful place is goa"
b=[]
for i in range(len(a)):
    count=0
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            count+=1
    if(count==1):
        if(a[i]!=" "):
           b.append(a[i])
print(b)
for k in b:
    a=a.replace(k,"")
print(a)
