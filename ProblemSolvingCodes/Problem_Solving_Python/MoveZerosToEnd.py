def move_zeros_to_end(nums):
    zero_index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero_index] = nums[zero_index], nums[i]
            zero_index += 1
    print(nums)


if __name__ == "__main__":
    try:
        n = int(input("Enter the num: "))
        if n < 0:
            raise ValueError("Please enter a non-negative integer for the number of elements.")
        nums = []
        for i in range(n):
            try:
                nums.append(int(input()))
            except ValueError:
                print("Invalid input!! please pass integer value")
                exit()
        move_zeros_to_end(nums)
    except ValueError as e:
        print(e)