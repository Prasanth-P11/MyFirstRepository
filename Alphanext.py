a="All The Best"
b=""
for i in a:
    if i.islower():
        b+=chr((ord(i)-97+1)%26+97)
    elif i.isupper():
        b+=chr((ord(i)-65+1)%26+65)
    else:
        b+=i
print(b)
