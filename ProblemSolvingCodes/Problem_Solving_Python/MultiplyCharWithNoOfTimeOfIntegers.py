def multiply_char(string):
    char = []
    digit = []
    out = ""
    for i in string:
        if i.isalpha():
            char.append(i)
        else:
            digit.append(int(i))
    for i in range(len(char)):
        for j in range(len(digit)):
            if i == j:
                mul = char[i] * digit[j]
                out += mul
    print("output:", out)


if __name__ == "__main__":
    try:
        string = input("Enter the string: ")
        if not string.strip():
            raise ValueError("Input should not be empty or white-space character")
        else:
            if all(c.isalpha() or c.isdigit() for c in string):
                print("The given string is:", string)
                multiply_char(string)
            else:
                raise ValueError("String values should not contains special characters")
    except ValueError as e:
        print(e)