def palindrome(string):
    if not (string.isalpha()):
        print("Invalid input, Please pass string a input")
        return
    try:
        rev = ""
        for i in string:
            rev = i+rev
        if rev == string:
            print("Palindrom")
        else:
            print("Not a palindrom")
    except TypeError:
        print("invalid input, Please pass string a input")


if __name__ == "__main__":
    string = input("Enter the string:")
    palindrome(string)