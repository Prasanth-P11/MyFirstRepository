# LIST
# remove, pop, insert, index, copy is applicable
# get, add is not applicable

# remove
my_list = [1, 2, 3, 4, 3]  # remove: Removes the first occurrence of a specified value.
my_list.remove(3)
print(my_list)

# pop
my_list = [1, 2, 3, 4, 3]
popped_element = my_list.pop()
print(popped_element)
print(my_list)

my_list = [1, 2, 3, 4, 3]
popped_element = my_list.pop(3)
print(popped_element)
print(my_list)

my_list = [1, 2, 3, 4, 3]
index_value = my_list.index(3)
print(index_value)

my_list = [1, 2, 3, 4, 3]
my_list.insert(1, 0)
print(my_list)

my_list = [1, 2, 3, 4, 3]
copy_my_list = my_list.copy()
print(copy_my_list)

# DICTIONARY
# remove, pop, add , get

# remove
# remove: Not directly applicable, but you can use del to remove a key.
my_dict = {'a': 1, 'b': 2, 'c': 3}
del my_dict['b']
print(my_dict)

# pop
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict.pop('c')
print(my_dict)

# get
my_dict = {'a': 1, 'b': 2, 'c': 3}
value = my_dict.get('b')
print(value)

# add
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict['d'] = 4
print(my_dict)

# SET
# remove add pop get
# remove, pop and add applicable
# get not applicable

# remove
my_set = {1, 3, 4, 5}
my_set.remove(3)
print(my_set)

# pop
my_set = {5, 6, 7, 8}
popped_element = my_set.pop()  # Removes and returns an arbitrary element
print(popped_element)
print(my_set)

# add
my_set = {5, 6, 7, 8}
my_set.add(9)
print(my_set)