def count_duplicate_num_in_list(arr):
    dict = {}
    duplicates = []
    for i in arr:
        dict[i] = dict.get(i, 0) + 1
    for num, count in dict.items():
        if count > 1:
            duplicates.append(num)
            print("Count of", num, "is", count)
    print("Duplicated values are:", duplicates)


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
        count_duplicate_num_in_list(arr)
    except ValueError as e:
        print(e)
