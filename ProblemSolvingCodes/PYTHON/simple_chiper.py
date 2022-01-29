a = input("enter the value:")
b = []
c = []
for i in a:
    b.append(ord(i))
for j in range(len(b)):
    if(j%2 == 0):
        b[j] += 2
    if(j%2 != 0):
        b[j] -= 2
for k in b:
    c.append(chr(k))
print("".join(c))


