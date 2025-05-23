def palindrome(a):
    try:
        temp = a
        rev = 0
        while a > 0:
            b = a % 10
            rev = rev * 10 + b
            a = a // 10
        if temp == rev:
            return "this is palindrome"
        else:
            return "Not a palindrome"
    except TypeError:
        return "Invalid input"
