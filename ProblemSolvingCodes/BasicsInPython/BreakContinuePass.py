# Break
for num in range(5):
    if num == 3:
        break  # Exit the loop when num is 3
    print(num)

# Output:
# 0
# 1
# 2

# Continue
for num in range(5):
    if num == 3:
        continue  # Skip the iteration when num is 3
    print(num)

# Output:
# 0
# 1
# 2
# 4

# Pass
for num in range(5):
    if num == 3:
        pass  # Do nothing when num is 3
    print(num)

# Output:
# 0
# 1
# 2
# 3
# 4

