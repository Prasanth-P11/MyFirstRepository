def print_mid_word(string):
    length = len(string)
    mid = length // 2
    if length % 2 == 0:
        return string[mid-1:mid+1]
    else:
        return string[mid]


if __name__ == "__main__":
    try:
        string = input("Enter the string: ")
        if not string.strip():
            raise ValueError("Input should not be empty or white-space character")
        else:
            if all(c.isalpha() or c.isdigit() or c.isspace() for c in string):
                print("The given string is:", string)
                out = print_mid_word(string)
                print("The middle word of the string is:", out)
            else:
                raise ValueError("String values should not contains special characters")
    except ValueError as e:
        print(e)