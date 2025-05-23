def addition_without_operator(x, y):
    while y != 0:
        carry = x & y
        x = x ^ y
        y = carry << 1
    return x


if __name__ == "__main__":
    try:
        x = int(input("Enter the number: "))
        y = int(input("Enter the number: "))
        out = addition_without_operator(x, y)
        print("The addition of two numbers are:", out)
    except ValueError:
        print("Invalid input!! please pass integer value")