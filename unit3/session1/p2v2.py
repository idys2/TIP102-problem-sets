'''
- 
'''
def pair_up_animals(discomfort_levels):
    discomfort_levels.sort()
    n = len(discomfort_levels)
    t = []

    for i in range(n//2):
        t.append(discomfort_levels[i] + discomfort_levels[n-i-1])

    return max(t)


print(pair_up_animals([3,5,2,3]))       # 7 = 2+5
print(pair_up_animals([3,5,4,2,4,6]))   # 8 = 2+6
print(pair_up_animals([1,4,4,5]))       # 8 = 4+4
