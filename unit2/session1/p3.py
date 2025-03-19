'''
inputs
- souvenirs: list
- threshold: 

- use counter

edge cases
- assume lowercase, order doesn't matter
- threshold = 0 -> return []
- souvenirs empty -> return []
'''
from collections import Counter

def declutter(souvenirs, threshold):
    result = []

    if threshold == 0 or not souvenirs:
        return []
    
    hm = Counter(souvenirs)

    '''
    for k, v in hm.items():
        if v < threshold:
            for _ in range(v):
                result.append(k)
    '''

    for item in souvenirs:
        if hm[item] < threshold:
            result.append(item)

    return result

souvenirs1 = ["coin", "alien egg", "coin", "coin", "map", "map", "statue"]
threshold1 = 3
print(declutter(souvenirs1, threshold1))

souvenirs2 = ["postcard", "postcard", "postcard", "sword"]
threshold2 = 2
print(declutter(souvenirs2, threshold2))