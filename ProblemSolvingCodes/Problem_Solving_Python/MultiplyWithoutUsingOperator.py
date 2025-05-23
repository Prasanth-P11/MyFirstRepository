def multiply_two_num_without_operator(a, b):
    num1 = abs(a)
    num2 = abs(b)
    result = 0
    for i in range(num2):
        result += num1
    if a < 0 and b < 0:
        result = result
    elif a < 0 and b > 0:
        result = -result
    elif a > 0 and b < 0:
        result = -result
    else:
        result = result
    return result


if __name__ == "__main__":
    try:
        a = int(input("Enter the num: "))
        b = int(input("Enter the num: "))
        out = multiply_two_num_without_operator(a, b)
        print("The multiplication of two numbers are:", out)
    except ValueError:
        print("Invalid input!! Please pass only numeric values")