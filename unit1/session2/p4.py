'''
- input: int array nums
- output: int array with all even numbers first
- pop even numbers to a new array, combine the arrays
- empty array -> empty array
'''

def sort_by_parity(nums):
    even_nums = []

    if len(nums) == 0:
        return nums
    
    index = 0
    while index < len(nums):
        if nums[index] % 2 == 0:
            even_nums.append(nums.pop(index))
        else:
            index += 1

    return even_nums + nums

nums = [3, 1, 2, 4]
print(sort_by_parity(nums))

nums = [0]
print(sort_by_parity(nums))

nums = [
    3, 7, 1, 4, 9, 0, 6, 8, 2, 5, 1, 3, 7, 0, 4, 9, 6, 2, 8, 5,
    4, 2, 7, 9, 1, 3, 6, 8, 0, 5, 7, 1, 8, 6, 2, 4, 9, 0, 3, 5,
    2, 9, 0, 7, 6, 3, 8, 5, 1, 4, 9, 8, 6, 2, 0, 7, 3, 5, 1, 4,
    7, 0, 3, 9, 5, 8, 2, 6, 4, 1, 8, 5, 7, 2, 0, 3, 9, 4, 6, 1,
    5, 7, 3, 0, 8, 9, 2, 6, 4, 1, 9, 6, 4, 2, 0, 7, 8, 5, 3, 1
]
print(sort_by_parity(nums))
