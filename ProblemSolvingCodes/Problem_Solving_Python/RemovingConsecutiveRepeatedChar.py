def remove_consecutive_repeated_char(string):
    b = []
    c = " "
    for i in string:
        if c != i:
            b.append(i)
            c = i
    print("The string after removing consecutive char:", "".join(b))


if __name__ == "__main__":
    try:
        string = input("Enter the string:")
        if not string.strip():
            raise ValueError("Input string should not be empty or whitespace-only character")
        else:
            if all(c.isalpha() or c.isspace() or not c.isalnum() for c in string):
                print("The given string is:", string)
                remove_consecutive_repeated_char(string)
            else:
                raise ValueError("String values should not contains numerical values")
    except ValueError as e:
        print(e)