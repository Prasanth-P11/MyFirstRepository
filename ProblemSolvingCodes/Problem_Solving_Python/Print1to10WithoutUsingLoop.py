def print_number(n):
    if n > 10:
        return
    print(n)
    print_number(n + 1)


def print_numbers(n, current=1):
    if current <= n:
        print(current)
        print_numbers(n, current+1)


if __name__ == "__main__":
    try:
        n = int(input("Enter the number: "))
        if n < 0:
            raise ValueError("Input should not be a negative integer")
        else:
            print("The given number is: ", n)
            print_number(n)
            print_numbers(n)
    except ValueError as e:
        print(e)
        print("User input should not be a string value or negative integer")