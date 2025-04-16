from common import build_tree, print_tree, TreeNode

'''
- find the node to remove
- replace with inorder predecessor (greatest value less than the node)
    - find inorder predecessor
    - set links accordingly
'''
def remove_plant(collection: TreeNode, name: str):
    
    # find node to remove
    prev = None
    curr = collection
    while curr:
        if name < curr.val:
            prev = curr
            curr = curr.left
        elif name > curr.val:
            prev = curr
            curr = curr.right
        else:
            # deletion case (3 cases)

            # none (leaf node)
            if curr.left is None and curr.right is None:
                return None
            
            # 1 child
            if prev.val < curr.val:
                if curr.left:
                    prev.right = curr.left
                elif curr.right:
                    prev.right = curr.right
            
            elif prev.val > curr.val:
                if curr.left:
                    prev.left = curr.left
                elif curr.right:
                    prev.left = curr.right

            
            # 2 children



"""
              Money Tree
             /         \
           Hoya        Pilea
              \        /   \
             Ivy    Orchid  ZZ Plant
"""

# Using build_tree() function at the top of page
values = ["Money Tree", "Hoya", "Pilea", None, "Ivy", "Orchid", "ZZ Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of page
print_tree(remove_plant(collection, "Pilea"))