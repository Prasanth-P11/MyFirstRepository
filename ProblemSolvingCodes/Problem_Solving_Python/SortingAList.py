# Method 1 o(n log n)
# using a build in function
def sort_a_list(arr):
    arr.sort()
    return arr


# Method 2
# Bubble sort o(n^2)
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
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
        out = sort_a_list(arr)
        output = bubble_sort(arr)
        print("The sorted list is: ", out)
        print("The sorted list is: ", output)
    except ValueError as e:
        print(e)
