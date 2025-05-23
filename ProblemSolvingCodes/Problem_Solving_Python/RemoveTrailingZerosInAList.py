def remove_trailing_zeros(arr):
    # Start from the end and move backwards
    i = len(arr) - 1
    # Move the index i backwards until a non-zero element is found
    while i >= 0 and arr[i] == 0:
        i -= 1
    # Return the array up to the last non-zero element
    return arr[:i + 1]


# Example usage
arr = [0, 5, 0, 0, 3, 1, 15, 0, 12, 0, 0, 0]
result = remove_trailing_zeros(arr)
print("Output:", result)
