def addition(a, b):
    try:
        c = a + b
        return c
    except TypeError:
        return "Invalid input! Please enter values."

try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    out = addition(a, b)
    print(out)
except ValueError:
    print("Invalid input! Please enter numeric values.")
