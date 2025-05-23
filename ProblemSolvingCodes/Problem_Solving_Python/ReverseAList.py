def reverse_a_list(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


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
        out = reverse_a_list(arr)
        print("The reversed list is: ", out)
    except ValueError as e:
        print(e)