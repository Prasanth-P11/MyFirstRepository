# Method 1 using set
def remove_repeated_chars_set(string):
    string1 = string.lower()
    seen_chars = set()
    duplicates = set()
    result = []
    for char in string1:
        if char.isalpha():
            if char in seen_chars:
                duplicates.add(char)
            else:
                seen_chars.add(char)
    for char in string:
        if char.isspace() or not char.isalnum():
            result.append(char)
        elif char.lower() not in duplicates:
            result.append(char)

    print("The string after removing repeated characters:", "".join(result))


# Method 2 using dictionary
def remove_repeated_chars_dict(string):
    string1 = string.lower()
    char_count = {}
    for char in string1:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    result = []
    for char in string:
        if char.isspace() or not char.isalnum():
            result.append(char)
        elif char_count[char.lower()] == 1:
            result.append(char)
    print("The string after removing repeated char:", "".join(result))


def remove_repeated_chars_dict1(string):
    string1 = string.lower()
    dict_char = {}
    string2 = []
    for i in string1:
        dict_char[i] = dict_char.get(i, 0) + 1
    for i in string:
        if i.isspace() or not i.isalnum():
            string2.append(i)
        elif dict_char[i.lower()] == 1:
            string2.append(i)
    print("The string after removing repeated char:", "".join(string2))


if __name__ == "__main__":
    try:
        string = input("Enter the string:")
        if not string.strip():
            raise ValueError("Input string should not be empty or whitespace-only character")
        else:
            if all(c.isalpha() or c.isspace() or not c.isalnum() for c in string):
                print("The given string is:", string)
                remove_repeated_chars_dict(string)
                remove_repeated_chars_dict1(string)
                remove_repeated_chars_set(string)
            else:
                raise ValueError("String values should not contains numerical values")
    except ValueError as e:
        print(e)