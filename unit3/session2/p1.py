'''
- input: list of ints
- output: 

precon:
- requires a queue
- queue sort in place
- find minimum

[3, 5, 2, 1, 4]
[3, 5, 2, 4, 1]
[3, 5, 4, 1, 2]
[5, 4, 1, 2, 3]
[5, 1, 2, 3, 4]
[1, 2, 3, 4, 5]
'''

from collections import deque

def find_min():
    pass

def blueprint_approval(blueprints: list[int]):
    #return sorted(blueprints)
    min_index = -1
    min_val = int('inf')

    queue = deque(blueprints)

    for i in range(len(blueprints)):
        pass


print(blueprint_approval([3, 5, 2, 1, 4])) 
print(blueprint_approval([7, 4, 6, 2, 5])) 