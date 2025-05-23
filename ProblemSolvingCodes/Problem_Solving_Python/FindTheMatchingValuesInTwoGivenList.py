def find_matching_values_in_two_given_list(arr1, arr2):
    h = set(arr2)
    matching_values = []
    for i in arr1:
        if i in h:
            matching_values.append(i)
    print("Matching values in the two given list are:", list(set(matching_values)))


if __name__ == "__main__":
    try:
        n = int(input("Enter the number:"))
        if n < 0:
            raise ValueError("Invalid input!!, Values should not be a negative integer")
        arr1 = []
        for i in range(n):
            try:
                arr1.append(int(input()))
            except ValueError:
                print("Invalid input!!, Value should be numeric")
                exit()
        arr2 = []
        for i in range(n):
            try:
                arr2.append(int(input()))
            except ValueError:
                print("Invalid input!!, Value should be numeric")
                exit()
        print("1. List of integer from user: ", arr1)
        print("2. List of integer from user: ", arr2)
        find_matching_values_in_two_given_list(arr1, arr2)
    except ValueError as e:
        print(e)