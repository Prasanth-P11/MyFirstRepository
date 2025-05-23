str = "a1b5c4"
char = []
digit = []
out = ""
for i in str:
    if i.isalpha():
        char.append(i)
    else:
        digit.append(int(i))
for i in range(len(char)):
    for j in range(len(digit)):
        if i == j:
            mul = char[i] * digit[j]
            out += mul
print(out)