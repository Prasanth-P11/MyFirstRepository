# Method 1 using sorted() function
def anagram_of_string(string1, string2):
    a = "".join(char.lower() for char in string1 if char.isalpha())
    b = "".join(char.lower() for char in string2 if char.isalpha())
    if sorted(a) == sorted(b):
        print("The given two strings are Anagram")
    else:
        print("The given two string are not Anagram")


# Method 2 using dictionary
def anagram_of_string_dict(string1, string2):
    a = "".join(char.lower() for char in string1 if char.isalpha())
    b = "".join(char.lower() for char in string2 if char.isalpha())
    char_count1 = {}
    char_count2 = {}
    for char in a:
        char_count1[char] = char_count1.get(char, 0) + 1
    for char in b:
        char_count2[char] = char_count2.get(char, 0) + 1
    if char_count1 == char_count2:
        print("The given two strings are Anagram")
    else:
        print("The given two string are not Anagram")


if __name__ == "__main__":
    try:
        string1 = input("Enter the string: ")
        string2 = input("Enter the string: ")
        if not string1.strip() and string2.strip():
            raise ValueError("Input cannot be an empty or whitespace-only string.")
        if all(c.isalpha() or c.isspace() or not c.isalnum() for c in string1) and all(c.isalpha() or c.isspace() or not c.isalnum() for c in string2):
            print("String 1:", string1)
            print("string 2:", string2)
            anagram_of_string(string1, string2)
            anagram_of_string_dict(string1, string2)
        else:
            raise ValueError("Invalid input!! Please pass only alphabetic characters.")
    except ValueError as e:
        print(e)