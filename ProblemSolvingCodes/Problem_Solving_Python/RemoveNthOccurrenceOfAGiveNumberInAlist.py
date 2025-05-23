def remove_nth_occurrence(lst, num, n):
    count = 0  # to keep track of the occurrences
    for i in range(len(lst)):
        if lst[i] == num:
            count += 1
            if count == n:
                lst.pop(i)
                break
    return lst


# Example usage
lst = [1, 2, 3, 4, 2, 5, 2, 6]
num = int(input("Enter the number to remove: "))
n = int(input("Enter the nth occurrence to remove: "))

# Remove nth occurrence
result = remove_nth_occurrence(lst, num, n)
print("Updated list:", result)