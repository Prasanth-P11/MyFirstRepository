def move_zeros_to_end(nums):
    try:
        zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero_index] = nums[zero_index], nums[i]
                zero_index += 1
        return nums
    except TypeError:
        return "invalid input"
