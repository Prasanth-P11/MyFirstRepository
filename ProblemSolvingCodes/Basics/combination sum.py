def combination_sum(a, target):
    def backtrack(start, path, target):
        if target == 0:
            result.append(path)
            return
        if target < 0:
            return
        for i in range(start, len(a)):
            # Skip duplicates
            if i > start and a[i] == a[i - 1]:
                continue
            backtrack(i + 1, path + [a[i]], target - a[i])

    a.sort()  # Sort the list to handle duplicates and make combination generation easier
    result = []
    backtrack(0, [], target)
    return result

# Example usage
a = [10, 1, 2, 7, 6, 1, 5]
target = 8
output = combination_sum(a, target)
print(output)
