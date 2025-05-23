def count_repeated_char_in_string(string):
    string1 = "".join(char.lower() for char in string if char.isalpha())
    dict = {}
    duplicates = []
    for i in string1:
        dict[i] = dict.get(i, 0) + 1
    for num, count in dict.items():
        if count > 1:
            duplicates.append(num)
            print("Count of", num, "is", count)
    print("Duplicated values are:", duplicates)


if __name__ == "__main__":
    try:
        string = input("Enter the string:")
        if not string.strip():
            raise ValueError("Input string should not be empty or whitespace-only character")
        else:
            if all(c.isalpha() or c.isspace() or not c.isalnum() for c in string):
                print("The given string is:", string)
                count_repeated_char_in_string(string)
            else:
                raise ValueError("String values should not contains numerical values")
    except ValueError as e:
        print(e)