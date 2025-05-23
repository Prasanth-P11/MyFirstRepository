def print_prime_number(num):
    print("Prime number btw", 2, "to", num, "are:")
    for i in range(2, num+1):
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
        if count == 2 and i % 10 == 7:
            print(i, end=" ")


if __name__ == "__main__":
    try:
        num = int(input("Enter the number: "))
        if num < 0:
            raise ValueError("Input should not be a negative integer")
        else:
            print("The given number is: ", num)
            print_prime_number(num)
    except ValueError as e:
        print(e)
        print("User input should not be a string value or negative integer")