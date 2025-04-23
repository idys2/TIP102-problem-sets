from common import build_tree

class TreeNode():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

from collections import deque

def zigzag_icing_order(cupcakes):
    res = []

    queue = deque()
    child_queue = deque()

    child_list = []

    queue.appendleft(cupcakes)

    while queue:
        node = queue.popleft()
        
        if node.left:
            child_queue.append(node.left)
        if node.right:
            child_queue.append(node.right)
        


"""
            Chocolate
           /         \\
        Vanilla       Lemon
       /              /    \\
    Strawberry   Hazelnut   Red Velvet   
"""

# Using build_tree() function included at top of page
flavors = ["Chocolate", "Vanilla", "Lemon", "Strawberry", None, "Hazelnut", "Red Velvet"]
cupcakes = build_tree(flavors)