def move_zeros_to_beginning(nums):
    zero_index = len(nums)-1
    for i in range(len(nums)-1, -1, -1):
        if nums[i] != 0:
            nums[zero_index], nums[i] = nums[i], nums[zero_index]
            zero_index -= 1
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
        move_zeros_to_beginning(nums)
    except ValueError as e:
        print(e)