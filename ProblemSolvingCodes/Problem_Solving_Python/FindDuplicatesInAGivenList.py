def find_duplicates_in_a_list(arr):
    b = set()
    c = []
    for i in arr:
        if i not in b:
            b.add(i)
        else:
            c.append(i)
    print("Returning the duplicated values:", c)


if __name__ == "__main__":
    try:
        n = int(input("Enter the num: "))
        if n < 0:
            raise ValueError("Please enter a non-negative integer for the number of elements.")
        arr = []
        for i in range(n):
            try:
                arr.append(int(input()))
            except ValueError:
                print("Invalid input!! please pass integer value")
                exit()
        find_duplicates_in_a_list(arr)
    except ValueError as e:
        print(e)