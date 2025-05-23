a = [1, 3, 1, 5, 2, 4, 7, 3, 5] # [1, 3, 5, 2, 4, 7]
b = set()
c = []
for i in a:
    if i not in b:
        c.append(i)
        b.add(i)
print("Returning the list after removing duplicates:",c)

# Using Nested Loops O(n^3)
a = [1, 3, 1, 5, 2, 4, 7, 3, 5]
b = []
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] == a[j] and a[i] not in b:
            b.append(a[i])
print("Returning the duplicated values:",b)

# Using Set for Duplicates O(n)
a = [1, 3, 1, 5, 2, 4, 7, 3, 5]
b = set()
c = []
for i in a:
    if i not in b:
        b.add(i)
    else:
        c.append(i)
print("Returning the duplicated values:",c)
