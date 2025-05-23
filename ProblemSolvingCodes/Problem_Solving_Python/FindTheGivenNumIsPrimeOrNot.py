def find_given_number_is_prime_or_not(num):
    # Check if the number is less than or equal to 1
    if num < 2:
        return False
    # Check if the number is divisible by any integer from 2 to the square root of the number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    try:
        num = int(input("Enter the number: "))
        if num < 0:
            raise ValueError("Input should not be a negative integer")
        else:
            print("The given number is: ", num)
            if find_given_number_is_prime_or_not(num):
                print("The given number is a prime number")
            else:
                print("Thr given number is not a prime number")
    except ValueError as e:
        print(e)
        print("Invalid input!! User input should not be a string value or negative integer or whitespace character or "
              "empty string, please pass positive integer value")