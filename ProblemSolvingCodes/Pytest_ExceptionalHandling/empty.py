def palindrome(a):
    try:
        temp = a
        rev=0
        while(a>0):
            b=a%10
            rev=rev*10+b
            a=a//10
        if(temp==rev):
            print("this is palindrome")
        else:
            print("Not a palindrome")
    except TypeError:
        print("Invalid input")

try:
    a = int(input("enter the value:"))
    palindrome(a)
except ValueError:
    print("invalid input")