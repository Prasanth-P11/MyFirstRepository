def factorial(num):
    fact = 1
    while num > 1:
        fact = fact * num
        num -= 1
    print("The factorial of the given number is: ", fact)


if __name__ == "__main__":
    try:
        num = int(input("Enter the number: "))
        factorial(num)
    except ValueError:
        print("Invalid input!! please pass integer value")