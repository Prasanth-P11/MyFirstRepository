def odd_or_even(num):
    if num % 2 == 0:
        print(num, "is a even number")
    else:
        print(num, "is a odd number")


if __name__ == "__main__":
    try:
        num = int(input("Enter the number:"))
        odd_or_even(num)
    except ValueError:
        print("Invalid input!! please pass integer value")
