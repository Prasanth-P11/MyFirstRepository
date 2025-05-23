def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    try:
        num1 = int(input("Enter the number:"))
        num2 = int(input("Enter the number:"))
        out = gcd(num1, num2)
        print("The GCD of the two number is: ", out)
    except ValueError:
        print("Invalid input!! please pass integer value")
