def is_binary_palindrome(num):
    # Convert the number to binary (excluding the '0b' prefix)
    binary_rep = bin(num)[2:]
    print(binary_rep)
    # Check if the binary string is the same forwards and backwards
    return binary_rep == binary_rep[::-1]


# Example usage
num = int(input("Enter a number: "))

if is_binary_palindrome(num):
    print(f"The binary representation of {num} is a palindrome.")
else:
    print(f"The binary representation of {num} is not a palindrome.")
