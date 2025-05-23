def retain_first_occurrence(string):
    seen = set()
    result = []
    for char in string:
        if char.isspace() or not char.isalnum():
            result.append(char)
        elif char.upper() not in seen and char.lower() not in seen:
            result.append(char)
            seen.add(char)
    print("The string after removing occurrence of a repeated char:", "".join(result))


if __name__ == "__main__":
    try:
        string = input("Enter the string:")
        if not string.strip():
            raise ValueError("Input string should not be empty or whitespace-only character")
        else:
            if all(c.isalpha() or c.isspace() or not c.isalnum() for c in string):
                print("The given string is:", string)
                retain_first_occurrence(string)
            else:
                raise ValueError("String values should not contains numerical values")
    except ValueError as e:
        print(e)