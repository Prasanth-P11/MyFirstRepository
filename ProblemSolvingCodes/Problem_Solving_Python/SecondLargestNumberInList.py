def second_largest_num(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    print("The second largest number in a given list is:", arr[1])


if __name__ == "__main__":
    try:
        n = int(input("Enter the number:"))
        if n < 0:
            raise ValueError("Invalid input!!, Values should not be a negative integer")
        arr = []
        for i in range(n):
            try:
                arr.append(int(input()))
            except ValueError:
                print("Invalid input!!, Value should be numeric")
                exit()
        print("List of integer from user: ", arr)
        second_largest_num(arr)
    except ValueError as e:
        print(e)
