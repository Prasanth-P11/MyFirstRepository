# A lambda function in Python is a small, anonymous function defined using the lambda keyword.
# syntax: lambda arguments: expression
# The map() function in Python is a built-in function that allows you to apply a given function to all items in an
# iterable (like a list or tuple) and returns an iterator that produces the results.
# Lambda function to add two numbers
add = lambda a, b: a + b
result = add(5, 3)
print(result)

# Lambda function to square each element in the list
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)

# Lambda function to filter even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# Convert all characters in a string to uppercase
words = ['hello', 'world', 'python']
uppercase_words = list(map(lambda x: x.upper(), words))
print(uppercase_words)


