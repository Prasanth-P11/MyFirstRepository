def count_senior_citizens(details):
    senior_count = 0

    for info in details:
        # Extract the age from the 12th and 13th characters (index 11 and 12)
        age = int(info[11:13])

        # Check if the age is 60 or above
        if age >= 60:
            senior_count += 1

    return senior_count


# Example usage
details = ["7868190130M7522", "5303914400F9211", "9273338290F4010"]
print(count_senior_citizens(details))  # Output: 2