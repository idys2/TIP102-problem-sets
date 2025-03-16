def non_decreasing(nums):
    flag = False
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            if flag:
                return False
            flag = True
    return True

nums = [4, 2, 3]
non_decreasing(nums)

nums = [4, 2, 1]
non_decreasing(nums)
