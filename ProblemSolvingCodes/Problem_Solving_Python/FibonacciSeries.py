def fibonacci_series(num):
    n1, n2 = 0, 1
    print("Fibonacci Series:", n1, n2, end=" ")
    for i in range(2, num):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(n3, end=" ")


if __name__ == "__main__":
    try:
        num = int(input("Enter the number: "))
        if num < 0:
            raise ValueError("Input should not be a negative integer")
        else:
            print("The given number is: ", num)
            fibonacci_series(num)
    except ValueError as e:
        print(e)
        print("User input should not be a string value or negative integer")