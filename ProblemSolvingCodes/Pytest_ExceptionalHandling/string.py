def string_concat(str1, str2):
    # Check if both inputs are strings
    if not (str1.isalpha() and str2.isalpha()):
        return "Invalid input!! Please provide string values."

    try:
        str3 = str1 + str2
        return str3
    except TypeError:
        return "Invalid input!! Please provide string values."


# Input from user
str1 = input("Enter the first value: ")
str2 = input("Enter the second value: ")

# Concatenate strings
out = string_concat(str1, str2)
print(out)
