def multiply(num1, num2):
    for i in range(num2+1):
        result = num1 * i
        print(num1,"x",i,"=",result)


if __name__ == "__main__":
    try:
        num1 = int(input("Enter the number:"))
        num2 = int(input("Enter the number:"))
        multiply(num1, num2)
    except ValueError:
        print("Invalid input!! please pass integer value")