def count_trailing_zeros(number):
    # Convert the number to a string and strip any trailing zeros
    stripped_number = str(number).rstrip('0')
    # The count of trailing zeros is the difference in length between the original number and the stripped number
    trailing_zeros = len(str(number)) - len(stripped_number)
    return trailing_zeros


if __name__ == "__main__":
    try:
        number = int(input("Enter the number:"))
        out = count_trailing_zeros(number)
        print("The no of trailing zeros in the given number is:", out)
    except ValueError:
        print("Invalid input!! please pass integer value")
