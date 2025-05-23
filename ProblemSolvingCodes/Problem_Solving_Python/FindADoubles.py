def find_all_doubles(arr, target_sum):
    # Set to store the elements we've already seen
    seen = set()
    doubles = []

    # Iterate through the array
    for num in arr:
        complement = target_sum - num
        if complement in seen:
            doubles.append([complement, num])
        seen.add(num)

    return doubles


# Example input
arr = [1, 2, 3, 4, 5]
number = 7

# Finding doubles
doubles = find_all_doubles(arr, number)

# Returning the doubles list
print(doubles)
