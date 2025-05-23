def factorial(n):
    """Calculate the factorial of a number using recursion."""
    if n == 0 or n == 1:  # Base case: 0! = 1! = 1
        return 1
    return n * factorial(n - 1)  # Recursive case


if __name__ == "__main__":
    try:
        num = int(input("Enter a number to calculate its factorial: "))
        if num < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        result = factorial(num)
        print("Factorial of given number is:", result)
    except ValueError as e:
        print(e)
