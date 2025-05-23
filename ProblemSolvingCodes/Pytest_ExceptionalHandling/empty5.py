def move_zeros(nums):
    if not all(isinstance(x, str) for x in nums):
        print("All the values must be string")
        return
    zero_index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero_index] = nums[zero_index], nums[i]
            zero_index += 1
    print(nums)


nums = [1,2]
move_zeros(nums)
