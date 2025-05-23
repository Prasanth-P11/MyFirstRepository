def find_all_triplets(arr, target_sum):
    # Sort the array
    arr.sort()

    # List to store all found triplets
    triplets = []

    # Iterate through the array
    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            # If the sum matches the target sum
            if current_sum == target_sum:
                triplets.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
            elif current_sum < target_sum:
                left += 1
            else:
                right -= 1

    return triplets


# Example input
arr = [5,7,1,4,9,2,6,0,1]
number = 20

# Finding triplets
triplets = find_all_triplets(arr, number)

# Returning the triplets list
print(triplets)
