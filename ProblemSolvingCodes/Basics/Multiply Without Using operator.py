def multiply(a, b):
    num1 = abs(a)
    num2 = abs(b)
    result = 0
    for i in range(num2):
        result += num1
    if a < 0 and b < 0:
        result = result
    elif a < 0 and b > 0:
        result = -result
    elif a > 0 and b < 0:
        result = -result
    else:
        result = result
    return result

if __name__ == "__main__":
    a = int(input("Enter the number:"))
    b = int(input("Enter the number:"))
    out = multiply(a, b)
    print("Multiplication of", a, "and", b, "is:", out)