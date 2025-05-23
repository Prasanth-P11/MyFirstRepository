def find_duplicates_in_a_list(arr):
    dict_list = {}
    arr1 = []
    for i in arr:
        dict_list[i] = dict_list.get(i, 0) + 1
    for key, value in dict_list.items():
        if value == 1:
            arr1.append(key)
    print("Returning the list after removing duplicates:", arr1)


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