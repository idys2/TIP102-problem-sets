'''
- input: binary tree
- output: list of lists
    - each list contains the elements in each level

- queue the 1st element (root)
- dequeue the 1st element, queue the children of that element
- when queue is empty after dequeuing, then we move to the next layer
'''
from collections import deque
class Puff():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def listify_design(design):
    queue = deque()
    child_queue = deque()
    result = []

    queue.appendleft(design)

    while queue:
        level = []
        while queue:
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                child_queue.append(node.left)
            if node.right:
                child_queue.append(node.right)
        
        result.append(level)
        queue = child_queue
        child_queue = deque()

    return result


"""
            Vanilla
           /       \\
      Chocolate   Strawberry
      /     \\
  Vanilla   Matcha  
"""
croquembouche = Puff("Vanilla", 
                    Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
                    Puff("Strawberry"))
print(listify_design(croquembouche))