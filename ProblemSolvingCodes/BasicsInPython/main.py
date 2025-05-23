a = 1
b = 2
c = a + b
print(c)

a = "1"
b = "2"
print(a + b)

a = "Hello"
b = "Welcome"
print(a + b)

a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)

a = ["Hi", "How are you"]
b = ["I'm fine"]
print(a + b)

a = ("Hello",)
b = ("Welcome",)
print(type(a))
print(type(b))
print(a + b)

a = (1,2)
b = (3,4)
print(a + b)

a = ("Hello",)
b = (1,)
print(a + b)

# In Python, dictionaries cannot be directly added using the + operator
a = {1: 2, 2: 4, 4: 5}
b = {3: 4, 5: 6}
a.update(b)
print(a)

a = {"Hi": 1, "Welcome": 2}
b = {"How are you": 3}
a.update(b)
print(a)

# Keys should be unique No duplicates are allowed
# keys are immutable (Tuple, str, int)
# values can have duplicates, Values can be of any type (List, str, int, dict)
a = {1: 2, 1: [1, 2, 3]}
b = {3: 7}
a.update(b)
print(a)

a = {"Hi": 1, "Hi": 2}
print(a)

# A set is an unordered collection of unique elements. It automatically removes any duplicates.
a = {1,2,5,4,1,5,2}
b = {"a","b","c","a","b"}
print(a)
print(b)

# declare empty list, str, set, dict
a = []
print(type(a))
a = ""
print(type(a))
a = {}
print(type(a))
empty_set = set()
print(type(empty_set))

