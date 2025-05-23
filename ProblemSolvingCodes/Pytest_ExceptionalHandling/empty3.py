def move_zeros(nums):
    zero_index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero_index] = nums[zero_index], nums[i]
            zero_index += 1
    print(nums)

try:
    a = int(input("Enter:"))
    nums = []
    for i in range(a):
        try:
            nums.append(int(input()))
        except ValueError:
            print("Invalid input, expecting int")
            break
    if len(nums)==a:
        move_zeros(nums)
except ValueError:
    print("Invalid input")
