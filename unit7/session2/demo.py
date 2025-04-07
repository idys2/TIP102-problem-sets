def binary_search(nums: list[int], target: int):
    if not nums:
        return -1

    low, high = 0, len(nums)-1

    while low <= high:
        mid = (low + high) // 2

        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1

print(binary_search([1,3,5,7,9,11], 5))