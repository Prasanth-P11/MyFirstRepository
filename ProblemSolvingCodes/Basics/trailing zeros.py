def count_trailing_zeros(number):
    # Convert the number to a string and strip any trailing zeros
    stripped_number = str(number).rstrip('0')
    # The count of trailing zeros is the difference in length between the original number and the stripped number
    trailing_zeros = len(str(number)) - len(stripped_number)
    return trailing_zeros


# Test cases
print(count_trailing_zeros(1230400))  # Output: 2
print(count_trailing_zeros(12345))  # Output: 0
print(count_trailing_zeros(1234000))  # Output: 3
print(count_trailing_zeros(12304))  # Output: 0
