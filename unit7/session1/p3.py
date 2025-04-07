'''
input: list of integers, number of workers
output: 
'''

def can_split_coffee(coffee, n):
    if len(coffee) == 0:
        return True
    
    elif coffee.pop() % n != 0:
        return False
    
    else:
        return can_split_coffee(coffee, n)

print(can_split_coffee([4, 4, 8], 2))
print(can_split_coffee([5, 10, 15], 4))