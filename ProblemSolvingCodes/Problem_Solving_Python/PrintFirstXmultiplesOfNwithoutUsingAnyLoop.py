def print_multiples(n, x, current=1):
    if current <= x:
        print(n * current)
        print_multiples(n, x, current + 1)


# Get user input
n = int(input("Enter the number (N): "))
x = int(input("Enter how many multiples to print (X): "))

# Call the recursive function
print_multiples(n, x)
