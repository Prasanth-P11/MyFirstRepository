def addition_without_operator(x, y):
    while y != 0:
        carry = x & y
        x = x ^ y
        y = carry << 1
    return x

if __name__ == "__main__":
    x = int(input("Enter the num:"))
    y = int(input("Enter the num:"))
    result = addition_without_operator(x, y)
    print("Addition of", x, "and", y, "is:",result)