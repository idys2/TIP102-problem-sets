'''
- input: list of floors
- output: minimized number of skyscrapers

- rule: each floor must be placed on top of a floor with => height

ex 1:
1. 10
2. 5, 8
3. 3, 7
4. 2, 9

ex 2:
1. 7
2. 3, 7
3. 3, 5
4. 1, 6

ex 3:
1. 8
2. 6
3. 4, 7
4. 5
5. 3
6. 2

- loop through list, check if next number >= current num
    - if true, then continue
    - else create new skyscraper
'''

def build_skyscrapers(floors):
    if not floors:
        return 0
    
    n = len(floors)
    
    num_skyscrapers = 1

    for i in range(n-1):
        if floors[i+1] >= floors[i]:
            continue
        else:
            num_skyscrapers += 1

    return num_skyscrapers

print(build_skyscrapers([10, 5, 8, 3, 7, 2, 9])) 
print(build_skyscrapers([7, 3, 7, 3, 5, 1, 6]))  
print(build_skyscrapers([8, 6, 4, 7, 5, 3, 2]))