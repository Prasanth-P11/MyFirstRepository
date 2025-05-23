# APPEND EXTEND

# LIST
# APPEND
my_list = [1, 2, 3]
add = 4
my_list.append(add)
print(my_list)

my_list = [1, 2, 3]
add = [4, 5, 6]
my_list.append(add)
print(my_list)

# EXTEND
my_list = [1, 2, 3]
add = [4, 5, 6]
my_list.extend(add)
print(my_list)

# Common Type Conversions:
# int
a = 123
b = str(a)
print(b)
print(type(b))

# str
str1 = "123"  # only applicable if the str is numeric
a = int(str1)
print(a)
print(type(a))

str1 = "Hellow"
a = list(str1)
print(a)

str1 = "Hellow"
a = tuple(str1)
print(a)

str1 = "Hellow"
a = set(str1)
print(a)

# List
a = [1, 2, 3, 4]
b = tuple(a)
print(b)

a = [1, 2, 3, 4]
b = set(a)
print(b)

a = ["a", "b", "c", "d"]
b = "".join(a)
print(b)

# dictionary
my_dict = {1: 5, 2: 6, 3: 7}
a = list(my_dict)
print(a)

my_dict = {1: "a", 2: "b", 3: "c"}
a = set(my_dict)
print(a)

my_dict = {1: "a", 2: "b", 3: "c"}
a = tuple(my_dict)
print(a)

# Tuple
a = (1, 2, 3, 4)
b = list(a)
print(b)

a = (1, 2, 3, 4)
b = set(a)
print(b)

a = ("a", "b")
b = "".join(a)
print(b)

# Set
a = {"a", "b", "c", "a"}
b = list(a)
print(b)

a = {"a", "b", "c"}
b = tuple(a)
print(b)

a = {"a", "b", "c"}  # sets are unordered collections of unique elements
b = "".join(a)
print(b)
