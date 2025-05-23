def sort_people(names, heights):
    # Pair each name with its corresponding height
    name_height_pairs = zip(names, heights)

    # Sort the pairs by height in descending order
    sorted_pairs = sorted(name_height_pairs, key=lambda x: x[1], reverse=True)

    # Extract and return the names from the sorted pairs
    sorted_names = [name for name, height in sorted_pairs]

    return sorted_names


# Example usage
names = ["Mary", "John", "Emma"]
heights = [180, 165, 170]
print(sort_people(names, heights))  # Output: ['Mary', 'Emma', 'John']
