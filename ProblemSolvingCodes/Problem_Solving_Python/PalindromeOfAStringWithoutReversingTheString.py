def palindrome_of_string(string):
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    try:
        string = input("Enter the string: ")
        if not string.strip():
            raise ValueError("Input string should not be empty or whitespace-only character")
        else:
            if all(c.isalpha() or c.isspace() or not c.isalnum() for c in string):
                print("The given string is:", string)
                if palindrome_of_string(string):
                    print(f"'{string}' is a palindrome.")
                else:
                    print(f"'{string}' is not a palindrome.")
            else:
                raise ValueError("String values should not contains numerical values")
    except ValueError as e:
        print(e)