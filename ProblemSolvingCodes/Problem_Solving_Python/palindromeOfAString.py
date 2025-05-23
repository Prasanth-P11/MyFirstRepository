def palindrome_of_string(string):
    a = "".join(char.lower() for char in string if char.isalpha())
    char_list = list(a)
    left = 0
    right = len(char_list) - 1
    while left < right:
        char_list[left], char_list[right] = char_list[right], char_list[left]
        left += 1
        right -= 1

    reversed_str = ''.join(char_list)
    if a == reversed_str:
        print(string, "is a palindrome")
    else:
        print(string, "is not a palindrome")


if __name__ == "__main__":
    try:
        string = input("Enter the string: ")
        if not string.strip():
            raise ValueError("Input string should not be empty or whitespace-only character")
        else:
            if all(c.isalpha() or c.isspace() or not c.isalnum() for c in string):
                print("The given string is:", string)
                palindrome_of_string(string)
            else:
                raise ValueError("String values should not contains numerical values")
    except ValueError as e:
        print(e)