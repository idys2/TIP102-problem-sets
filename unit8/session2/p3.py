from common import build_tree, print_tree, TreeNode

'''
- add node to BST while preversing order

edge cases:
- duplicates: add to right subtree
- empty tree: create new node
'''
def add_plant(collection: TreeNode, name):
    prev = None
    curr = collection
    
    while curr:
        prev = curr
        if curr.val > name:
            curr = curr.left
        else:
            curr = curr.right
        
    if prev.val > name:
        prev.left = TreeNode(name)
    else:
        prev.right = TreeNode(name)

    return collection

"""
            Money Tree
        /              \\
Fiddle Leaf Fig    Snake Plant
"""

# Using build_tree() function at the top of page
values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of page
print_tree(add_plant(collection, "Aloe"))
print_tree(add_plant(collection, "Money Tree"))