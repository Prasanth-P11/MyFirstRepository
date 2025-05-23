def palindrome_of_a_num(num):
    rev = 0
    temp = num
    while num > 0:
        b = num % 10
        rev = rev * 10 + b
        num = num // 10
    if temp == rev:
        print(temp, "is a palindrome")
    else:
        print(temp, "is not a palindrome")


if __name__ == "__main__":
    try:
        num = int(input("Enter the number: "))
        if num < 0:
            raise ValueError("Input should not be negative integer")
        else:
            print("The given number is:", num)
            palindrome_of_a_num(num)
    except ValueError as e:
        print(e)