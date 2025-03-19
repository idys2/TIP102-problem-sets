'''
- input: list of strings
- output: same list of strings but reversed
- 
- pointer at start and end
- swap strings at pointers
- increment start and decrement end until they meet in the middle
- 1. empty list -> empty list
'''

def reverse_list(lst):
    if len(lst) == 0:
        return lst

    start = 0
    end = len(lst) - 1

    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1

    return lst

lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
print(reverse_list(lst))
