'''
- identify center node: node that is present in every sublist
- keep a set of possible center nodes
- return the single node in the set
'''

def find_center(terminals):
    return list(set(terminals[0]) & set(terminals[1]))[0]

terminals1 = [[1,2],[2,3],[4,2]]
terminals2 = [[1,2],[5,1],[1,3],[1,4]]

print(find_center(terminals1))
print(find_center(terminals2))