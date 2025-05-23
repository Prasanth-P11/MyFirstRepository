a = [1, "Hi", [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 2, 3: 4}]
print(type(a))
print(a)

a = (1, "Hi", [1, 2, 3], {1: 2, 3: 4}, {1, 2, 3}, (1, 2, 3))
print(type(a))
print(a)

a = {1, "Hi", (1, 2, 3)}
print(type(a))
print(a)

a = {1: (1, 2, 3), "Hi": {1, 2, 3}, (1, 2): {1: 2, 3: 4}}
print(type(a))
print(a)

import array as arr
a = arr.array('i', [1, 2, 3, 4]) # 'i' indicates integer type
print(type(a))
for i in a:
    print(i, end=" ")

arr = arr.array('f', [1.1, 2.2, 3.3])  # Float array
for i in arr:
    print(i, end=" ")

import numpy as np
arr = np.array(["apple", "banana", "cherry"])
print("\n")
print(arr)

import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr)
